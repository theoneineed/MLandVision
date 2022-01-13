function soccer_analysis(filename)
%Analyzes the image of a soccer game given
    color = double (imread(filename));
    r = color(:,:,1);
    g = color(:,:,2);
    b = color(:,:,3);
    
    %identify red areas:
    red = ((r - g > 25) & (r - b > 35));
    kernel = ones(5,5)/35;
    red = imfilter(red,kernel);
    %identify green areas:
    green = ((g - r > 35) & (g - b > 15));
    green = imdilate(green, ones(5,5));
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    green2 = ((g - r > 25)&(g - b > 30));
    green2 = remove_holes(green2);
    green2 = imfilter(green2, kernel);
    %identify blue areas:
    blue = ((b - r > 35) & (b - g > 30));
    blue = imdilate(blue, ones(1,1));
    
    green = imrotate(green,180);
    field = remove_holes(green);
    field = imrotate(field,180);
    
    field = remove_holes(field);
    red_players = (green2 & red);
    blue_players = (green2 & blue);
    
    figure(1); imshow(field);
    figure(2); imshow(red_players);
    figure(3); imshow(blue_players);
end

