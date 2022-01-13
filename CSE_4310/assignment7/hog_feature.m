function result = hog_feature(image, top, left, block_size)

    gradient_dy = imfilter(image, [-1, 0, 1]');
    gradient_dx = imfilter(image, [-1, 0, 1]);
    cells_number = block_size/ 2;
    grad_orient = zeros(block_size, block_size);
    
    for i= top:(top+block_size)
        for j = left:(left+block_size)
            grad_orient(mod(i,top)+1,mod(j,left)+1) = atan2(double(gradient_dy(i,j)), double(gradient_dx(i,j)));
        end
    end
    grad_orient(grad_orient == 0) = grad_orient(grad_orient == 0)+1;
    v = grad_orient(:);
    v = v/norm(v);
    v(v>0.2) = 0.2;
    v = v / norm(v);
    
    result = v;
    
end

