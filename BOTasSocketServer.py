#載入函式庫
import sys
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#宣告類別
class DemoBOT:
    # 類別內含一個import的ChatBot物件
    chatbot = ChatBot(
        # ChatBot 的名字
        "DemoBOT",
        #這一行我看不是很有
        storage_adapter = "chatterbot.storage.JsonFileStorageAdapter",
        # 設定訓練的資料庫輸出於根目錄之目錄，並命名為 DemoBOT_DB.json
        database = "./DemoBOT_DB.json"    
    )
    #建構子
    def __init__(self):
        #ChatterBot中的訓練者設定，沒有深入研究
        self.chatbot.set_trainer(ChatterBotCorpusTrainer)
        #載入chinese中的檔案作為對話庫，固定路徑寫在函式內
        self.chatbot.train("chatterbot.corpus.chinese")

#獲得回應的副函式
    def getResponse(self, message=""):
        #chatbot內建的方法，用來取得對message做為輸入時機器人的回應
        return self.chatbot.get_response(message)
        

#類似於C++的main
if __name__ == "__main__":
    #socket define
    import socket
    #沒有深入研究
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8001))  
    #監聽指令，沒有深入研究
    sock.listen(5)
     #socket definend
    
    #建立聊天機器人物件
    bot = DemoBOT()
    
    print('\ndone\n')#告知建立完成
    
    s="";
    #呼叫回應副函式獲得回應

    connection,address = sock.accept()
        
    while(True):
        #前IP，後port
        try:
            connection.settimeout(5)
            buf = connection.recv(1024)
            print(buf.decode("utf-8"))
            s = bot.getResponse(buf.decode("utf-8"))
            connection.send(str(s).encode('utf-8'))
        except socket.timeout:
            print('socket time out')
            
    connection.close()
        
    
