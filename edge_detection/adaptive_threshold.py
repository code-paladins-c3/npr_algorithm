import numpy as np

def calculate_threshold(gradient_magnitude, tolerance=1e-3, alpha=0.7):
    
    T0 = np.max(gradient_magnitude)
    T1 = np.min(gradient_magnitude)
    
   
    T_squared = (T0 * alpha) ** 2

    
    adapative_threshold = (T_squared + T1) / 2

    while True:
        
        Ta_values = gradient_magnitude[gradient_magnitude >= adapative_threshold]
        Tb_values = gradient_magnitude[gradient_magnitude < adapative_threshold]

    
        Ta = np.mean(Ta_values) if len(Ta_values) > 0 else 0
        Tb = np.mean(Tb_values) if len(Tb_values) > 0 else 0

        
        new_T = (Ta + Tb) / 2

       
        if abs(new_T - adapative_threshold) < tolerance:
            break

        adapative_threshold = new_T

    
    gradient_magnitude[gradient_magnitude < adapative_threshold] = 0

    return adapative_threshold
