grayscale = read_gray('road7.jpg');
edges = canny(grayscale,5);
[votes,thetas,rhos] = hough(edges);
%rhos=[-7, -5, -3, -1, 1, 3, 5, 7];
%thetas = [90, -75, -60, -45, -30, -15, 0, 15, 30, 45, 60, 75];
%size(thetas)
%size(rhos)

oriented_hough(grayscale,thetas,rhos,5,10);
%10 is suitable threshold for road8.jpg to use in canny detection
%5 seems to be suitable for other cases