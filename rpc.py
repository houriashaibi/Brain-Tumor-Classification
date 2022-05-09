from keras.models import load_model
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
import mysql.connector
from PIL import Image
from path import PATH
# load model
model = load_model('brain-tumor-model.h5')
classes = os.listdir(PATH+'Training')

def names(number):
    if(number == 0):
        return classes[0]
    elif(number == 1):
        return classes[1]
    elif(number == 2):
        return classes[2]
    elif(number == 3):
        return classes[3]

def riddle():
    img = Image.open(PATH+'Testing/pituitary_tumor/image(15).jpg')
    x = np.array(img.resize((150,150)))
    x = x.reshape(1,150,150,3)
    answ = model.predict_on_batch(x)
    classification = np.where(answ == np.amax(answ))[1][0]
    imshow(img)
    oracle = str(answ[0][classification]*100) + '% Confidence This Is ' + names(classification)
    return oracle;



import pika

def connect():
   return  mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="studentdb"  # Name of the database
)
mydb = connect()

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')
#channel.exchange_declare(exchange='tut.rpc', exchange_type='direct')



def on_request(ch, method, props, body):
   # n = int(body)

    print("classifying image...")
    response = riddle()
    print(riddle())
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()