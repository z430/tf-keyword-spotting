from pathlib import Path

import torch
from loguru import logger

from kws.datasets.speech_commands import SpeechCommandsDataset
from kws.libs.dataloader import SpeechCommandsLoader
from kws.settings import CONFIG_SPEECHCOMMANDS_DATASET_PATH, CONFIG_SPEECHCOMMANDS_PATH

ROOT_DIR = Path(__file__).parent
DATASET_PATH = ROOT_DIR / "data" / "speech-commands"
torch.manual_seed(0)


def main():
    # directories
    # saved wieghts directory
    saved_weights_dir = ROOT_DIR / "saved_weights"
    saved_weights_dir.mkdir(exist_ok=True)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    dataset = SpeechCommandsDataset(
        CONFIG_SPEECHCOMMANDS_PATH, CONFIG_SPEECHCOMMANDS_DATASET_PATH
    )

    train_loader = SpeechCommandsLoader(dataset, device, mode="training")
    validation_loader = SpeechCommandsLoader(dataset, device, mode="validation")


if __name__ == "__main__":
    main()
