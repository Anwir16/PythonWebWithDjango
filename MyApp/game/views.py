from django.shortcuts import redirect, render
from game.game import Game
from game.forms import GameForm

current_game = None

def format_string(input_string):
    parts = input_string.split(" of ")
    if len(parts) == 2:
        x = parts[0]
        y = parts[1]
        return f"{y}/{x}"
    else:
        return "Invalid input format"
    
# Create your views here.
def start_game(request):
    global current_game
    if request.method == 'POST':
        s_form = GameForm(request.POST)
        if s_form.is_valid():
            level = s_form.cleaned_data['choice_level']
            bet_point = s_form.cleaned_data['choice_bet_point']
        current_game = Game(bet_point)
        current_game.auto_create_card()
        print(f'current_game: {current_game.player}')
        player_card = current_game.player.card
        context = {
        'player_card': format_string(player_card.__str__()),
        'house_card': 'back_card',
        'reward_point': current_game.current_reward,
        }
        if level == '1':
            return render(request, 'game/easy.html', context)
    else:
        s_form = GameForm()

    return render(request, 'home/dashboard.html', {'s_form': s_form})

def play_round(request):
    global current_game
    if current_game is None:
        return redirect('/')
    if request.method == 'POST':
        guess = request.POST.get('guess')
        if guess:
            current_game.play_round(guess)

    if current_game.player.points < 30 or current_game.player.points >= 1000:
        return redirect('game_over')

    context = {
        'player_card': current_game.player.card,
        'house_card': current_game.house.card,
        'player_points': current_game.player.points,
        'current_reward': current_game.current_reward,
    }
    return render(request, 'game/easy.html', context)