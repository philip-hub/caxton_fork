import os
import argparse
import pytorch_lightning as pl
from data.data_module import ParametersDataModule
from model.network_module import ParametersClassifier
from train_config import *

parser = argparse.ArgumentParser()

parser.add_argument(
    "-s", "--seed", default=1234, type=int, help="Set seed for training"
)

args = parser.parse_args()
seed = args.seed

set_seed(seed)

checkpoint_path = "/home/poundspb/Computer Vision/caxton_fork/src/checkpoints/21052025/1234/MHResAttNet-dataset_full-21052025-epoch=09-val_loss=37.10-val_acc=0.46.ckpt"

# Load the model from the checkpoint
model = ParametersClassifier.load_from_checkpoint(checkpoint_path)
model.eval()

data = ParametersDataModule(
    batch_size=BATCH_SIZE,
    data_dir=DATA_DIR,
    csv_file=DATA_CSV,
    image_dim=(320, 320),
    dataset_name=DATASET_NAME,
    mean=DATASET_MEAN,
    std=DATASET_STD,
    transform=False,
)
data.setup('test')

trainer = pl.Trainer(
    num_nodes=1,
    gpus=1,
    weights_summary=None,
    precision=16,
)

trainer.test(model, datamodule=data)
