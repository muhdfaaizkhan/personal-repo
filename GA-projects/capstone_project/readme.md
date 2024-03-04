<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 5px; height: 70px">


# Training Mode Start! Training a Deep Learning Model for an AI-Controlled NPC
**DSI-41**: Muhammad Faaiz Khan

---

#### Background and Introduction 
___

Enemies in video games are designed to challenge and engage the player, an optimal gaming experience is where a player regards enemies as plausible threats that can feasibly be overcome.
Enemy NPCs (non-player characters) that are either too overwhelming or too easy will break the immersion for the player. Thus, there is a push for game developers to design ‘believable’ behavior in enemy NPCs.

#### Objectives
___

**Problem Statement**:
Utilising deep learning methods to train a non-player entity to behave in a believable and engaging way.


**Models**:

We will train a Convolutional Neural Network (CNN) on labelled screenshots from a video game. These screenshots shall be labelled with the inputs performed by the human player when the screenshot was taken, allowing the model to predict the appropriate input for a given screenshot. The model will then be used by a bot to perform keyinputs based on live screen captures from a running instance of the game.

Performance for the model is assesed on its accuracy score, losses during training, and its ability to defeat computer-controlled opponents in-game.

**Data collection**:

To collect our data, a function was designed to collect screen captures of the game screen, along with the corresponding inputs performed during the capture. 

**Bot behaviour**:

After training the model, we will need to interface the model with the game itself to perform actions within the game. A Python script was designed to run the model to perform predictions on a live feed from an active window playing the game, and to translate its predictions into keyboard inputs to interact with the game itself.

#### Data Dictionary
____
| Feature | Datatype | Details |
|----|---|-|
| SPACEBAR | int | 1/0 boolean indicating if the spacebar is pressed |
| a | int | 1/0 boolean indicating if the 'a' key is pressed |
| s | int | 1/0 boolean indicating if the 's' key is pressed |
| d | int | 1/0 boolean indicating if the 's' key is pressed |
| j | int | 1/0 boolean indicating if the 'j' key is pressed |
| k | int | 1/0 boolean indicating if the 'k' key is pressed |
| l | int | 1/0 boolean indicating if the 'l' key is pressed |
| isattack | int | 1/0 boolean indicating if 'j', 'k' or 'l' is pressed |

#### Model Refinement
___

To improve the performance of the model, we will train seperate models for a set of 3 defined opponents. This will allow the model to adopt matchup-specific behaviours in-game, thereby improving its performance.

Iterative improvements were made to the model to improve its predictive ability, as described below:

1. Bootstrapping rows with specific inputs

    Certain attacks are performed infrequently by the model, as the inputs for these attacks are underrepresented in the dataset. We want the model to utilise all available attacks under the appropriate conditions. Thus, we will bootstrap rows with these inputs to improve the model's confidence in predicting them.

2. Engineering additional data by flipping images

    Flip each image horizontally, then flip the left and right inputs corresponding to the image, to effectively double the number of datapoints available. This process generalises predictions by the model instead of overfitting based on screen position, thus improving the predictive ability of the model.

3. Customising thresholds for predicting inputs

    The stochastic nature of deep learning models results in varying prediction values between different models. To determine the appropriate threshold at which to perform inputs, we first monitor the predictions made by the model over the course of a round, and adapt our thresholds accordingly.

**Model Assessments**

The table below shows the final losses and accuracy scores for our 3 models.

| Model | Train loss | Val. loss | Train Acc. | Val. Acc |
|:--------------:|:-----------------:|:--------:|:--------:|----------------|
| 'poliwrath' |       0.454      |  0.455  |  0.787 |     0.783    |
|  'heracross' |       0.419      |  0.419  |  0.816  |     0.818     |
|      'mienshao'      |       0.429     |  0.428  |  0.811  |     0.808     |


#### Assumptions and Limitations
___

- A limitation for the data collection process is a lack of datapoints for specific scenarios due to the collection process. For example, the bot is unable to perform as well when cornered at the edge of the stage, due to a lack of datapoints in the training data in the corner. Bootstrapping such data will require more effort as we can only visually determine which datapoints fit this criteria.
- The bot is unable to perform actions that require a specific pattern of consecutive inputs, as it has no concept of historical information and only performs predictions based on the most recent screenshot.
- In the context of our problem statement, a key issue with the CNN model is the filesize of the trained model. Each model is approximately 900MB: it is unfeasible to implement this training method as it is for a standard video game with multiple different enemy types.
- Although individualised models help the bot to perform optimally and adapt based on the opponent detected, the models will perform poorly on other opponents as they are overfit on a particular opponent. A potential area to explore would be to train the model on all different enemies at once.

### Conclusions and future work
___

- To lower the filesize of the model, we can consider reducing the number of convlutional and linear layers, or reducing the dimensions of the input image. This may have adverse effects on the predictive ability of the model but can be explored as an area for improvement.
- As the data is already indexed by datetime, we can explore using a combination of a CNN and a Long Short-Term Memory Network (LSTM), so that our model can incorporate historical data for its predictions.