# BTS-make-txt

### This repository helps you to make `files_with_gt.txt` in [BTS](https://github.com/cogaplex-bts/bts).  

First, when you make your own dataset, you should know your focal length.  
Second, you have to change the name of RGB images & Depth images.  
Referring to BTS, they make their image names with their own rules.  

For example, NYU_depth_v2 has many sequence of image.  
Their names have a rule like...  
```
rgb_00045.jpg
rgb_00046.jpg
rgb_00047.jpg
rgb_00048.jpg
rgb_00049.jpg
sync_depth_00045.jpg
sync_depth_00046.jpg
sync_depth_00047.jpg
sync_depth_00048.jpg
sync_depth_00049.jpg
```  

You must follow this rule to make your own dataset.  

When you make this sequence, then you could use my repositroy.  
