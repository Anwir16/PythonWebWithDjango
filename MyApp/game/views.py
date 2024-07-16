from django.shortcuts import redirect, render
from game.game import Game
from game.player import Player
from django.http import JsonResponse
from user.models import Profile
import re

current_game = player = None
bet_point = 0

def start_game(request):
    global current_game, profile, _player, bet_point
    
    if request.method == 'POST':
        user = request.user
        profile = Profile.objects.get(user=user)
        _bet_point = int(request.POST.get('choice_bet_point'))
        _player = Player(name=user.username, point=profile.point, user=user)
        current_game = Game(bet_point=_bet_point, player=_player)
        current_game.auto_create_card()
        print(f's_current_game: {current_game}')
        player_card = current_game.player.card
        print(f's_player_card: {player_card}')
        context = {
        'player_card': player_card.__str__(),
        'house_card': 'back_card',
        'reward_point': current_game.current_reward,
        'result' : '',
        }
        return render(request, 'game/easy.html', context)
    return render(request, 'home/dashboard.html')

def play_round(request):
    global current_game, bet_point
    result = ""
    house_card = "back_card"
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'POST':
        guess = request.POST.get('guess', None)
        action = request.POST.get('action', None)
        print(f'guess: {guess}')
        user = request.user
        profile = Profile.objects.get(user=user)
        if re.match("^(greater|less)$", guess):
            result = current_game.play_round(guess)
            print(f'result: {result}')
            house_card =  current_game.house.card.__str__()
        elif action == 'Continue':
            current_game.auto_create_card()
        else:
            profile.point += current_game.current_reward
            profile.save()
            result = 'Game over'
        context = {
            'player_card': current_game.player.card.__str__(),
            'house_card': house_card,
            'player_points':  profile.point,
            'reward_point': current_game.current_reward,
            'result' : result,
        }
        return JsonResponse(context)
    return JsonResponse({'error': 'Invalid request'}, status=400)