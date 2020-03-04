from keras.models import model_from_json
import cv2
import os
import numpy as np

def Test_Images():

    total = 0
    num_suc = 0
    for filename in os.listdir('test'):

        print("\n")
        image = cv2.imread('test/' + filename)
        cv2.imshow("test_image", image)
        image = cv2.resize(image, (360, 640))

        image = np.array(image).reshape(-1, 360, 640, 3)

        expected = int(filename[0])
        prediction = model.predict(image)
        # score, acc = model.evaluate(image, expected)
        # print(score, acc)
        
        # if(expected == prediction):
        #     print('Success\nPrediction: ', prediction)
        #     print('Expected: ', expected)
        #     num_suc += 1
        # else:
        #     print('Fail\nPrediction: ', prediction)
        #     print('Expected: ', expected)
        
        # total += 1
        print(prediction)

        # cv2.waitKey()
    # print(num_suc/total)

def Live_Test():

    cap = cv2.VideoCapture(0)
    
    ret, frame = cap.read()

    y = 0
    x = 0
    w = 256
    h = 256
    while(ret):

        image = frame[y:y+h, x:x+w]

        cv2.imshow("frame", image)

        image = cv2.resize(image, (360, 640))
        # image = image.flatten()
        image = np.array(image, dtype="float") / 255.0

        image = np.array(image).reshape(-1, 360, 640, 3)
        prediction = model.predict_classes(image)
        
        print(prediction)
        cv2.waitKey(10)
        ret, frame = cap.read()



json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)

model.load_weights('weights1.h5')

# Live_Test()
Test_Images()