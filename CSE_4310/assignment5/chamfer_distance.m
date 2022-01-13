function distance = chamfer_distance(image1, image2)
%returns the chamfer distance of those two images
    %You should return the symmetric chamfer distance, which is the sum of the two directed chamfer distance
    im1_binary = (image1 ~= 0);
    im2_binary = (image2 ~= 0);
    n1 = sum(im1_binary(:));
    dt2 = bwdist(im2_binary);
    chamfer_im1_to_im2 = sum(sum(im1_binary .* dt2)) / n1;
    
    n2 = sum(im2_binary(:));
    dt1 = bwdist(im1_binary);
    chamfer_im2_to_im1 = sum(sum(im2_binary .* dt1)) / n2;
    symmetric_chamfer_distance = chamfer_im1_to_im2 + chamfer_im2_to_im1;
    distance = symmetric_chamfer_distance;
end

