# Video-Object-Segmentation Aggregation

The project is based on following paper: [link](https://opus.lib.uts.edu.au/bitstream/10453/54467/4/2016icme_submission.pdf)

The paper Build a Aggregation Model based on the 7 other Video Object Segmentation models.
Initially the algorithms implements a majority voting based on segmentation models Mentioned below 

1. Key-segments 
2. Fast object segmentation 
3. Seamseg
4. DagSeg
5. JotSeg
6. Saliency Seg
 and  a Baseline Model is created based on Majority Voting

A Proposed method is then applied on Baseline Model. Which gives Object Semgented Model better than the Models described Above.
The visualization of algorithm model can be understood from PA5_b.ipynb.

Reference:

[1] Jae Lee Yong, Jaechul Kim, and Kristen Grauman,“Key-segments for video object segmentation,” in ICCV, 2011.

[2] Anestis Papazoglou and V. Ferrari, “Fast object segmentation in unconstrained video,” in ICCV, 2013.

[3] S. Avinash Ramakanth and R. Venkatesh Babu, “Seamseg: Video object segmentation using patch seams,” in CVPR, 2014.

[4] Dong Zhang, O. Javed, and M. Shah, “Video object segmentation through spatially accurate and temporally
    dense extraction of primary object regions,” in CVPR, 2013
    
[5] Longyin Wen, Dawei Du, Zhen Lei, Stan Z. Li, and Ming-Hsuan Yang, “Jots: Joint online tracking and segmentation,” in 
    CVPR, June 2015
    
[6] Wenguan Wang, Jianbing Shen, and Fatih Porikli, “Saliency-aware geodesic video object segmentation,” in CVPR, 2015
