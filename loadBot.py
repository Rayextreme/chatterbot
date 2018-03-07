#coding:utf-8
import pickle
import sys


if __name__ == "__main__":
    #呼叫物件
    filehandler = open('ChatBot.obj', 'rb') 
    bot = pickle.load(filehandler)

    #呼叫回應副函式獲得回應
    print(bot.getResponse('還不錯'))
