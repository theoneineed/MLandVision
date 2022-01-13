grayscale = read_gray('vassilis4.jpg');
template = imread('tmp10.png');
result = ssd_bn_search(grayscale, template);

%[result, max_scales] = ssd_bn_multiscale(grayscale, template, [1,1.5,3,5,7,9]);
i=1;
for k = 1:1
    
    figure(i)
    imshow(result,[])
    i=i+1;
    [template_rows, template_cols] = size(template);
    result(result == -1) = nan;
    min_value = min(min(result));
    [x,y] = find(result == min_value);
    figure(i);
    imshow(draw_rectangle2(grayscale,x,y,template_rows,template_cols),[]);
    i=i+1;
end