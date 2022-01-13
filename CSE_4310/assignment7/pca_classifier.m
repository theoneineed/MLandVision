function class_label = pca_classifier(image, data_file, d)
    
    eigenvectors = zeros(784,d,10);
    eigenvalues = zeros(d,1,10);
    average_return = zeros(784,1,10);
    for i=1:10
        j=i;
        if (i==10)
            j=0;
        end
        
        [eigenvectors(:,:,i), eigenvalues(:,:,i), average_return(:,:,i)] = mnist_pca(data_file, j, d);
        
    end
    
    %now to compute the projection error
    %P(V) = <V-avg, P1 > = P1’ * (V – avg) if P1 is first eigenvector
    
    V = image(:);
    Projection =  zeros(10,d);
    for c = 1:10 %that is for each label from 0 to 9
        for j = 1:d
            Projection(c,j) = eigenvectors(:,j,c)' * (V - average_return(:,:,c));
            %gives c by j matrix which is projection dependent on label and
            %the order of the eigenvector being used
        end
    end
    
    %Backprojection
    
    BackProjection =  zeros([size(V),10*d]);
    for j = 1:d %for each of the d eigenvectors 
        for c = 1:10 %that is for each label from 0 to 9
            BackProjection(:,:,j*(d-1)+c) =  eigenvectors(:,j,c) * Projection(c,j) +average_return(:,:,c);
        end
    end
    
    SSD = zeros(10*d,1);
    for loop = 1:(10*d)
        predicted = BackProjection(:,:,loop);
        diff_vector = predicted(:) - V(:);
        squared_diffs = diff_vector .* diff_vector;
        SSD(loop) = sum(squared_diffs);
    end
    min_index = find(SSD == min(SSD));
    min_index_index = randi(size(min_index,1));
    class_label = mod(min_index_index,10);

end


