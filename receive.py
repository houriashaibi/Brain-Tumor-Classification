import pika
import sys
import os
# from keras.models import load_model
# import keras
# from keras.models import Sequential
# from keras.layers import Dense, Dropout, Flatten
# from keras.layers import Conv2D, MaxPooling2D, Conv3D, BatchNormalization, Activation
# from keras import backend as K
# from PIL import Image
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import OneHotEncoder
# import matplotlib.pyplot as plt
# from matplotlib.pyplot import imshow
# import pandas as pd

# # load model
# model = load_model('brain-tumor-model.h5')
# classes = os.listdir(
#     PATH+'Training')


# def names(number):
#     if(number == 0):
#         return classes[0]
#     elif(number == 1):
#         return classes[1]
#     elif(number == 2):
#         return classes[2]
#     elif(number == 3):
#         return classes[3]


# def analyze():
#     img = Image.open(PATH+'Testing/pituitary_tumor/image(15).jpg')
#     x = np.array(img.resize((150, 150)))
#     x = x.reshape(1, 150, 150, 3)
#     answ = model.predict_on_batch(x)
#     classification = np.where(answ == np.amax(answ))[1][0]
#     imshow(img)
#     print(str(answ[0][classification]*100) +
#           '% Confidence This Is ' + names(classification))

#     classification = str(answ[0][classification]*100) + \
#         '% Confidence This Is ' + names(classification)


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        # channel.stop_consuming()
        # channel2 = connection.channel()
        # channel2.queue_declare(queue='reply')
        # channel2.basic_publish(exchange='mom',
        #                        routing_key='hello',
        #                        body="classification")
        # print(" [x] Sent ")
        # channel.start_consuming()
        print(" [x] Received %r" % body)


    channel.basic_consume(
        queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')

    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
