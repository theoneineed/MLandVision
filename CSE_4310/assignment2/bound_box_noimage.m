function [top, bottom, left, right] = bound_box_noimage(pathname1)
    %This is the find_bounding_box function but it does not draw the rectangle%
    [sequence_name, frame] = parse_frame_name(pathname1);
    pathname0 = make_frame_name(sequence_name, frame+5);
    pathname2 = make_frame_name(sequence_name, frame-5);
    frame1 = read_gray(pathname0);
    frame2 = read_gray(pathname1);
    frame3 = read_gray(pathname2);
    original = imread(pathname1,'tif');
    %frame61 = imread('walkstraight/frame0047.tif');
    %frame62 = imread('walkstraight/frame0062.tif');
    %frame63 = imread('walkstraight/frame0077.tif');
    
    diff1 = abs(frame2-frame1);
    %imshow(diff1)
    diff2 = abs(frame3-frame2);
    %imshow(diff2)
    motion = min(diff1,diff2);
    %imshow(motion)
    threshold = 10;
    thresholded = (motion > threshold);
    %imshow(thresholded, []);
    [labels, number] = bwlabel(thresholded, 8);
    %imshow(labels,[ ]);
    %disp(number)
    %disp(' is number of connected component')
    %colored = label2rgb(labels, @spring, 'c', 'shuffle');
    %figure(2); imshow(colored);
    counters = zeros(1,number);
    for i = 1:number
    % first, find all pixels having that label.
        component_image = (labels == i);
    % second, sum up all white pixels in component_image
        counters(i) = sum(component_image(:));
    end
    [area, id] = max(counters);
    person = (labels == id);
    %imshow(person,[ ]);
    imwrite(person, 'personBW.jpg','jpg');
    
    % find coordinates of all non-zero pixels.
    [rows cols] = find(person);
    top = min(rows);
    bottom = max(rows);
    left = min(cols);
    right = max(cols);
end