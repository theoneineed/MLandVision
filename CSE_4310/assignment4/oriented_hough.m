function votes = oriented_hough(grayscale, thetas, rhos, thr1, thr2)
    grayscale = double(grayscale);
    edges = canny(grayscale,thr1);
    figure(4)
    imshow(edges,[]);
    votes = zeros(length(rhos),length(thetas));
    %here is where hough work has to be done
    [row_edge,col_edge] = size(edges);

    o = gradient_orientations(edges,2);    
    
    for i=1:row_edge
        for j = 1:col_edge
            if(edges(i,j) == 0)
                continue
            end

            for theta = thetas
                if (orientation_difference(o(i,j), theta) <= thr2)
                    rho = find_rho(j,i,theta);
                    diff_rho = abs(rhos - rho);
                    [minValue, rho_indexes] = min(diff_rho);
                    rho_indexes = find(diff_rho == min(diff_rho));
                    theta_index = find(thetas == theta);
                    for loop = length(rho_indexes)
                        votes(rho_indexes(loop),theta_index) = votes(rho_indexes(loop),theta_index) + 1/length(rho_indexes);
                
                    end
                end    
           end
        end
    end
    votes_to_draw = votes;
    result = grayscale/2;
    for i = 1:2
        max_value = max(max(votes_to_draw));
        [rho_indices, theta_indices] = find(votes_to_draw == max_value);
        rho_index = rho_indices(1);
        theta_index = theta_indices(1);
        rho = rhos(rho_index);
        theta = thetas(theta_index);
        result = draw_line2(result, rho, theta);
        votes_to_draw(rho_index, theta_index) = 0;
    end
    figure()
    imshow(result,[]);
end

