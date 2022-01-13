function [row_speed, col_speed] = person_speed(pathname1,pathname2)
    [top1, bottom1, left1, right1] = bound_box_noimage(pathname1);
    [top2, bottom2, left2, right2] = bound_box_noimage(pathname2);
    [sequence_name1, frame1] = parse_frame_name(pathname1);
    [sequence_name2, frame2] = parse_frame_name(pathname2);
    no_frames = abs(frame2-frame1); %number of frames is scalar and should be same 62-50 and 50-62%
    center1 = [(top1+bottom1)/2,(left1+right1)/2];
    center2 = [(top2+bottom2)/2,(left2+right2)/2];
    % You can assume that the first argument refers to an earlier frame in the sequence compared to the second argument.%
    velocity_total=((center2 - center1)./no_frames);
    row_speed = velocity_total(1);
    col_speed = velocity_total(2);
    %"Since matlab works with matrix and matrix indices increase as we go right and down, negative row_speed means the object is moving upwards and negative column_speed means the object is going towards left.
    disp([row_speed, col_speed])
    
end

