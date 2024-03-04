'''
The model class for the CNN is included in its own script as it is used by the modelling notebook, the bot notebook and the bot script.
'''

from torch import nn, flatten

class CNN(nn.Module):
    def __init__(self):
        super().__init__()

        # Pre-checked length of vector after convolutional layers + flattening:
        length = 207296

        # Initialise list to plot loss, accuracy and recall over time
        self.hloss_train = []
        self.hacc_train = []
        self.hrec_train = []

        self.hloss_val = []
        self.hacc_val = []
        self.hrec_val = []

        # Shared convolutional layers
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=5, padding=1)
        self.conv3 = nn.Conv2d(32, 64, kernel_size=3, padding=1)

        # Pooling layer between convolutional layers
        self.pool = nn.MaxPool2d(2, 2)

        # Batch Normalization: commonly used in CNNs to improve training stability and speed up convergence. 
        self.batch_norm = nn.BatchNorm2d(64)
        
        self.linear1 = nn.Linear(length, 1028)
        self.linear2 = nn.Linear(1028, 256)
        self.linear3 = nn.Linear(256, 64)

        # Dropout layer, reduces overfitting by dropping out defined proportion of outputs
        self.drop = nn.Dropout(p=0.3)

        # Fully connected layer for output
        self.fc_output1 = nn.Linear(64, 8)

        # Activation functions
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    # Forward function
    def forward(self, x):
        # Forward pass through convolutional layers
        x = self.relu(self.conv1(x))
        x = self.pool(x)
        x = self.relu(self.conv2(x))
        x = self.pool(x)
        x = self.relu(self.conv3(x))
        x = self.pool(x)
        x = self.batch_norm(x)

        # Flatten the output before fully connected layers
        x = flatten(x, 1)

        '''When checking dimensions of image before flattening, uncomment (return x) below and comment the remaining layers'''
        # return x

        x = self.relu(self.linear1(x))
        x = self.drop(x)
        x = self.relu(self.linear2(x))
        x = self.drop(x)
        x = self.relu(self.linear3(x))
        x = self.drop(x)

        # Forward pass through fully connected layers
        output = self.sigmoid(self.fc_output1(x))

        return output
    
'''Uncomment below and run this script to check dimensions of flattened vector'''

# checkm = CNN()
# checkm = checkm.to(device)
# for i, data in enumerate(trainloader):
#     inputs, labels = data[0].to(device), data[1].to(device)
#     print(f'input shape: {inputs.shape}')
#     print(f'after flattening shape: {checkm(inputs).shape}')
#     break