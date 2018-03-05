# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
import logging
import pickle
import sys
from flask import Flask
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class DemoBOT:
    chatbot = ChatBot(
        "DemoBOT",
        input_adapter = "chatterbot.input.VariableInputTypeAdapter",
        database = "./DemoBOT_DB.json"    
    )

    def __init__(self):
        self.chatbot.set_trainer(ChatterBotCorpusTrainer)
        self.chatbot.train("chatterbot.corpus.chinese")

    def getResponse(self, message=""):
        return self.chatbot.get_response(message)

filehandler = open('ChatBot.obj', 'rb') 
bot = pickle.load(filehandler)

args_on = bot.getResponse('還不錯');

#args_on = [arg for arg in self.request.arguments() if self.request.get(arg) == 'on']

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return args_on


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    filehandler = open('ChatBot.obj', 'rb') 
    bot = pickle.load(filehandler)
    print(bot.getResponse('還不錯'))
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END app]
