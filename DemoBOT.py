#載入函式庫
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#宣告類別
class DemoBOT:
    # 建立一個 ChatBot
    chatbot = ChatBot(
        # ChatBot 的名字
        "DemoBOT",
        input_adapter="chatterbot.input.VariableInputTypeAdapter",
        # 設定訓練的資料庫輸出於根目錄，並命名為 DemoBOT_DB.json
        database = "./DemoBOT_DB"    
    )

    def __init__(self):
        #ChatterBot中的訓練者設定
        self.chatbot.set_trainer(ChatterBotCorpusTrainer)
        #載入chinese中的檔案作為對話庫
        self.chatbot.train("chatterbot.corpus.chinese")

#獲得回應的副函式
    def getResponse(self, message=""):
        return self.chatbot.get_response(message)
