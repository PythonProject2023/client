import unittest
from unittest.mock import MagicMock, patch
import kivy
from kivy.uix.button import Button
import sys
import socket
import io
import parser
import app


class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sock = MagicMock(spec=socket.socket)
        cls.sock.send.return_value = cls.sock
        app.sock = cls.sock
        app.widgets = {'text_fields': {'answer': Button(text='text')}}

    def test_1_choose_button(self):
        app.choose_button('прекрасный дагестан', 300)
        exp_call = unittest.mock.call(("choose 'прекрасный дагестан' 300\n").encode())
        self.sock.send.assert_has_calls(exp_call)
        
    def test_2_answer_button(self):
        app.answer_button('test')
        exp_call = unittest.mock.call(("choose 'прекрасный дагестан' 300\n").encode())
        self.sock.send.assert_has_calls(exp_call)
        
    def test_3_choose_button(self):
        app.choose_button('прекрасный дагестан', 300)
        exp_call = unittest.mock.call(("choose 'прекрасный дагестан' 300\n").encode())
        self.sock.send.assert_has_calls(exp_call)
        
    def test_4_choose_button(self):
        app.choose_button('прекрасный дагестан', 300)
        exp_call = unittest.mock.call(("choose 'прекрасный дагестан' 300\n").encode())
        self.sock.send.assert_has_calls(exp_call)
        
class TestParser(unittest.TestCase):
    def test_1(self):
        res = parser.parse_package('test.siq')
        ans = parser.Package()
        ans.set_author('test')
        r = parser.Round('first')
        th1 = parser.Theme('th1')
        q = parser.Question(100, text='txt')
        q.add_answer(parser.Answer('ans1'))
        th1.add_question(q)
        q = parser.Question(200, text='txt')
        q.add_answer(parser.Answer('ans2'))
        th1.add_question(q)
        q = parser.Question(300, text='txt')
        q.add_answer(parser.Answer('ans3'))
        th1.add_question(q)
        th2 = parser.Theme('th2')
        q = parser.Question(100, text='txt txt')
        q.add_answer(parser.Answer('ans1 ans1'))
        th2.add_question(q)
        q = parser.Question(200, text='txt txt')
        q.add_answer(parser.Answer('ans2 ans2'))
        th2.add_question(q)
        q = parser.Question(300, text='txt txt')
        q.add_answer(parser.Answer('ans3 ans3'))
        th2.add_question(q)
        r.add_theme(th1)
        r.add_theme(th2)
        ans.add_round(r)
        r = parser.Round('second')
        th1 = parser.Theme('th1')
        q = parser.Question(100, text='txt')
        q.add_answer(parser.Answer('ans1'))
        th1.add_question(q)
        q = parser.Question(200, text='txt')
        q.add_answer(parser.Answer('ans2'))
        th1.add_question(q)
        th2 = parser.Theme('th2')
        q = parser.Question(100, text='txt')
        q.add_answer(parser.Answer('ans1'))
        th2.add_question(q)
        q = parser.Question(200, text='txt')
        q.add_answer(parser.Answer('ans2'))
        th2.add_question(q)
        th3 = parser.Theme('th3')
        q = parser.Question(100, text='txt')
        q.add_answer(parser.Answer('ans1'))
        th3.add_question(q)
        q = parser.Question(200, text='txt')
        q.add_answer(parser.Answer('ans2'))
        th3.add_question(q)
        r.add_theme(th1)
        r.add_theme(th2)
        r.add_theme(th3)
        ans.add_round(r)
        self.assertEqual(res, ans)
