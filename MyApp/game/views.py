from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from game.game import Game
from game.player import Player
from django.http import JsonResponse
from user.models import Profile
import re
from game.card import Card

@login_required(login_url='user:login')
def start_game(request):
    if request.method == 'POST':
        user = request.user
        profile = Profile.objects.get(user=user)
        result = ""
        show_house_card = 'back_card'

        if 'current_reward' in request.session:
            # If game state already exists in session, restore the game
            bet_point = int(request.session.get('bet_point'))
            player_card = request.session.get('player_card')
            house_card = request.session.get('house_card')
            show_house_card = request.session.get('show_house_card')
            current_reward = request.session.get('current_reward')
            result = request.session.get('result')
            print(f'exist result: {result}')
            print(f'show_house_card: {show_house_card}')

            player = Player(name=user.username, point=profile.point, user=user)
            print(f'player_point: {player.points}')
            print(f'bet_point: {bet_point}')
            if player.points < bet_point:
                error = f"Please enter bet point less {player.points}!"
                return render(request, 'home/dashboard.html', {'error' : error})
            current_game = Game(bet_point=bet_point, player=player)
            current_game.current_reward = current_reward

            current_game.player.card = Card.from_string(player_card)
            current_game.house.receive_card(Card.from_string(house_card))
        else:
            # Initialize a new game
            player = Player(name=user.username, point=profile.point, user=user)
            bet_point = request.POST.get('choice_bet_point')
            if not bet_point:
                error = "Please top up to continue!"
                return render(request, 'home/dashboard.html', {'error' : error})
            elif not bet_point.isdigit():
                error = "Bet point must be an integer!"
                return render(request, 'home/dashboard.html', {'error' : error})
            elif player.points < int(bet_point):
                error = f"Please enter bet point less {player.points}!"
                return render(request, 'home/dashboard.html', {'error' : error})
            current_game = Game(bet_point=bet_point, player=player)
            current_game.auto_create_card()

            request.session['bet_point'] = bet_point
            request.session['player_card'] = current_game.player.card.__str__()
            request.session['house_card'] = current_game.house.card.__str__()
            request.session['show_house_card'] = show_house_card
            request.session['current_reward'] = current_game.current_reward
            request.session['result'] = ''
        
        print(f'final result: {result}')
        context = {
            'player_card': current_game.player.card.__str__(),
            'house_card': show_house_card,
            'reward_point': current_game.current_reward,
            'result': result,
        }
        return render(request, 'game/easy.html', context)
    return render(request, 'home/dashboard.html')

@login_required(login_url='user:login')
def play_round(request):
    result = ""
    house_card = "back_card"
    current_reward_ = request.session.get('current_reward')
    print(f'current_reward: {current_reward_}')
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'POST':
        
        guess = request.POST.get('guess', '')
        print(f'guess: {guess}')
        action = request.POST.get('action', '')
        print(f'action: {action}')
        
        bet_point = request.session.get('bet_point')
        player_card = request.session.get('player_card')
        house_card = request.session.get('house_card')
        show_house_card = request.session.get('show_house_card')
        current_reward = request.session.get('current_reward')
        print(f'current_reward: {current_reward}')
        
        user = request.user
        profile = Profile.objects.get(user=user)
        player = Player(name=user.username, point=profile.point, user=user)
        current_game = Game(bet_point=bet_point, player=player)
        current_game.current_reward = current_reward
        current_game.player.card = Card.from_string(player_card)
        current_game.house.receive_card(Card.from_string(house_card))
        
        if re.match("^(greater|less)$", guess):
            result = current_game.play_round(guess)
            print(f'result: {result}')
            house_card =  current_game.house.card.__str__()
            request.session['show_house_card'] = house_card
            request.session['current_reward'] = current_game.current_reward
            request.session['result'] = result
        elif action == 'Continue':
            current_game.auto_create_card()
            request.session['bet_point'] = bet_point
            request.session['player_card'] = current_game.player.card.__str__()
            request.session['house_card'] = current_game.house.card.__str__()
            request.session['show_house_card'] = 'back_card'
            request.session['result'] = ""
        else:
            profile.point += current_game.current_reward
            profile.save()
            result = 'Game over'
            del request.session['bet_point']
            del request.session['player_card']
            del request.session['house_card']
            del request.session['current_reward']
            del request.session['show_house_card']
            del request.session['result']
        
        context = {
            'player_card': current_game.player.card.__str__(),
            'house_card': show_house_card,
            'player_points':  profile.point,
            'reward_point': current_game.current_reward,
            'result' : result,
        }
        
        
        
        return JsonResponse(context)
    return JsonResponse({'error': 'Invalid request'}, status=400)