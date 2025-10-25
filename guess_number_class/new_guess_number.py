from games_class import GuessNumber


def guess_number():
    game = GuessNumber()
    game.get_username()

    while True:
        game.add_game()
        game.play_game()
        play_again = input('\nХотите сыграть ещё? (yes/no): ').strip().lower()
        if play_again not in ('y', 'yes'):
            break


if __name__ == '__main__':
    print(
        'Вас приветствует игра "Угадай число"!\n'
        'Для выхода нажмите Ctrl+C'
    )
    guess_number()
