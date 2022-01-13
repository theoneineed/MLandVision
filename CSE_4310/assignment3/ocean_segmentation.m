function ocean_segmentation(filename)
%gives the different segments of ocean landscape
    gray = read_gray(filename);
    dx = [-0.5, 0, 0.5]; 
    dy = dx'; %The dy kernel is just the transpose of dx
    blurred_gray = blur_image(gray,1.3*1.3); %1.4*1.4
    dxb1gray = imfilter(blurred_gray, dx, 'symmetric');
    dyb1gray = imfilter(blurred_gray, dy, 'symmetric');
    %computing gradient norms
    grad_norms = (dxb1gray.^2 + dyb1gray.^2).^0.5;
    C = round(grad_norms/3);
    figure(4);imshow(C);
    sky_area = remove_holes(~C);
    figure(1); imshow(sky_area);
    row = size(C,1)/2;
    ocean_area = remove_holes_rc(~C, row, 1);
    figure(2); imshow(ocean_area);
end

