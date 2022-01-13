%Nabin Chapagain, 1001551151%
function [avg,stdev] = file_stats(pathname)
    fileID = fopen(pathname,'r');
    A = fscanf(fileID, '%f');
    avg = mean(A);
    stdev = std(A);
    fclose(fileID);
end