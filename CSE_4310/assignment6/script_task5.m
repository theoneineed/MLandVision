values = load('check_u1v1.txt');
ac1 = load('img1_wc1.txt');
bc2 = load('img1_wc2.txt');
cm1 = perspective_calibration(ac1);
cm2 = perspective_calibration(bc2);
for i = 1:size(values,1)
    result = estimate_3D_point(cm1, cm2, values(i,1), values(i,2), values(i,3), values(i,4));
    disp(result.')
    %disp(values(i,1))
    %disp(values(i,2))
end