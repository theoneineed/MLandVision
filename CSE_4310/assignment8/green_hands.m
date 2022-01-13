function [scores, result, center] = ...
    green_hands(video_frames, frame, hand_size)

% [scores, result, center] = green_hands(video_frames, frame, hand_size)
%
% hand_size = [rows, cols] is a 1x2 matrix specifying the size of the
% bounding box of the hand. The detection will only consider that scale.
%
% detects one hand in an image, assuming that the hand is wearing a 
% green glove.
% - scores is a 2D image of detection scores.
% - result is a color image, showing the detected bounding box drawn on top
% of the original frame.
% - center = [row, col] is a 1x2 matrix containing the center of the detected
% bounding box.


current = double(video_frames(:,:,:,frame));
green_scores = 2 * current(:, :, 2) - current(:, :, 1) - current(:, :, 3);
%green_scores = (current(:, :, 2) > current(:, :, 1)) & (current(:, :, 2) > current(:, :, 3));

previous = video_frames(:,:,:, frame-1);
previous_gray = double_gray(previous);
current_gray = double_gray(current);
next = video_frames(:,:,:, frame+1);
next_gray = double_gray(next);

frame_diff = min(abs(current_gray-previous_gray), abs(current_gray-next_gray));
green_motion_scores = green_scores .* frame_diff;

scores = imfilter(green_motion_scores, ones(hand_size), 'same', 'symmetric');
[result, center] = top_detection_results(current, scores, hand_size, ...
                                          1, 1);


