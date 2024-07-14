from django.shortcuts import redirect, render
from game.game import Game
from game.forms import GameForm
from game.player import Player
from django.contrib.auth.models import User
from user.models import Profile

current_game = None
player = None
profile = None
bet_point = 0

def format_string(input_string):
    parts = input_string.split(" of ")
    if parts and len(parts) == 2:
        x = parts[0]
        y = parts[1]
        return f"{y}/{x}"
    return input_string

def start_game(request):
    global current_game, profile, player, bet_point
    
    if request.method == 'POST':
        s_form = GameForm(request.POST)
        user = request.user
        profile = Profile.objects.get(user=user)
        if s_form.is_valid():
            level = s_form.cleaned_data['choice_level']
            bet_point = s_form.cleaned_data['choice_bet_point']
        current_game = Game(bet_point)
        player = Player(name=user.username, point=profile.point)
        current_game.player = player
        current_game.auto_create_card()
        player_card = current_game.player.card
        context = {
        'player_card': format_string(player_card.__str__()),
        'house_card': 'back_card',
        'reward_point': current_game.current_reward,
        'result' : '',
        }
        if level == '1':
            return render(request, 'game/easy.html', context)
    else:
        s_form = GameForm()

    return render(request, 'home/dashboard.html', {'s_form': s_form})

def play_round(request):
    global current_game, bet_point, profile
    result = ""
    house_card = "back_card"
    if current_game is None:
        print(f'current_game: {current_game}')
        return redirect('/')
    if request.method == 'POST':
        guess = request.POST.get('guess')
        print(f'guess: {guess}')
        if guess in ('less','greater'):
            result = current_game.play_round(guess)
            if result == 'Wrong':
                profile.point -= bet_point
                profile.save()
            house_card =  format_string(current_game.house.card.__str__())
            print(f'result:{result}')
        elif guess == 'Continue':
            current_game.auto_create_card()
        else:
            profile.point += current_game.current_reward
            profile.save()
            current_game = None
            return redirect('/')
    if current_game.player.points < 30 or current_game.current_reward >= 1000:
        return redirect('/')
    context = {
        'player_card': format_string(current_game.player.card.__str__()),
        'house_card': house_card,
        'player_points': current_game.player.points,
        'reward_point': current_game.current_reward,
        'result' : result,
    }
    return render(request, 'game/easy.html', context)