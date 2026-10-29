import numpy as np
import matplotlib.pyplot as plt
def mse(y, y_hat):
    return np.mean((y-y_hat)**2)
def mnk(x, y):
    A = np.array([
        [np.mean(x**4), np.mean(x**3),np.mean(x**2)],
        [np.mean(x**3), np.mean(x**2),np.mean(x)],
        [np.mean(x**2), np.mean(x),x.size],
    ])
    B = np.array([np.mean(x**2*y), np.mean(x*y),np.mean(y)])
    a,b,c = np.linalg.solve(A,B)
    return a,b,c
rng = np.random.default_rng(42)
Q = np.linspace(0.5,5.0,25)
dp = 2.0*Q+0.8*Q**2+rng.normal(0,1.0,Q.size)
a,b,c = mnk(Q,dp)
print(a,b,c) #0.8114925751105655 1.9591107491162103 -0.0012346804323716462
print(mse(dp, a*Q**2+b*Q+c))
print(mse(dp, 2*Q+0.8*Q**2))
plt.plot(Q,a*Q**2+b*Q+c,'-')
plt.plot(Q,dp, 'o')
plt.xlabel('Q, л/с'); plt.ylabel('dp, кПа')
plt.grid(alpha=0.3); plt.show()
