from datetime import datetime as dt
from random import randint


def access_control(func):
    def wrapper(self, *args, **kwargs):
        if GuessNumber.admin_username == self.name:
            result = func(self, *args, **kwargs)
            return result
        else:
            print(GuessNumber.unknown_comand)
    return wrapper


class GuessNumber():
    admin_username = 'Admin'
    unknown_comand = 'Неизвестная команда, попробуйте еще раз!'

    def __init__(self):
        self.total_games = 0
        self.start_game_time = dt.now()

    def get_username(self):
        self.name = input(
            'Представьтесь, пожалуйста, как Вас зовут?\n').strip()
        if self.name == GuessNumber.admin_username:
            print(
                '\nДобро пожаловать, создатель! '
                'Во время игры вам доступны команды "stat", "answer"'
            )
        else:
            print(f'\n{self.name}, добро пожаловать в игру!')

    def play_game(self):
        number = randint(1, 100)
        print(
            '\nУгадайте число от 1 до 100.\n'
            'Для выхода из текущей игры введите команду "stop"'
        )
        while True:
            user_input = input('Введите число или команду: ').strip().lower()
            match user_input:
                case 'stop':
                    break
                case 'stat':
                    self.get_statistics()
                case 'answer':
                    self.get_right_answer(number)
                case _:
                    try:
                        guess = int(user_input)
                    except ValueError:
                        print(GuessNumber.unknown_comand)
                        continue

                    if self.check_number(guess, number):
                        break

    def check_number(self, guess, number):
        if guess == number:
            print(f'Отличная интуиция, {self.name}! Вы угадали число :)')
            return True

        if guess < number:
            print('Ваше число меньше того, что загадано.')
        else:
            print('Ваше число больше того, что загадано.')
        return False

    def add_game(self):
        self.total_games += 1

    @access_control
    def get_statistics(self, *args, **kwargs):
        game_time = dt.now() - self.start_game_time
        total_seconds = int(game_time.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(
            f'Время игры: {hours:02}:{minutes:02}:{seconds:02}, '
            f'текущая игра - №{self.total_games}')

    @access_control
    def get_right_answer(self, number, *args, **kwargs):
        print(f'Правильный ответ: {number}')
