function [tp,fp,fn] = check_boxes(boxes,ground_truth,iou_thr)
    
    fn=0;%false negatives
    tp=0; %true positives
    fp=0;%false positives
    size_ground_truth = size(ground_truth, 1);
    size_boxes = size(boxes,1);
    %boxes is a matrix of size Nx6
    %check for true positives, false positives and false negatives
   
    %true and false positive first
    for index = 1:size_boxes
        counter = -1;
        B = boxes(index,:);
        for index2 = 1:size_ground_truth
            A = ground_truth(index2,:);
            IoverU = IntoverUni(A,B);
            if(IoverU >= iou_thr)
                counter=1; %we accept it as the true value
            end
        end 
        
        if(counter == 1)
            tp = tp+1; %if boxes were recognised to be true
        else
            fp = fp+1; %if boxes were not similar enough to be true
        end
    end
    
    %now, false negative
    for index = 1 : size_ground_truth %we directly compare the answer to truth from ground_truth
        A = ground_truth(index,:);
        counter = -1;
        for index3 = 1:size_boxes %checks for every box that is computed by code
           B = boxes(index3,:);
           IoverU = IntoverUni(A,B);
           if(IoverU >= iou_thr) %it recognised the face, so doesn't count as negative
              counter =1; 
           end
        end
        
        if(counter ~= 1) 
            fn = fn+1; %for those that were not same as true boxes, negative value goes up
        end
    end
   %Note: if there is zero box that code returns then in every iteration of
   %this for loop, there will be counter=-1 and that would count as false
   %negative
    
end
