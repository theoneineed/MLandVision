function result = pinhole_location(correspondences)
    camera_matrix = perspective_calibration(correspondences);
    random_row1 = randi([1,14]);%choosing a random row to get x,y,z values
    Point11 = correspondences(random_row1, 1:3).';
    x1 = correspondences(random_row1, 1)*2;
    [line_1A, line_1B] = returnsAandB(camera_matrix,correspondences(random_row1,4),correspondences(random_row1,5),x1);
    line_1W = line_1A\line_1B;
    Point12 = [x1,line_1W(1),line_1W(2)].';
    %two points in line 1 achieved, do same for line 2.

    random_row2 = randi([16 ,27]);
    Point21 = correspondences(random_row2, 1:3).';
    x2 = correspondences(random_row2, 1)*2;
    [line_2A, line_2B] = returnsAandB(camera_matrix,correspondences(random_row2,4),correspondences(random_row2,5),x2);
    line_2W = line_2A\line_2B;
    Point22 = [x2,line_2W(1),line_2W(2)].';
    
    %so, we have point11, point12, point 21 and point 22 so far.
    %Since both these lines pass through the same point, which is pinhole,
    %we can calculate the location of pinhole using simple linear algebra
    u1 = Point12-Point11;
    u2 = Point22-Point21;
    mu = ((Point21(1)-Point11(1))*u1(2)-(Point21(2)-Point11(2))*u1(1))/(u2(2)*u1(1)-u2(1)*u1(2));
    lambda = ((Point21(1)-Point11(1))+ mu*u2(1))/u1(1);
    pinhole_coordinate1 = Point11 + lambda * u1;
    result = pinhole_coordinate1;
end

