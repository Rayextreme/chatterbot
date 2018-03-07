#載入函式庫
import sys
import pickle
from DemoBOT import DemoBOT
#類似於C++的main
#if __name__ == "__main__":
#    #建立物件
#   bot = DemoBOT()
    #儲存物件
#    filehandler=open('ChatBot.obj','wb')
#    bot.__module__= 'DemoBOT'
#    pickle.dump(bot,filehandler,protocol=2)
#    filehandler.close()

#un __main__
bot = DemoBOT()
filehandler=open('ChatBot.obj','wb')
DemoBOT.__module__= 'DemoBOT'
pickle.dump(bot,filehandler,protocol=2)
filehandler.close()
