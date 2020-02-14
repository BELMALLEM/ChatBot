from actions import actions
from text_process import text_process
# restore all of our data structures
import pickle

# things we need for Tensorflow
import numpy as np
import tflearn
import random
# import our chat-bot intents file
import json

with open('intents.json') as json_data:
    intents = json.load(json_data)

data = pickle.load( open("training_data", "rb"))
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']

#load our saved model
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 15)
net = tflearn.fully_connected(net, 15)
net = tflearn.fully_connected(net, len(train_y[0]), activation = 'softmax')
net = tflearn.regression(net)
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
model.load('model.tfl')

# create a data structure to hold user context
context = {}

ERROR_THRESHOLD = 0
#classify the sentence in wich class is to get the right response
def classify(sentence):
    # generate probabilities from the model
    results = model.predict([text_process.bow(sentence, words)])[0]
    # filter out predictions below a threshold
    results = [[i,r] for i,r in enumerate(results) ]#if r>ERROR_THRESHOLD]

    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1])) # that's why we used enumerate to have the order of the result
    # return tuple of intent and probability
    return return_list

# the fonction that control the given actions by the classfication
def control_actions(sentence, i):
    print("control action nw")
    action = i['action']
    x = actions()
    if action == "search":
        x.search(sentence)
    #elif action == "news":     for the news
        #x.news()
    elif action == "services":
        print('services')
        x.get_services()
    elif action == "hosting":
        x.search("hosting")
        print("In our world you encounter 4 hosting types:")
        print("- Pro\n- Lite\n- Rebuy\n- Info-Managed")
        print("You can choose one to talk more")
    #elif action == "server":
    elif action == "dmn_nm":
        x.get_domain_nm(input("Enter please your domain name as (.com, .ma, ...)"))
    elif action == "host-pro" or action == "host-lite" or action == "host-info" or action == "host-rebuy":
        x.get_host_plan(i['path'])


# this little function uses classify() to know how to respond and then she does what she have and create the context structure
def response(sentence, userID='123', show_details=False):
    results = classify(sentence)
    # if we have a classification then find the matching intent tag
    # loop as long as there are matches to process
    while results:
        for i in intents['intents']:
            # find a tag matching the first result
            if i['tag'] == results[0][0]:
                if 'action' in i:
                    print("action="+i['action'])
                    control_actions(sentence, i)
                 # set context for this intent if necessary
                if 'context_set' in i:
                    if show_details: print('context:', i['context_set'])
                    context[userID] = i['context_set']

                    # check if this intent is contextual and applies to this user's conversation
                if not 'context_filter' in i or \
                    (userID in context and 'context_filter' in i and i['context_filter'] == context[userID]):
                    if show_details: print ('tag:', i['tag'])
                    # a random response from the intent
                    return print(random.choice(i['responses']))
            results.pop(0)


message = input("YOU: ")
while(message):
    print(classify(message)[0])
    response(message)
    message = input("YOU: ")
