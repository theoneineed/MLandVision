function IoverU = IntoverUni(A,B)
    %A and B are two objects with top,bottom, left and right pixel locations of each
    Ta = A(1);
    Ba = A(2);
    La = A(3);
    Ra = A(4);
    Tb = B(1);
    Bb = B(2);
    Lb = B(3);
    Rb = B(4);
    
    T_a_int_b = max(Ta, Tb);
    B_a_int_b = min(Ba, Bb);
    L_a_int_b = max(La, Lb);
    R_a_int_b = min(Ra, Rb);
    
    Height_a = Ba-Ta+1;
    Width_a = Ra-La+1;
    Area_a = Height_a * Width_a;
    
    Height_b = Bb - Tb +1;
    Width_b = Rb - Lb +1;
    Area_b = Height_b * Width_b;
    
    Height_a_int_b = B_a_int_b - T_a_int_b +1;
    Width_a_int_b = R_a_int_b - L_a_int_b +1;
    Area_a_int_b = Height_a_int_b * Width_a_int_b;
    
    Area_a_union_b = Area_a+ Area_b - Area_a_int_b;
    
    IoverU = Area_a_int_b/Area_a_union_b;
    
    if (Height_a_int_b <= 0)
        IoverU = 0;
    end
    
    if (Width_a_int_b <= 0)
       IoverU = 0; 
    end
    
end
