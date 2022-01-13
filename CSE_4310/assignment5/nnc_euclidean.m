function class_label = nnc_euclidean(test_image)
%recognizes the digit shown in test_image using nearest neighbor classification 
%under the Euclidean distance
    dist_holder = zeros(1,150);
    index_dist=0;
    for label = 0:9
       for training = 1:15
           index_dist = index_dist+1;
           filename_train = strcat('./digits_training/label',int2str(label),'_training',int2str(training),'.png');
           train_image = imread(filename_train);
           dist_holder(index_dist) = euclidean_distance(test_image,train_image);
       end
    end
    [M,I] = min(dist_holder);
    if(mod(I,15) == 0)
       class_label = fix(I/15)-1;
    else
        class_label = fix(I/15);
    end
end

