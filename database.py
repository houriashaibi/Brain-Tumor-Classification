import mysql.connector
from PIL import Image
import io
import os
from keras.models import load_model
from PIL import Image
import numpy as np
import pika
from receive import main
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
    
    
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="jyupiter",
        password="15935789",
        database="pathogene"  # Name of the database
    )


def riddle(n):
  
        binary_data = io.BytesIO(n)

        img = Image.open(binary_data)
        x = np.array(img.resize((150,150)))
        x = x.reshape(1,150,150,3)
        answ = model.predict_on_batch(x)
        classification = np.where(answ == np.amax(answ))[1][0]
        oracle = str(answ[0][classification]*100) + '% Confidence This Is ' + names(classification)
        return oracle;
        

def main():
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()

    channel.queue_declare(queue='rpc_queue')
    #channel.exchange_declare(exchange='tut.rpc', exchange_type='direct')



    def on_request(ch, method, props, body):

      #  n = int.from_bytes(body, "big")

        print("classifying image...")
        response = riddle(body)
        print(riddle(body))
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
    print(' [*] Waiting for messages. To exit press CTRL+C')



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

