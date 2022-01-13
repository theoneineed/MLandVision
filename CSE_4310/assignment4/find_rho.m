function rho = find_rho(x,y,theta)
%calculates rho from x,y and theta
    rho = x*cos(theta/180 * pi) + y*sin(theta/180 * pi);
end

