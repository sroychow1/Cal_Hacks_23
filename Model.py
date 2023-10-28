import torch
import torch.nn as nn
import torch.optim as optim

class BinaryClassificationNN(nn.Module):
    def __init__(self, input_dim):
        super(BinaryClassificationNN, self).__init__()
        
        self.fc1 = nn.Linear(input_dim, 512)  # First fully connected layer
        self.relu1 = nn.ReLU()  # ReLU activation function
        self.dropout1 = nn.Dropout(0.2)  # Dropout layer with 50% drop probability
        
        self.fc2 = nn.Linear(512, 256)  # Second fully connected layer
        self.relu2 = nn.ReLU()  # ReLU activation function
        self.dropout2 = nn.Dropout(0.4)  # Dropout layer with 50% drop probability
        
        self.fc3 = nn.Linear(256, 128)  # Third fully connected layer
        self.relu3 = nn.ReLU()  # ReLU activation function
        self.dropout3 = nn.Dropout(0.3)  # Dropout layer with 50% drop probability
        
        self.fc4 = nn.Linear(128, 1)  # Fourth fully connected layer
        
        self.sigmoid = nn.Sigmoid()  # Sigmoid activation function for binary classification

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu1(out)
        out = self.dropout1(out)
        
        out = self.fc2(out)
        out = self.relu2(out)
        out = self.dropout2(out)
        
        out = self.fc3(out)
        out = self.relu3(out)
        out = self.dropout3(out)
        
        out = self.fc4(out)
        
        out = self.sigmoid(out)  # Output should be a single scalar between 0 and 1
        return out

class BinaryClassificationLSTM(nn.Module):
    def __init__(self, input_size=17, hidden_size=128, num_layers=2):
        super(BinaryClassificationLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)  # Binary classification

    def forward(self, x):
        # LSTM layer
        out, (hn, cn) = self.lstm(x)
        # Take the output from the last time step
        out = out[:, -1, :]
        # Fully connected layer
        out = torch.sigmoid(self.fc(out))
        return out

# Assume each data point has been reshaped to have 48 time steps, each with 17 features
# Your input data should now have a shape of [batch_size, 48, 17]
model = BinaryClassificationLSTM()


