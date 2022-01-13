function [eigenvectors, eigenvalues, average_return] = mnist_pca(data_file, class_label, d)

    [mnist_digits,mnist_labels] = load_mnist(data_file);
    
    indices = mnist_labels == class_label; %is an array with indices where the class_label is stored
    data_we_deal_with = mnist_digits(:,:,indices);
    %Finding the Best Projection: PCA
    
    number = size(data_we_deal_with,3);
    average = mean(data_we_deal_with,3);
    centered_points = zeros([size(data_we_deal_with,1) * size(data_we_deal_with,2),size(data_we_deal_with,3)]);
    for index = 1:number
        dummy_list = data_we_deal_with(:,:, index);
        centered_points(:,index) = double(dummy_list(:)) - double(average(:));
    end

    covariance_matrix = centered_points * centered_points';
    [all_eigenvectors, all_eigenvalues] = eig(covariance_matrix);
    all_eigenvalues = diag(all_eigenvalues);
    [all_eigenvalues, ev_indices] = sort(all_eigenvalues, 'descend');
    all_eigenvectors = all_eigenvectors(:, ev_indices);
    eigenvectors = all_eigenvectors(:,1:d);
    eigenvalues = all_eigenvalues(1:d,:);
    average_return = average(:);
    
end

