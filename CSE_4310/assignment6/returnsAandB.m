function [A,B] = returnsAandB(c,u,v,x)
%takes in camera_matrix,projected co-ordinates, x and returns matrix A and B
%used for calculation later
    A = [(c(1,2) - c(3,2)*u), (c(1,3) - c(3,3)*u); (c(2,2) - c(3,2)*v), (c(2,3) - c(3,3)*v)];
    B = [c(3,1)*x*u + u - c(1,1)*x - c(1,4); c(3,1)*x*v + v - c(2,1)*x - c(2,4)]; 

end

