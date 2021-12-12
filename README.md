# Super-Resolution-Multi-Shot-Neural-Talking-Head-Synthesis

## Paper abstract
This paper proposes a low bandwidth talking-head video synthesis model Super Resolution Multi Shot Neural Talking Head Synthesis for video conferencing. Super Resolution Multi Shot Neural Talking Head Synthesis builds on the previous paper "One-Shot Free-View Neural Talking-Head Synthesis for Video Conferencing" (face-vid2vid). We decided to work on the Source Image. The main idea is to send through the internet multiple low resolution resized version of the source image and upscale it at the other end with a super resolution model from the paper "Enhanced Super-Resolution Generative Adversarial Networks" (ESRGAN). Our implementation managed to synthesize a talking head using less amount of data compared to our baseline models, without notable reduction of video quality. 

**This novel implementation was build on top of the implementation of:** https://github.com/zhanglonghao1992/One-Shot_Free-View_Neural_Talking_Head_Synthesis

To get the pre-trained weights used in this model: https://www.mediafire.com/folder/rw51an7tk7bh2/TalkingHead
