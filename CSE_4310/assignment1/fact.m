%Nabin Chapagain, 1001551151%
function [factorial] = fact(x)
    if x == 1
        factorial = 1;
        return;
    end
    factorial = x* fact(x-1);
end
