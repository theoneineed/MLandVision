function camera_matrix = perspective_calibration(correspondences)
%returns the 3x4 camera matrix that maps 3D world coordinates to 2D pixel coordinates.
    %correspondences passed is Nx5 matrix with each line with
    %1x5 matrix where first three elements are x,y,z component and last two
    %are u,v component
    
    no_rowsA = size(correspondences,1)*2;
    A = zeros(no_rowsA,11);
    A((0:no_rowsA/2-1)*2+1, 1:3) = correspondences(:,1:3);
    A((0:no_rowsA/2-1)*2+1, 9:11) = -correspondences(:,1:3).*correspondences(:,4);
    A((1:no_rowsA/2)*2, 5:7) = correspondences(:,1:3);
    A((1:no_rowsA/2)*2, 9:11) = -correspondences(:,1:3).*correspondences(:,5);
    A((0:no_rowsA/2-1)*2+1, 4) = 1;
    A((1:no_rowsA/2)*2, 8) = 1;
    
    B = zeros(no_rowsA/2,2);
    B(:,1:2) = correspondences(:,4:5);
    B = B.';
    B = B(:);
    X = A\B;
    X(end + 1) = 1;
    X = X.';
    %since X, here will be in vector form, we need to convert it to matrix
    camera_matrix = reshape(X(:), 4, []).';
    
end

