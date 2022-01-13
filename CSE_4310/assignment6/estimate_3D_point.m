function result = estimate_3D_point(c1, c2, u1, v1, u2, v2)

%estimates the 3D world coordinates of a point, given two camera matrices and given the locations where that point projects on those two cameras
    %result is a 3x1 column vector, whose format is [x, y, z]'
    
    [line_1A1, line_1B1] = returnsAandB(c1,u1,v1,u1*2);
    line_1W1 = line_1A1\line_1B1; %this will be the [y,z] pair connected to x=1 that we passed earlier
    Point11 = [u1*2,line_1W1(1),line_1W1(2)].';
    
    [line_1A2, line_1B2] = returnsAandB(c1,u1,v1,u1-1);
    line_1W2 = line_1A2\line_1B2;
    Point12 = [u1-1,line_1W2(1),line_1W2(2)].';
    
    [line_2A1, line_2B1] = returnsAandB(c2,u2,v2,u1/2);
    line_2W1 = line_2A1\line_2B1;
    Point21 = [u1/2,line_2W1(1),line_2W1(2)].';
    
    [line_2A2, line_2B2] = returnsAandB(c2,u2,v2,u1+2);
    line_2W2 = line_2A2\line_2B2;
    Point22 = [u1+2,line_2W2(1),line_2W2(2)].';
    
    %So far we have two points each in lines 1 and 2. Moving on to get the
    % "intersection" of the lines
    
    parallel_vector1 = Point12 - Point11; 
    parallel_vector2 = Point22 - Point21; 
    
    %Points are column vectors and so are parallel vectors
    
    %Now, need to solve for a1 and a2
    intersection_A = [parallel_vector1.' * parallel_vector1 , -parallel_vector2.' * parallel_vector1; parallel_vector1.' * parallel_vector2 , -parallel_vector2.' * parallel_vector2];
    intersection_B = [Point21.' * parallel_vector1 - Point11.' * parallel_vector1; Point21.' * parallel_vector2 - Point11.' *parallel_vector2];
    solution_As = intersection_A \ intersection_B;
    result = ((Point11 + solution_As(1)*parallel_vector1)+(Point21 + solution_As(2)*parallel_vector2))/2;
end

