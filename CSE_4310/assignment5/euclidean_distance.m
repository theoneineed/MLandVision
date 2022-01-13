function distance = euclidean_distance(image1, image2)
%takes in as arguments two grayscale images A,
%and returns the Euclidean distance of those two grayscale images.
img1 = image1(:);
img2 = image2(:);
distance = sqrt(sum((img1 - img2).^2,'all'));
end

