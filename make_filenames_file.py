import os

"""
##### Input #######
upper_directory - Folder with collection of images and groundtruth depth images
image_file_path - Folder with sequence of images
depth_file_path - Folder with sequence of groundtruth depth images
output_txt - name of the txt file
카메라 focal length - 517.306408

##### Output ######
The txt file
It should be placed in /bts/train_test_inputs/
"""

upper_directory = 'freiburg1_floor/'
image_file_path = '/home/taeyoungkim/Desktop/Make_filenames_file/rgb'
depth_file_path = '/home/taeyoungkim/Desktop/Make_filenames_file/depth'
output_txt = 'TUM_floor_files_with_gt.txt'

focal = 517.306408

image_file_list = os.listdir(image_file_path)   # file path에 있는 파일들 list 불러오기
image_file_list.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

depth_file_list = os.listdir(depth_file_path)   # file path에 있는 파일들 list 불러오기
depth_file_list.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

print('Start!')

with open(output_txt, 'w') as f:
    for num in range(len(image_file_list)):
        f.write(upper_directory+image_file_list[num])
        f.write(' ')
        f.write(upper_directory+depth_file_list[num])
        f.write(' ')
        f.write(str(focal))
        f.write('\n')

print('Finished!')
