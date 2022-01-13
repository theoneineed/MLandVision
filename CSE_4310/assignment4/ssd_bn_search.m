function result = ssd_bn_search(grayscale, template)
    result = zeros(size(grayscale));
    result = result-1;
    grayscale = double(grayscale);
    template = double(template);
    template = template - mean(template(:));
    [no_rowt,no_colt] = size(template);
    [no_row,no_col] = size(result);
    temp_rhalf = fix(no_rowt/2);
    temp_chalf = fix(no_colt/2);
    for i= (1+temp_rhalf):(no_row-temp_rhalf)
        for j = (1+temp_chalf):(no_col-temp_chalf)
            subwindow_ij = grayscale(i-temp_rhalf:i+temp_rhalf,j-temp_chalf:j+temp_chalf);
            subwindow_ij = subwindow_ij - mean(subwindow_ij(:));
            diff_vector = subwindow_ij(:) - template(:);
            result(i,j) = sum(diff_vector .* diff_vector);
        end
    end
end
