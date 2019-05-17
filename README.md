# README
Here I briefly describe how to run my scripts. In order for most of these to run, I expect the test_data.zip file to be unzipped in the same directory as the repo. 

## Required Task 2
The following command does the circular array with my tests. My driver tries to give a one line description of each test.
```
./circularArrayTest
```

## Required Task 3
I have the command below. If you don't specify the images, it looks in the current directory for the sample images provided. It also saves out images showing the intermediary steps I took. For more details, looks at the documentation I provide. The output of the script gives two values, an Intersection Over Union based on the difference in pixels from the colored image, and the IOU based on the difference in pixels when you grayscale the images. The second one is a better estimate. You can see the effect of this method if you look at the image comp_grayscale_sub1.png. The image consists of only the different points.
```
python image_comparer.py [img1] [img2]
```

## Bonus Task 1
The command to run this is below. The argument is optional. Without it the script will run the deps_test1.txt file in the repo. The correct result is described in the test file.
```
python build_order.py [deps_test1.txt]
```

## Bonus Task 2
The command to run this is below. I offer three ways to run it. The first way is the basic way that does the affine transform and combines the images in the test_data. The second modifies it to do the affine transform on the 3d data in the test_data. The third allows you to specify two arbitrary text files with points in them and find the affine transform between them.
```
python affine_transform.py
```
```
python affine_transform.py 3d
```
```
python affine_transform.py [correspondence?D_w0.txt] [correspondence?D_w1.txt]
```
