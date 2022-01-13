function [accuracy, confusion_matrix] = nnc_chamfer_stats()
%measures the classification accuracy of nearest neighbor classification using the chamfer distance
    accuracy_int = 0;
    confusion_matrix= zeros(10,10);
    for label = 0:9
       for test = 1:10
           filename_test = strcat('./digits_test/label',int2str(label),'_test',int2str(test),'.png');
           test_image = imread(filename_test);
           class_label = nnc_chamfer(test_image);
           label_index = label;
           class_label_index =  class_label;
           
           if (class_label == label)
               accuracy_int = accuracy_int+1;
           end
           
           if(label == 0)
              label_index = 10;
           end
           
           if(class_label == 0)
               class_label_index = 10;
           end
           
           confusion_matrix(label_index, class_label_index) = confusion_matrix(label_index, class_label_index) + 1;
        end
       
    end
    accuracy = accuracy_int/100;
    confusion_matrix = confusion_matrix/10;

end

