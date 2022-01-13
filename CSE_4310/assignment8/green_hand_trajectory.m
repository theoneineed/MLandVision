function trajectory = green_hand_trajectory(filename, start_frame, end_frame)
    video_frames = read_video_frames(filename);
    no_rows = end_frame - start_frame + 1;
    hand_loc = zeros(no_rows,2);
    for i = start_frame : end_frame
        [scores, result, center] = green_hands(video_frames, i, [40,30]);
        hand_loc(i-start_frame+1,1) = center(:,2);
        hand_loc(i-start_frame+1,2) = center(:,1);
    end
    trajectory = hand_loc;    
end

