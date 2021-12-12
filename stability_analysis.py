import numpy as np
import matplotlib.pyplot as plt
import control

# controller Parameters
Kp = 0.8
Ti = 18
# TF for pi controller
num_c = np.array ([Kp*Ti, Kp])
den_c = np.array ([Ti , 0])
Hc = control.tf(num_c, den_c)
print ('Hc(s) =', Hc)

# Process Parameters
Kh = 3.5
theta_t = 22
theta_d = 2
# transfer function for air heater 
num_p = np. array ([Kh])
den_p = np. array ([theta_t, 1])
Hp1 = control.tf(num_p , den_p)
N = 5 # Time Delay - Order of the Approximation
[num_pade,den_pade] = control.pade(theta_d, N)
Hp_pade = control.tf(num_pade,den_pade);
Hp = control.series(Hp1, Hp_pade);
print ('Hp(s) =', Hp)

#filter parameters
Tf=5*theta_t
# TF for filter
num_f = np.array ([1])
den_f = np.array ([Tf*theta_t,1])
Hf = control.tf(num_f, den_f)
print ('Hf(s) =', Hf)

#-----------------------------------------------------------------------------
L = control.series(Hc, Hp)  # Transfer function for the loop
print ('L(s) =', L)
T = control.feedback(L,1) # Transfer function for the tracking
print ('T(s) =', T)

# Step Response
t, y = control.step_response(T)
plt.figure(1)
plt.plot(t,y)
plt.title("Step Response T(s)")
plt.grid()

# Bode Diagram
plt.figure(2)
plt.title("Bodeplot")
control.bode(L, dB=True, deg=True, margins=True, grid=True)
plt.show(2)
# Poles and Zeros
control.pzmap(T)
p = control.pole(T)
z = control.zero(T)
print("poles = ", p)

gm , pm , w180 , wc = control.margin(L) # Calculating stability margins and crossover frequencies

gmdb = 20 * np.log10(gm) # Convert gm to Decibel
print("wc =", f'{wc:.2f}', "rad/s")
print("w180 =", f'{w180:.2f}', "rad/s")
print("GM =", f'{gm:.2f}')
print("GM =", f'{gmdb:.2f}', "dB")
print("PM =", f'{pm:.2f}', "deg")

# Find when Sysem is Marginally Stable (Kritical Gain - Kc)
Kc = Kp*gm
print("Kc=", f'{Kc:.2f}')

"""
# controller Parameters
Kp = 0.8
Ti = 10
# TF for pi controller
num_c = np.array ([Kp*Ti, Kp])
den_c = np.array ([Ti , 0])
Hc = control.tf(num_c, den_c)
print ('Hc(s) =', Hc)

# Process Parameters
Kh = 3.5
theta_t = 22
theta_d = 2
# transfer function for air heater 
num_p = np. array ([Kh])
den_p = np. array ([theta_t , 1])
Hp1 = control.tf(num_p , den_p)
N = 5 # Time Delay - Order of the Approximation
[num_pade,den_pade] = control.pade(theta_d, N)
Hp_pade = control.tf(num_pade,den_pade);
Hp = control.series(Hp1, Hp_pade);
print ('Hp(s) =', Hp)

#filter parameters
Tf=5*theta_t
"""