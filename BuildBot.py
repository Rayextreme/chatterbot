#載入函式庫
import sys
import pickle
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#宣告類別
class DemoBOT:
    # 建立一個 ChatBot
    chatbot = ChatBot(
        # ChatBot 的名字
        "DemoBOT",
        storage_adapter = "chatterbot.storage.JsonFileStorageAdapter",
        # 設定訓練的資料庫輸出於根目錄，並命名為 DemoBOT_DB.json
        database = "./DemoBOT_DB.json"    
    )

    def __init__(self):
        #ChatterBot中的訓練者設定
        self.chatbot.set_trainer(ChatterBotCorpusTrainer)
        #載入chinese中的檔案作為對話庫
        self.chatbot.train("chatterbot.corpus.chinese")

#獲得回應的副函式
    def getResponse(self, message=""):
        return self.chatbot.get_response(message)

#類似於C++的main
if __name__ == "__main__":
    #建立物件
    bot = DemoBOT()
    #儲存物件
    filehandler=open('ChatBot.obj','wb')
    pickle.dump(bot,filehandler)
    filehandler.close()
