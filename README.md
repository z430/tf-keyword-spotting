<div align="center">
  <p>
    <a align="center" href="" target="_blank">
      <img
        width="100%"
        src="assets/logo.png"
      >
    </a>
  </p>

  <br>
  [![license](https://img.shields.io/github/license/z430/keyword-spotting.svg)](https://github.com/z430/keyword-spotting/blob/master/LICENSE)
</div>


## 👋 hello

**We write keyword spotting or wake up word to call your devices 🤝
## 💻 Install

- python >= 3.6
- Tensorflow 1.13
- Keras 2.2.4
  
or run `pip install -r requirement.txt`


## 📻 Dataset
Dataset is from google speech commands dataset which contains 30 keyword. 
Then, we select 6 commands to navigate the wheelchair.
They keyword are: `'backward', 'forward', 'go', 'left', 'right', 'stop'`

## 🚅 Training

To Train a new model:
1. Put the model inside `dnn_models.py`. don't forget to put respected input shape
2. Change the model selection, feature extraction method in `train.py` and `input_data.py`
3. train the model with `python train.py`
   
## 👋🏻 Testing

- Test single audio
  - put the audio path to `inference.py`
  - select the model you want, list available model is in `models`
  - run: `python inference.py`

- Test with live input
  - select the model
  - run `python inference_local.py`
