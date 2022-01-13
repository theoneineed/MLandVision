function gray_hand = read_gray(pathname)
    %converts colored image into grayscale image%
    image_read = imread(pathname,'tif');
    double_image_read = double(image_read);
    gray_hand = (double_image_read(:,:,1) + double_image_read(:,:,2) + double_image_read(:,:,3)) / 3;
end