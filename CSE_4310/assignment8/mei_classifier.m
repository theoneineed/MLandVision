function class_label = mei_classifier(filename, start_frame, end_frame)
    %quan_model should be the training file
    gt_train = load('./gesture_videos/start_end_frames_model_quan_ex3.txt');
    video_frames_train = read_video_frames('./gesture_videos/digits_model_quan_ex3.avi');
    frame_size = size(rgb2gray(video_frames_train(:,:,:,1)));
    labels_mei_train = zeros(frame_size(1),frame_size(2),10);
    for i = 1:10
        if(i==10)
            labels_mei_train(:,:,i) = mei_provided_video(video_frames_train, gt_train(1,2), gt_train(1,3));
        else
            labels_mei_train(:,:,i) = mei_provided_video(video_frames_train, gt_train(i+1,2), gt_train(i+1,3));
        end
    end
    %training MEI are ready now we move on to test objects
    
    
    video_frames_test = read_video_frames(filename);
    mei_test = mei_provided_video(video_frames_test, start_frame, end_frame);
    mei_test = blur_image(mei_test, 0.5);
    distance = zeros(1,10);
    for i = 1:10
        distance(i) = L1_distance(labels_mei_train(:,:,i), mei_test);
    end
    [min_dist, index] = min(distance);
    class_label = index;
    if(index == 10)
        class_label = 0;
    end    
    %figure(1)
    %imshow(labels_mei_train(:,:,index),[]);
    %figure(2)
    %imshow(mei_test,[]);

end

