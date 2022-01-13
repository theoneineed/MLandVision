function result = mei_provided_video(video_frames, start_frame, end_frame)
%For every frame (except the first one and the last one):
%Compute the frame difference image for that frame.
%The motion energy image is the sum of all frame difference images.
    first_frame = video_frames(:,:,:,1);
    frame_size = (first_frame(:,:,1)+first_frame(:,:,2)+first_frame(:,:,3))/3;
    mei_result = zeros(size(frame_size));

    for frames = (start_frame + 1) : end_frame
        framediff = video_frames(:,:,:,frames) - video_frames(:,:,:,frames-1);
        framediff_double = double(framediff);
        framediff2d = (framediff_double(:,:,1) + framediff_double(:,:,2) + framediff_double(:,:,3)) / 3; 
        framediff2d = blur_image(framediff2d, 1);
        mei_result = mei_result + framediff2d;
    end
    result = mei_result;
end

