function result = person_present(pathname1)
%This function tells us if person is visible in image or not
    [sequence_name, frame] = parse_frame_name(pathname1);
    pathname0 = make_frame_name(sequence_name, frame+1);
    pathname2 = make_frame_name(sequence_name, frame-1);
    frame1 = read_gray(pathname0);
    frame2 = read_gray(pathname1);
    frame3 = read_gray(pathname2);
    original = imread(pathname1,'tif');
    diff1 = abs(frame2-frame1);
    %imshow(diff1)
    diff2 = abs(frame3-frame2);
    %imshow(diff2)
    motion = min(diff1,diff2);
    threshold = 25;
    thresholded = (motion > threshold);
    %imshow(thresholded, []);
    if(sum(thresholded,'all')<15)
        disp("0") %0 means we cannot see the person%
    else
        disp("1") %1 means we can see the person%
    end
    %imshow(original)
end

