function result = ssd_search(grayscale, template)
    result = zeros(size(grayscale));
    result = result-1;
    grayscale = double(grayscale);
    template = double(template);
    [no_rowt,no_colt] = size(template);
    [no_row,no_col] = size(result);
    temp_rhalf = fix(no_rowt/2);
    temp_chalf = fix(no_colt/2);
    template_vector = template(:);
    for i= (1+temp_rhalf):(no_row-temp_rhalf)
        for j = (1+temp_chalf):(no_col-temp_chalf)
            window = grayscale(i-temp_rhalf:i+temp_rhalf,j-temp_chalf:j+temp_chalf);
            window_vector = window(:);
            diff_vector = window_vector - template_vector;
            squared_diffs = diff_vector .* diff_vector;
            ssd_score = sum(squared_diffs);
            %disp(ssd_score)
            result(i,j) = ssd_score;
        end
    end
end

