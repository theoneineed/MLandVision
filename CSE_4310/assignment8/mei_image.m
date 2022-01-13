function result = mei_image(filename, start_frame, end_frame)
%For every frame (except the first one and the last one):
%Compute the frame difference image for that frame.
%The motion energy image is the sum of all frame difference images.
    video_frames = read_video_frames(filename);
    mei_result = rgb2gray(video_frames(:,:,:,1)) * 0;
    for frames = (start_frame + 1) : end_frame
        framediff = rgb2gray(video_frames(:,:,:,frames)) - rgb2gray(video_frames(:,:,:,frames-1));
        mei_result = mei_result + framediff;
    end
    result = mei_result;
end

