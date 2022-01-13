function result = chi_squared(sc1, sc2)

    chi_sum = 0;
    for i=1:5
        for j = 1:12
            chi_sum = ((sc1(i,j) - sc2 (i,j))^2) / (sc1(i,j) + sc2(i,j)) + chi_sum; 
        end
    end
    result = chi_sum/2;
end