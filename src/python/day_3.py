import numpy as np

def lines_to_mat(lines):
    mat = []    
    for line in lines:
        mat.append([int(i) for i in list(line.strip())])
    return np.array(mat)

def binary_list_to_decimal(bin_list):
    print(bin_list)
    d = 0.0
    for i in range(len(bin_list)):
        v = bin_list[::-1][i]
        d += v*(2**i)
    print(d)
    return d
        

def part1(file_path: str):
   
    lines =[] 
    with open(file_path) as f:
       lines = f.readlines() 
    mat = lines_to_mat(lines)

    n_half = np.ceil(mat.shape[0] / 2.0)
    
    print(n_half)

    tots = mat.sum(axis=0)
    print(tots)
    
    gamma_list = [1 if t >= n_half else 0 for t in list(tots)] 
    gamma = binary_list_to_decimal(gamma_list)
    alpha = binary_list_to_decimal([1 if g == 0 else 0 for g in gamma_list])

    return gamma*alpha


def part2(file_path: str):
   
    lines =[] 
    with open(file_path) as f:
       lines = f.readlines() 
    mat = lines_to_mat(lines)
    
    oxygen_temp = mat.copy()
    
    scruber_temp = mat.copy()
    
    for i in range(mat.shape[1]):
        
        tot_oxy = oxygen_temp[:,i].sum()
        
        tot_scruber = scruber_temp[:,i].sum()
        
        oxy_n_half = np.ceil(oxygen_temp.shape[0] / 2.0)
        
        scruber_n_half = np.ceil(scruber_temp.shape[0] / 2.0)

        oxy_num = 1 if tot_oxy >= oxy_n_half else 0 

        scruber_num = 0 if tot_scruber >= scruber_n_half else 1

        if oxygen_temp.shape[0] > 1:
            oxygen_temp = oxygen_temp[np.where(oxygen_temp[:,i] == oxy_num)]

        if scruber_temp.shape[0] > 1:
            scruber_temp = scruber_temp[np.where(scruber_temp[:,i] == scruber_num)]

    oxy = binary_list_to_decimal(list(oxygen_temp.flatten()))
    scruber = binary_list_to_decimal(list(scruber_temp.flatten()))

    return oxy*scruber

    


   

    
    