# ECCV2022



## Description



## Approach Ovewview
![](https://github.com/anonymousGithub2022/1/blob/main/fig/0001.jpg)

Our approach overview is shown in the above figure, for the detail design, please refer to our papers.


## File Structure
* **src** -main source codes.
  * **./src/model** -the model architecture of the NICG models.
  * **./src/attack** -the implementation of proposd attack algorithm.
* **train.py** -the script to train the NICG models.
* **generate_adv.py** -this script generate the adversarial examples.
* **test_latency.py** -this script measure the latency of the generated adversarial examples.
* **gpu4.sh** -bash script to generate adversarial examples and measure the efficiency.


## How to run
We provide the bash script that generate adversarial examples and measure the efficiency in **gpu4.sh**. **gpu5.sh**, **gpu6.sh**,**gpu7.sh** are implementing the similar functionality but for different gpus. 

 So just run `bash gpu4.sh`


## Results
![](https://github.com/anonymousGithub2022/1/blob/main/fig/res.jpg)
The above figure shows the *efficiency* distribution of the benign images and the adversarial images. The ares under the cumulative distribution function (CDF) represent the victim NICG models' efficiency. A large area implies the model is less efficiency.








