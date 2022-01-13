function [top, bottom, left, right] = find_bounding_box(pathname1)
    %draws a yellow box around a person%
    [sequence_name, frame] = parse_frame_name(pathname1);
    pathname0 = make_frame_name(sequence_name, frame+4);
    pathname2 = make_frame_name(sequence_name, frame-6);
    frame1 = read_gray(pathname0);
    frame2 = read_gray(pathname1);
    frame3 = read_gray(pathname2);
    original = imread(pathname1,'tif');
    diff1 = abs(frame2-frame1);
    diff2 = abs(frame3-frame2);
    motion = min(diff1,diff2);
    threshold = 12;
    thresholded = (motion > threshold);
    [labels, number] = bwlabel(thresholded, 8);
    counters = zeros(1,number);
    for i = 1:number
    % first, find all pixels having that label.
        component_image = (labels == i);
    % second, sum up all white pixels in component_image
        counters(i) = sum(component_image(:));
    end
    [area, id] = max(counters);
    person = (labels == id);
    imshow(person,[ ]);
    imwrite(person, 'personBW.jpg','jpg');
    
    % find coordinates of all non-zero pixels.
    [rows, cols] = find(person);
    top = min(rows);
    bottom = max(rows);
    left = min(cols);
    right = max(cols);
    border_img = draw_rectangle(original, [255,255,0], top, bottom, left, right);
    imwrite(border_img,'yellow_border.jpg','jpg');
    imshow(border_img);
end

