function class_label = dtw_classifier_green(filename, start_frame, end_frame)

    %first we will get center points of each gestures in training file
    gt_train = load('./gesture_videos/start_end_frames_model_quan_ex3.txt');
    video_frames_train = read_video_frames('./gesture_videos/digits_model_quan_ex3.avi');
    
    video_frames_test = read_video_frames(filename);
    testght = ght_provided_video(video_frames_test, start_frame, end_frame);
    label_scores_ret = zeros(1,10);
    
    for labels = 1:10
        trainght = ght_provided_video(video_frames_train, gt_train(labels,2),gt_train(labels,3)); %gives trajectory for the given section of the video
        
        %Initialization
        scores = zeros(size(trainght,1),size(testght,1));
        scores(1,1) = cost(trainght(1,:),testght(1,:));
        
        for i = 2: size(trainght,1)
            scores(i,1) = scores(i-1,1) + cost(trainght(i,:),testght(1,:));
        end
        
        for j = 2 : size(testght,1)
            scores(1, j) = scores(1, j-1) + cost(trainght(1,:) , testght(j,:) );
        end
        
        %Main loop
        for i = 2: size(trainght,1)
            for j = 2: size(testght,1)
                scores(i, j) = cost(trainght(i,:),testght(j,:)) + min([scores(i-1, j), scores(i, j-1), scores(i-1, j-1)]);
            end
        end
        label_scores_ret(labels) = scores(size(trainght,1),size(testght,1));
                
    end
    
    [min_score, min_index] = min(label_scores_ret);
    
    class_label = min_index-1;
end

