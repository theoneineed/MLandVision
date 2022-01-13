function odiff = orientation_difference(ornt, theta)
    if(ornt<0)
        ornt = 180 + ornt;
    end
    if (theta<0)
        theta = 180 + theta;
    end
    odiff1 = abs(ornt-theta);
    odiff2 = 180-odiff1;
    odiff = min(odiff1,odiff2);
end

