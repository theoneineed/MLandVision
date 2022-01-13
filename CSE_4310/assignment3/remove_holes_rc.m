function reversed_bg = remove_holes_rc(my_image,row,column)
%This function takes in a binary image and fills the holes in them
    A = my_image;
    if(A(row,column) == 0)
        C = ~A;
    else
        C = A;
    end
    %need to account for both white and black background  
    [labels, number] = bwlabel(C, 4);
    %using row = column = 1 says background is the pixel that is first
    background = labels(row, column);
    background = (labels == background);
    if(A(1,1) == 0)
        reversed_bg = ~background;   
    else
        reversed_bg = background;  
    end
end

