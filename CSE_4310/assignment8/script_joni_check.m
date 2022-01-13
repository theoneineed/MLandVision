gt_test = load('./gesture_videos/start_end_frames_model_joni_ex3.txt');
filename = './gesture_videos/digits_model_joni_ex3.avi';
labels_mei = zeros(1,10);
labels_ght = zeros(1,10);
for i = 1:10
    labels_mei(i) = mei_classifier(filename, gt_test(i,2), gt_test(i,3));
    labels_ght(i) = dtw_classifier_green(filename, gt_test(i,2), gt_test(i,3));
end
disp('labels_mei')
disp(labels_mei)
disp('labels_ght')
disp(labels_ght)
disp('ground truth')
disp(0:9)

%  7     1     7     9     4     2     7     7     3     7 for euclidean
%  9     1     2     2     4     3     2     7     8     2 for L1

%after blurring

%  7     1     7     9     4     2     9     7     3     9 for euclidean
%  9     1     2     2     4     3     2     7     8     6 for L1