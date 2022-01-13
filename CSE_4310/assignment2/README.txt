Nabin Chapagain, 1001551151

Task 2:

For task 2, I used the threshold technique and it seems to work pretty well. I have added a feature in the code which shows the outline of the person in the frame that is given to us through the argument. It works very well with the frames that are in walkstraight folder. I checked with frame 90, 35, 45, 120 and 109; all of them seem to be working properly.

The way I solve this problem is find a difference in n+1 and nth slide and n-1 and nth slide, find a common value between them to get whatever is minimum changed in nth slide then I use threshold value to get rid of some noise. Later, I compute the sum of matrix elements in the common file and see if the sum of elements is above a certain threshold value. If yes, that means there is considerable amount of white elements in there which means, there is a person. If not, I say, there is no person.

Task 3:

The approach I took for task 3 was I used "bound_box_noimage.m" which gave top, bottom, right and left values for each file that is passed when the function is called. Then, for frame1 and frame2, I call this function and compute center of each frames as (top1+bottom1)/2 (i.e; row of center) and (left1+right1)/2 (i.e; column of center). I did same with frame2. Using "parse_frame_name.m" to get the frame numbers for frame1 and frame2. I then calculated the difference of frame numbers of frame2 and frame1 which gives us the number of frames. I calculated the difference of centers of frames and divided it by number of frames which gives us the velocity of the person.

As it can be seen from the calculation, the average velocity can be an integer or a decimal. Since it is an average, the velocity is not always an integer although velocity has units of pixels per frame. Since matlab works with matrix and matrix indices increase as we go right and down, negative row_speed means the object (or, at least the center of the object) is moving upwards and negative column_speed means the object is going towards left. 


















