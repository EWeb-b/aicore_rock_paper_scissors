# Computer Vision Rock Paper Scissors
> A computer-vision Rock-Paper_Scissors game. The model was trained using Teachable Machine.

## Milestone 1: Create the Model
- The model was trained using Teachable Machine. It allows for a rapid computer-vision training process which is also free to use.
- The model was downloaded as a Tensorflow/Keras model along with its labels.

## Milestone 2: Install the Dependancies
- A virtual envrionment was created using conda and the required packages were installed: opencv-python, tensorflow, and ipykernel.
- A list of all the required libraries was created using 

```Python
pip list > requirements.txt
```

### Milestone 3: Create a Rock-Paper-Scissors Game
- Created the maunal_rps.py file to maunally play Rock-Paper-Scissors with the computer.
- The function get_computer_choice uses the random Python library to randomly return the computer's choice of rock, paper, or scissors.
- Created the function get_user_choice which uses the input method to obtain the user's choice from the keyboard.
- Finally created the get_winner function which compares the computer's and user's choices to calculate and display the winner.
