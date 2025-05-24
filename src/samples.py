import os
import pytorch_lightning as pl
from model.network_module import ParametersClassifier
import os
import time
import torch
from PIL import Image
import pytorch_lightning as pl
from torchvision import transforms

preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.4815, 0.4578, 0.4082], std=[0.2686, 0.2613, 0.2758])
])



# Hardcoded checkpoint path
checkpoint_path = "/home/poundspb/Computer Vision/caxton_fork/src/checkpoints/21052025/1234/MHResAttNet-dataset_full-21052025-epoch=09-val_loss=37.10-val_acc=0.46.ckpt"

# Ensure it exists
assert os.path.exists(checkpoint_path), f"Checkpoint not found at: {checkpoint_path}"

# Load the model
model = ParametersClassifier.load_from_checkpoint(checkpoint_path)
model.eval()

sample_data = "/home/poundspb/Computer Vision/caxton_fork/data/full/"
assert os.path.isdir(sample_data), f"Image folder not found at: {sample_data}"


img_paths = [
    os.path.join(sample_data, img)
    for img in os.listdir(sample_data)
    if os.path.splitext(img)[1] == ".jpg"
]

print("********* CAXTON sample predictions *********")
print("Flow rate | Lateral speed | Z offset | Hotend")
print("*********************************************")

t1 = time.time()

for img_path in img_paths:
    pil_img = Image.open(img_path)
    x = preprocess(pil_img).unsqueeze(0)
    y_hats = model(x)
    y_hat0, y_hat1, y_hat2, y_hat3 = y_hats

    _, preds0 = torch.max(y_hat0, 1)
    _, preds1 = torch.max(y_hat1, 1)
    _, preds2 = torch.max(y_hat2, 1)
    _, preds3 = torch.max(y_hat3, 1)
    preds = torch.stack((preds0, preds1, preds2, preds3)).squeeze()

    preds_str = str(preds.numpy())
    img_basename = os.path.basename(img_path)
    print("Input:", img_basename, "->", "Prediction:", preds_str)

t2 = time.time()
print(f"Completed {len(img_paths)} predictions in {t2 - t1:.2f}s")