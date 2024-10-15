import numpy as np

def non_maximum_suppression(mag, ang, width, height):
    suppressed = np.zeros((height, width), dtype=np.float64)

    ang = np.abs(ang)
    ang = np.where(ang > 180, np.abs(ang - 180), ang)

    for i_y in range(1, height - 1):
        for i_x in range(1, width - 1):
            grad_ang = ang[i_y, i_x]

            if grad_ang <= 22.5 or grad_ang > 157.5:
                neighb_1 = mag[i_y, i_x - 1]
                neighb_2 = mag[i_y, i_x + 1]
            elif 22.5 < grad_ang <= 67.5:
                neighb_1 = mag[i_y - 1, i_x - 1]
                neighb_2 = mag[i_y + 1, i_x + 1]
            elif 67.5 < grad_ang <= 112.5:
                neighb_1 = mag[i_y - 1, i_x]
                neighb_2 = mag[i_y + 1, i_x]
            elif 112.5 < grad_ang <= 157.5:
                neighb_1 = mag[i_y + 1, i_x - 1]
                neighb_2 = mag[i_y - 1, i_x + 1]

            if mag[i_y, i_x] >= neighb_1 and mag[i_y, i_x] >= neighb_2:
                suppressed[i_y, i_x] = mag[i_y, i_x]
            else:
                suppressed[i_y, i_x] = 0
                
    foreground=suppressed[suppressed >= np.mean(suppressed)]
    background=suppressed[suppressed < np.mean(suppressed)]
    
    foreground_mean=np.mean(foreground)
    background_mean=np.mean(background)
    
    for i_y in range(1, height - 1):
        for i_x in range(1, width - 1):
            if suppressed[i_y, i_x] >= (foreground_mean + background_mean) / 2:
                suppressed[i_y, i_x] = suppressed[i_y, i_x]
            else:
                suppressed[i_y, i_x] = 0

    return suppressed
