<h1>Setup</h1>
To begin setup.<br><br>

1. I forked the original Caxton repo:<br>
<a href="https://github.com/cam-cambridge/caxton">https://github.com/cam-cambridge/caxton</a><br><br>

2. I cloned my "Caxton_Fork" to `gebru` using:<br>
<code>git clone git@github.com:philip-hub/caxton_fork.git</code><br><br>

3. I created a virtual environment:<br>
<code>python3 -m venv env</code><br>
I then activated my environment:<br>
<code>source env/bin/activate</code><br><br>

4. I ran the command to install requirements:<br>
<code>pip install requirements.txt</code><br>
This at first did not work and I had to edit the `requirements.txt`. I removed <code>dataclasses==0.8</code> as this is no longer needed for Python 3.7 and higher. I opened a pull request back to the original Caxton repo since this was the only change needed for training to run.<br><br>

<h1>Data</h1><br>

5. I downloaded the data from <a href="https://www.repository.cam.ac.uk/items/6d77cd6d-8569-4bf4-9d5f-311ad2a49ac8">this dataset page</a>. Specifically, I downloaded <a href="https://www.repository.cam.ac.uk/bitstreams/54554b08-6ac5-495f-8d51-9c614d6839f7/download">caxton_dataset_filtered.csv</a>. I also consulted with Dr. Wilson and downloaded <a href="https://www.repository.cam.ac.uk/bitstreams/ec724f7c-14e3-464d-b031-372cd2765a03/download">print0.zip</a>, which I unzipped. I decided to train the model using only these images.<br><br>

6. To train only with print0, I ran a script that drops entries not associated with the print0 dataset. This script is in <a href="https://github.com/philip-hub/caxton_fork/blob/main/extras/main.py">extras/main.py</a>. Make sure that the print0 images are placed in the appropriate path. See the README in the extras folder for more details.<br><br>

7. I moved the `print0` folder to <code>data/caxton</code> and placed the outputted <code>caxton_data_filtered.csv</code> into the <code>data/</code> directory.<br><br>

8. Final training step: start the training (ensure your virtual environment is activated):<br>
<code>python src/train.py</code><br>
This successfully trained my model!<br><br>

<h1>Testing</h1>

9. To run the test file, locate your checkpoint file after training. Mine was:<br>
<code>src/checkpoints/21052025/1234/MHResAttNet-dataset_full-21052025-epoch=09-val_loss=37.10-val_acc=0.46.ckpt</code><br><br>

Use Vim or a Visual Studio SSH client to open and edit `test.py`. On line 19, set the path:<br>
<code>checkpoint_path = "/home/poundspb/Computer Vision/caxton_fork/src/checkpoints/21052025/1234/MHResAttNet-dataset_full-21052025-epoch=09-val_loss=37.10-val_acc=0.46.ckpt"</code><br><br>

10. Run test.py:<br>
<code>python src/test.py</code><br>
This will show you the test accurcy and loss.

<h1>Running with real world samples</h1>

9. To run the sample file, locate your test image path. Upload your images to the path. Mine was:<br>
<code>/home/poundspb/Computer Vision/caxton_fork/data/full/</code><br><br>

Use Vim or a Visual Studio SSH client to open and edit `test.py`. On line 20, set the path you located in step 9:<br>
<code>checkpoint_path = "/home/poundspb/Computer Vision/caxton_fork/src/checkpoints/21052025/1234/MHResAttNet-dataset_full-21052025-epoch=09-val_loss=37.10-val_acc=0.46.ckpt"</code> And then on line 29 change to your image path

<code>sample_data = "/home/poundspb/Computer Vision/caxton_fork/data/full/"</code>

Run samples.py
<code>python src/samples.py</code><br>

*Note I had to make a few changes to samples.py for it to work. 
* Other note I used chatgpt on this project
<br><br>

