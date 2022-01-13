function [scores, max_scales] = ssd_bn_multiscale(grayscale, template, scales)

    scores = ones(size(grayscale)) * -10;
    max_scales = zeros(size(grayscale));
    for scale = scales
        % for efficiency, we either downsize the image, or the template, 
        % depending on the current scale
        if scale >= 1
            scaled_image = imresize(grayscale, 1/scale, 'bilinear');
            temp_result = ssd_bn_search(scaled_image, template);
            temp_result = imresize(temp_result, size(grayscale), 'bilinear');
        else
            scaled_template = imresize(template, scale, 'bilinear');
            temp_result = ssd_bn_search(grayscale, scaled_template);
        end
        
        higher_maxes = (temp_result > scores);

        max_scales(higher_maxes) = scale;
        scores(higher_maxes) = temp_result(higher_maxes);
    end

end