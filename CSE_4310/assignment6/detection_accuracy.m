function [tp, fp, fn] = detection_accuracy(ground_truth_file, template, scales, ...
                                           detection_thr, iou_thr)

[filenames, numbers, gt_boxes] = read_ground_truth(ground_truth_file);
number = numel(filenames);
tp = 0;
fp = 0;
fn = 0;
number_of_boxes = 0;
number_of_gt_boxes = 0;

for n = 1:number
    disp(sprintf('processing image %d out of %d...', n, number));
    filename = filenames{n};
    pathname = sprintf('%s', filename);
    test_image = read_gray(pathname);
    [result, boxes] = template_detector(test_image, template, scales, detection_thr);
    number_of_boxes = number_of_boxes+ size(boxes,1);
    % shows the detected bounding boxes.
    figure(1); imshow(result);
    
    current_gt = gt_boxes{n};
    [current_tp, current_fp, current_fn] = check_boxes(boxes, current_gt, iou_thr);
    number_of_gt_boxes = number_of_gt_boxes+ size(current_gt,1);
    tp = tp + current_tp;
    fp = fp + current_fp;
    fn = fn + current_fn;
end

disp('done');
disp(sprintf('true positive: %d ,false positive: %d ,false negative: %d', tp, fp, fn));
no_boxes = ['number of boxes: ',num2str(number_of_boxes),' = true positive + false positive'];
no_gt_boxes = ['number of faces: ', num2str(number_of_gt_boxes), ' = true positive + false negative'];
disp(no_boxes)
disp(no_gt_boxes)

