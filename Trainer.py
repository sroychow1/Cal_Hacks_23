import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.tensorboard import SummaryWriter
from torch.utils.data import DataLoader
from torch.utils.data import random_split
import torchvision
from Dataloader import ToxicCommentDataset
from Model import BinaryClassificationNN
import intel_extension_for_pytorch as ipex
# Initialize TensorBoard writer
writer = SummaryWriter()

dataset = ToxicCommentDataset(path_to_csv='/home/ubuntu/Cal_Hacks_23/train.csv')

total_length = len(dataset)
print(total_length)
train_size = int(0.0001 * total_length)    
val_size = int(0.0001 * total_length)
print(val_size)
remaining = total_length - train_size - val_size

train_dataset, val_dataset, _ = random_split(dataset, [train_size, val_size, remaining])

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

# Define loss function and optimizer


#Model Intialization
model = BinaryClassificationNN(827)
model = model.to('cpu')
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
model, optimizer = ipex.optimize(model, optimizer=optimizer, dtype=torch.float32)





# Define the number of epochs
num_epochs = 1

for epoch in range(num_epochs):
    print("epoch=", epoch)
    model.train()  # Set the model to training mode
    running_loss = 0.0
    
    for i, (inputs, labels) in enumerate(train_loader):
        print("epoch=", epoch, "i=", i)
        # Zero the parameter gradients
        optimizer.zero_grad()
        
        # Forward pass
        outputs = model(inputs)
        loss = criterion(outputs.squeeze(), labels.float())
        
        # Backward pass and optimization
        loss.backward()
        optimizer.step()
        
        # Update running loss
        running_loss += loss.item()
        
        # Log loss to TensorBoard every 10 batches
        if i % 10 == 9:
            writer.add_scalar('training loss', running_loss / 10, epoch * len(train_loader) + i)
            running_loss = 0.0
    
    # Save a checkpoint every epoch
    torch.save({
        'epoch': epoch,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'loss': loss,
    }, f'checkpoint{epoch}.pth')
    
    # Validate the model
    model.eval()  # Set the model to evaluation mode
    val_loss = 0.0
    with torch.no_grad():
        for inputs, labels in val_loader:
            outputs = model(inputs)
            print(labels)
            print(labels.float())
            loss = criterion(outputs.squeeze(), labels.float())
            val_loss += loss.item()
    
    # Log validation loss to TensorBoard
    writer.add_scalar('validation loss', val_loss / len(val_loader), epoch)
    print(f'Epoch {epoch}, Validation Loss: {val_loss / len(val_loader)}')

# Save training parameters
torch.save(model.state_dict(), 'final_model.pth')

# Close the TensorBoard writer
writer.close()
