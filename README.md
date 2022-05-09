# Computational_photography_final_project -- Photo Mosaics

1.Introduction
1) image dataset

I created a dataset where all the images are of Kobe Bryant.So I wrote a scrapy program to get all the images they had of Kobe Bryant.The website is https://www.gettyimages.com. And download all the images which are relevant to Kobe Bryant. Just like that

<img width="955" alt="image" src="https://user-images.githubusercontent.com/34802668/165138880-6279377d-63fc-4c33-95b9-4488c140b3cf.png">

And here we are, the Kobe-Bryant dataset are all set!The link of this dataset:
https://drive.google.com/file/d/188WvOJIYxa49OwJDMKoqDt34bmJ39m4P/view?usp=sharing

original image is:

![Kb](https://user-images.githubusercontent.com/34802668/165155882-96febd8c-60ea-449d-8017-2609760cff9a.png)


2) Photo Mosaics

a) Method I (k-d tree):
First I tried to use k-d tree to query the fittest image from our dataset to stick to the image block,so I check how to use k-d tree, here is the reference:

https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.html

First, I collect average color for the output image and the images in the database, then use k-d tree to query it, but then I found that first, when I just query them, this happened

<img width="955" alt="image" src="https://user-images.githubusercontent.com/34802668/165153503-febdc530-327f-45b5-b2f8-eafaa07e5b4d.png">

Then I found that in the calculation of dominant color, there exists one expansion only contains white elements, so just cut this dimension. 
After that, I found that those images I got from my scrapy codes are various in format, so that when I tried to query those images, I found some dimension errors, so in the begining of my codes, I transformed those images into 'RGB' format, that's the normolization part.
Next thing I do is to adjust the image, about the size and other things. For example, some pre-treatment are needed, like erase the noise etc.. 

b) Method II(Using distance):
First I need to adjust the image, since I have done lots of work in method I, I may not need to adjust a lot in color, but in size. This time, I would not resize all the photo to a certain scale, instead, by using aspect ratio for each image in my dataset. I just chose the image which has similar ratio to our grid size, so that it could fit better! After I did the method I, I have found that the key is to find the closest color to a specific grid zone in the output image, so what I need to do is to first, get the size of the output image and the grid size, second, for each grid, calculate the average color for this grid. After i get those information, all I need to do is to find the closest one from my dataset, just traverse the dataset once to find that. When I finished all the process, just need to put those selected images into those grids one by one, then it could be done !
here is the main function:

<img width="586" alt="image" src="https://user-images.githubusercontent.com/34802668/166501333-8db9a5a5-02b2-44a7-82aa-9327f54a782d.png">

Then I have found that the output image I found has a large black area(not pure black, but has some color in it), so that when I handle those areas, it has a large possibility that it will use the same image. So first, for those black images, I created a few filters to make them slight lighter or darker, and then apply them randomly. Next, in case that the situation still happens, I have created a list where if some images use more than certain specific times, the function will query the next closest one.

3）Output image

Method I:

![output](https://user-images.githubusercontent.com/34802668/165147080-7ea87558-d399-408b-b7ff-bf3fb159366d.jpeg)

Method II:

![output1](https://user-images.githubusercontent.com/34802668/165155690-361ee7c6-f497-47f7-b87e-afecf37bbbe4.jpg)

After finishing those, I found two problems, first, the background image has so many consistent color, like a big area of black or yellow, second, when I zoom in, I cannot see the images so clearly in each grid, and the last is that it may use one image so many times. 

So in order to solve these, first I find a new image which has rich color in it:

![t1](https://user-images.githubusercontent.com/34802668/167281153-cdc822b4-07b6-490b-b279-b68f16d9de6b.jpg)

and enrich my dataset by crawling more images.

Next, I create a function which use some packages in PIL.Image, to create a high resolution image, here is the function

<img width="984" alt="image" src="https://user-images.githubusercontent.com/34802668/167318705-b61e07f4-b69e-4150-8a4b-1eb13fa98e12.png">


after that, a new problem occurs, that is the limitation of max pixels, so I just change this limitation by this:

<img width="586" alt="image" src="https://user-images.githubusercontent.com/34802668/167281238-51047fe4-fe5c-47bd-a162-f664872eee1b.png">

and next when I set the grid to be (40, 40), it turns out to be like this:

![output_three](https://user-images.githubusercontent.com/34802668/167281258-102adf26-64be-4a95-bfb9-7739f65fc567.jpg)

I cannot see the background image so clearly, so I just changed the size of the grid

![output_two](https://user-images.githubusercontent.com/34802668/167281278-74204cab-7b02-4654-9291-deaa7e9d5308.jpg)

but I find out that I used one image so many times, so I just changed my query function of searching the kd-tree by adding k into it, and create a list where it doesn't allow to use the same picture within a certain distance.

Finally, in order to see the image in each grid clearly, I used the resize function in our dataset.

After all those preparations are set, just run the program, it turns out to be like that

![output_three](https://user-images.githubusercontent.com/34802668/167303945-6a083a86-eaa8-475b-a20c-75c37b002a31.jpg)

Note: I just find that the gettyimage might have some way to prevent big-scale crawling so that the resolution of images scale down.And it has a threhold when I want to increase the resolution.

Other work:

original:

![1720866](https://user-images.githubusercontent.com/34802668/167329736-f3ac9054-e6f6-4167-ac5c-d8b4de688718.jpg)

Mosaics:

image_name:



I searched for lots of ways and implentment on my own

