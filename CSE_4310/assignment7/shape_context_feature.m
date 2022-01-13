function result = shape_context_feature(edge_image, row, col, r1)

    %The result should be a matrix with 5 rows and 12 columns, where result(i,j) corresponds to the region that 
    %is the intersection of the i-th ring (or the innermost disk, if i=1), and the j-th sector (j-th "pizza slice"),
    %using the same numbering convention that we used in the slides
    result = zeros(5,12);
    [non0rows,non0columns] = find(edge_image ~= 0);
    non0rows = non0rows - row;
    non0columns = non0columns - col;
    theta_rho_array = zeros(1, 2, size(non0rows,1));
    for i = 1: size(non0rows,1)
        theta_rho_array(:,:,i) = cart2pol(non0rows(i),non0columns(i)); %in the format of theta, rho
    end
    

    %For m = 2, 3, 4, 5, define radius r_m = 2 * r_{m-1}
    radius = zeros(6,1);
    radius(1) = 0;
    radius(2) = r1;
    for i = 3:6
        radius(i) = radius(i-1)*2;
    end

    angles = [0,30,60,90,120,150,180,210,240,270,300,330,360]*pi/180;
    for pixels = 1 : size(non0rows,1)
        for r = 2:6
            i = 2;
            for i = 2:13
                if(((radius(r-1)< theta_rho_array(:,2,pixels)) && (theta_rho_array(:,2,pixels) <= radius(r))) && ((angles(i-1)< theta_rho_array(:,1,pixels)) && (theta_rho_array(:,1,pixels) <= angles(i))))
                    result(r-1,i-1) = result(r-1,i-1)+1;
                end
            end
        end
    end
    result(result == 0) = result(result == 0)+1;
    
end










