import numpy as np
import matplotlib.pyplot as plt


r = np.arange(0.05,1,0.01)
E_a = -1.436/r
E_r = (7.32*10**(-6))/r**8
E_n = (E_a + E_r)
point = r[list(E_n).index(min(list(E_n)))]

plt.plot(r,E_a, label = '$E_{A}$')
plt.plot(r,E_r, label = '$E_{R}$')
plt.plot(r,E_n, label = '$E_{N}$')
plt.legend()
plt.xlim([0.00, 1.00])
plt.ylim([-10, 10])
plt.xlabel('$r(nm)$')
plt.ylabel('$Energy(eV)$')
plt.plot([point, point], [0, min(E_n)])
plt.scatter(point, min(E_n))
plt.annotate("$r_{0} = 0.24nm $", (point, min(E_n)))

plt.plot([0, point], [min(E_n), min(E_n)], '--')
plt.scatter(0, min(E_n))
plt.annotate("$E_{0} = -5.3eV$", (0, min(E_n)))
plt.axvline(0)
plt.axhline(0)


plt.show()

print('Equilibrium spacing = '+ str(point) + 'nm')
print('Magnitude of Energy at r_0 = '+ str(min(E_n)) + 'eV')

