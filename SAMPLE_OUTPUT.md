Testing output
<code>

(env) poundspb@gebru:~/Computer Vision/caxton_fork/src$ python test.py
Global seed set to 1234
GPU available: True, used: True
TPU available: None, using: 0 TPU cores
LOCAL_RANK: 0 - CUDA_VISIBLE_DEVICES: [0,1,2,3,4,5,6,7]
Using native 16bit precision.
Testing: 0it [00:00, ?it/s]/home/poundspb/Computer Vision/caxton_fork/env/lib/python3.9/site-packages/pytorch_lightning/core/step_result.py:145: UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
  value = torch.tensor(value, device=device, dtype=torch.float)
Testing: 100%|██████████████████████████████████████████████████████████| 9/9 [00:01<00:00,  5.32it/s]
--------------------------------------------------------------------------------
DATALOADER:0 TEST RESULTS
{'test_acc': tensor(0.5448, device='cuda:0'),
 'test_acc_epoch': tensor(0.5448, device='cuda:0'),
 'test_loss': tensor(3.7239, device='cuda:0'),
 'test_loss0': tensor(0.9406, device='cuda:0'),
 'test_loss1': tensor(0.9644, device='cuda:0'),
 'test_loss2': tensor(0.8445, device='cuda:0'),
 'test_loss3': tensor(0.9130, device='cuda:0'),
 'test_loss_epoch': tensor(3.6625, device='cuda:0')}
</code>

Sample Output

<code>

(env) poundspb@gebru:~/Computer Vision/caxton_fork/src$ python samples.py
********* CAXTON sample predictions *********
Flow rate | Lateral speed | Z offset | Hotend
*********************************************
Input: IMG_3438.jpg -> Prediction: [0 0 2 2]
Input: IMG_3436.jpg -> Prediction: [0 0 2 2]
Input: sample0021.jpg -> Prediction: [0 0 2 2]
Input: sample1221.jpg -> Prediction: [0 0 2 2]
Input: sample1111.jpg -> Prediction: [0 0 2 2]
Input: IMG_3437.jpg -> Prediction: [0 0 2 2]
Input: sample1011.jpg -> Prediction: [0 0 2 2]
Input: sample2120.jpg -> Prediction: [0 0 2 2]
Input: sample0022.jpg -> Prediction: [0 0 2 2]
Input: sample2122.jpg -> Prediction: [0 0 2 2]
Input: sample2011.jpg -> Prediction: [0 0 2 2]
Completed 11 predictions in 1.84s

</code>
