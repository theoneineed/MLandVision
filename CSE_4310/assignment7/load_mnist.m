function [mnist_digits,mnist_labels] = load_mnist(filename)
    mnist_file = filename;
    fid = fopen(mnist_file, 'r');

    [number, count] = fread(fid, 1, 'int32');
    if count ~= 1
        disp('failed to read number');
    end

    [mnist_permutation, count] = fread(fid, number, 'int32');
    if count ~= mnist_permutation
        disp('failed to read number');
    end


    [mnist_labels, count] = fread(fid, number, 'uchar');
    if count ~= number
        disp('failed to read number');
    end

    mnist_digits = fread(fid, [28, 28 * number], 'uint8=>uint8');
    mnist_digits = reshape(mnist_digits, [28, 28, number]);

    fclose(fid);
    %disp('loaded mnist digits');
end
