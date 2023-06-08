import shlex
import socket
import threading

class Client:
    name = ''
    score = 0
    socket = None
    active = False
    ans_button = False
    
    def recieve(self):
        while thread_alive:
            ans = bytearray()
            ans = self.socket.recv(4096)
            ans = shlex.split(ans.decode().rstrip())
            match ans:
                case ['login', state]:
                    if state == 'error':
                        #вывод сообщения о неверном пароле?
                    else:
                        #переход на экран игры
                case ['active']:
                    #оповестить пользователя, что он выбирает вопрос
                    self.active = True
                case ['q:', x, y, txt]:
                    #убрать клетку из таблицы, вывести текст вопроса, начать отсчёт 2 мин?
                    ans_button = True
                case ['typing', name]:
                    if name == self.name:
                        #открыть поле ввода, начать отсчёт 20 сек?, поменять текст кнопки
                    else:
                        #кто-то уже начал отвечать
                        self.ans_button = False
                case ['a:', player, txt]:
                    #заменить вопрос на данный ответ (или дописать?)
                case ['ans', 'right']:
                    #мб подсветим текст/поле зелёным?
                case ['ans', 'wrong']:
                    #мб подсветим текст/поле красным?
                    self.ans_button = True
                case ['score', player, points]:
                    #отрисовать изменения
                    
    def request(self, s):
        self.socket.send((s + '\n').encode())
    
    def __init__(self, player_name, gui_object):
        self.name = player_name
        self.gui = gui_object
        
    def start_game(self, game_name, password):
        #происходит соединение с ведущим-сервером не знаю пока как
        pass
        
    def select_question(self, x, y):
        #выбор вопроса
        if self.active:
            self.active = False
            self.request(f'select {self.name} {x} {y}')
            
    def type_answer(self):
        #уведомляю, что начал отвечать -> отключить другим игрокам кнопки
        if self.ans_button:
            self.request(f'typing {self.name}')
            #с разрешения сервера открываем поле ввода, начинаем отсчёт
            
    def send_answer(self, text):
        self.request(f'ans {self.name} {text}')
        #убираем поле ввода, меняем текст кнопки
