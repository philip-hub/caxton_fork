<h1>Setup</h1>
    To begin setup.<br>
    <br> 
    1.  I forked the orignal Caxton repo:
    <br>
    <a href="https://github.com/cam-cambridge/caxton">`https://github.com/cam-cambridge/caxton`</a>
    2. I cloned the my "Caxton_Fork" to gebru using<br>
    `git clone git@github.com:philip-hub/caxton_fork.git`<br><br>
    3. I created a virtual enviorment: <br>
    `python3 -m venv env`<br>
    I then activated my enviorment:<br>
    `source env/bin/activate`<br><br>
    4. I ran the command pip install -r requirements.txt <br>
    `pip install requirements.txt`<br>
    This at first did not work and I had to edit the requirements.txt. All I had to do was delete `dataclasses==0.8` from the requirements.txt file as this is no longer needed for Python 3.7 and higher. I opened a pull request back to the orginal Caxton repo as this was the only change I had to make for the training to run.<br><br>
    <h1>Data</h1><br>
    5. I needed to download the data from <a href ="https://www.repository.cam.ac.uk/items/6d77cd6d-8569-4bf4-9d5f-311ad2a49ac8">`https://www.repository.cam.ac.uk/items/6d77cd6d-8569-4bf4-9d5f-311ad2a49ac8`</a> I downloaded the <a href ="https://www.repository.cam.ac.uk/bitstreams/54554b08-6ac5-495f-8d51-9c614d6839f7/download">caxton_dataset_filtered.csv</a> from the dataset repo. I consulted with Dr. Wilson. Then I decided to download <a href="https://www.repository.cam.ac.uk/bitstreams/ec724f7c-14e3-464d-b031-372cd2765a03/download">print0.zip</a> and unziped it. I decided to train the model only with these pictures.<br> <br>
    6. To only train with print0, I had to run a simple script to drop every set of photos that was not in my print0 dataset. This script is in the <a href ="https://github.com/philip-hub/caxton_fork/blob/main/extras/main.py">`extras/main.py`</a>. Note that the print0 images must be in the appropiate path. There is another readme in the extras with more details if needed.</a><br><br>
    7. Then I moved the print0 folder to `data/caxton` and the outputed `caxton_data_filtered.csv` to `data/`<br><br>
    8.Last step in training is to start the start the training (make sure the virtual enviorment is activated).<br>
    `python src/train.py`
    This successfully trained my model!<br><br>

<h1>Testing</h1>

 9. To run the test file simply navigate to your checkpoint file and copy the aboslute file directory after training. For me it was: `src/checkpoints/21052025/1234/MHResAttNet-dataset_full-21052025-epoch=09-val_loss=37.10-val_acc=0.46.ckpt`
    <br>Use VIM or Visual Studio SSH client to open and edit test.py. On line 19 `checkpoint_path =` paste the path in as a string. <br><br>
    `checkpoint_path = "/home/poundspb/Computer Vision/caxton_fork/src/checkpoints/21052025/1234/MHResAttNet-dataset_full-21052025-epoch=09-val_loss=37.10-val_acc=0.46.ckpt"`<br><br>
    10. Run test.py `python src/test.py`


