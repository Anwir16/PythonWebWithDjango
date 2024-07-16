from django.shortcuts import redirect, render
from game.game import Game
from game.player import Player
from django.http import JsonResponse
from user.models import Profile

current_game = player = profile = None
bet_point = 0

def start_game(request):
    global current_game, profile, player, bet_point
    
    if request.method == 'POST':
        user = request.user
        profile = Profile.objects.get(user=user)
        bet_point = int(request.POST.get('choice_bet_point'))
        current_game = Game(bet_point)
        player = Player(name=user.username, point=profile.point)
        current_game.player = player
        if profile.point >= bet_point:
            current_game.auto_create_card()
            player_card = current_game.player.card
            print(f'player_card: {player_card}')
            result = ''
        else:
            player_card = 'back_card'
            result = 'Game over'
        context = {
        'player_card': player_card.__str__(),
        'house_card': 'back_card',
        'reward_point': current_game.current_reward,
        'result' : result,
        }
        return render(request, 'game/easy.html', context)
    return render(request, 'home/dashboard.html')

def play_round(request):
    global current_game, bet_point, profile
    result = ""
    house_card = "back_card"
    if current_game is None:
        print(f'current_game: {current_game}')
        return JsonResponse({'redirect' : '/'})
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'POST':
        guess = request.POST.get('guess', None)
        action = request.POST.get('action', None)
        print(f'guess: {guess}')
        if guess in ('less','greater'):
            result = current_game.play_round(guess)
            house_card =  current_game.house.card.__str__()
            if result == 'Wrong':
                print(f'before : {profile.point}')
                profile.point -= bet_point
                print(f'after : {profile.point}')
                profile.save()
            print(f'result:{result}')
        elif action == 'Continue':
            current_game.auto_create_card()
        else:
            profile.point += current_game.current_reward
            profile.save()
            current_game = None
            return JsonResponse({'redirect' : '/'})
        print(f'profile.point: {profile.point}')
        if profile.point < bet_point:
            current_game = None
            return JsonResponse({'redirect' : '/'})
        elif current_game.current_reward >= 1000:
            profile.point += current_game.current_reward
            profile.save()
            current_game = None
            return JsonResponse({'redirect' : '//'})
        context = {
            'player_card': current_game.player.card.__str__(),
            'house_card': house_card,
            'player_points':  profile.point,
            'reward_point': current_game.current_reward,
            'result' : result,
        }
        return JsonResponse(context)
    return JsonResponse({'error': 'Invalid request'}, status=400)