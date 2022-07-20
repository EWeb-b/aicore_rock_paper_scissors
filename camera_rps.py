import cv2
from keras.models import load_model
import numpy as np
import random
import time
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


def get_computer_choice():
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    return computer_choice

def get_user_choice():
    user_choice = input("Choose Rock, Paper, or Scissors >")
    print("You chose {}".format(user_choice))
    return user_choice

def get_winner(computer_choice, user_choice):
    c, u = computer_choice, user_choice
    if (c == u): print("Draw")
    elif ((c == "Rock" and u == "Scissors") or (c == "Paper" and u == "Rock") or (c == "Scissors" and u == "Paper")):
        print("Computer Wins")
    elif ((u == "Rock" and c == "Scissors") or (u == "Paper" and c == "Rock") or (u == "Scissors" and c == "Paper")):
        print("User Wins")

def get_prediction(prediction):
    options = ["Rock", "Paper", "Scissors", "Nothing"]
    cam_pred = options[np.argmax(prediction)]
    return cam_pred

start_time = time.time()
print("You have 5 seconds to choose.")

while True:

    elapsed_time = time.time() - start_time
    remaining_time = 5 - elapsed_time
    #print("You have {:.0f} seconds left".format(remaining_time))
    
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window

    if (remaining_time < 0):
        user_choice = get_prediction(prediction)
        computer_choice = get_computer_choice()
        print("You chose: {}".format(user_choice))
        print("Computer choice was: {}".format(computer_choice))
        get_winner(computer_choice, user_choice)

        print("You have 5 seconds to choose.")
        start_time = time.time()
        remaining_time = 5
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()


