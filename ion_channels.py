# Copyright (c) 2020 Kyle Lopin (Naresuan University) <kylel@nu.ac.th>

"""

"""

__author__ = "Kyle Vitatus Lopin"


from numpy import exp

"""
### Sodium Channels
"""
g_Na = 40  # mS*cm**-2
E_Na = 50  # mV
# m gate
alpha_m_VShift = 38
alpha_m_max = 0.109
alpha_m_slope = 5
beta_m_VShift = 38
beta_m_max = 0.0744
beta_m_slope = 5

# h gate
alpha_h_VShift = 55
alpha_h_max = 0.0192
alpha_h_slope = 15
beta_h_VShift = 17
beta_h_max = 2.48
beta_h_slope = 21


def alpha_m(Vm):
    return alpha_m_max*(Vm+alpha_m_VShift) / ( 1 - (exp(-( Vm + alpha_m_VShift ) / alpha_m_slope )) )


def beta_m(Vm):
    return beta_m_max*(Vm+beta_m_VShift) / ((exp( (Vm + beta_m_VShift) / beta_m_slope )) - 1)


def alpha_h(Vm):
    return alpha_h_max*exp( -(alpha_h_VShift + Vm) / alpha_h_slope )


def beta_h(Vm):
    return beta_h_max / (1 + exp((beta_h_VShift-Vm) / beta_h_slope))


def I_Na(Vm, m, h):
    return g_Na * m**3 * h * (Vm - E_Na)


"""
### Potassium Channels      
"""
g_K = 1.2  # mS*cm**-2
E_K = -80  # mV
# n gate
alpha_n_VShift = 45
alpha_n_max = 0.012
alpha_n_slope = 5
beta_n_VShift = 50
beta_n_max = 0.204
beta_n_slope = 40


def alpha_n(Vm):
    return alpha_n_max*(Vm+alpha_n_VShift) / ( 1 - exp( -(Vm + alpha_n_VShift) / alpha_n_slope ) )


def beta_n(Vm):
    return beta_n_max*exp(-(Vm + beta_n_VShift) / beta_n_slope)


def I_K(Vm, n):
    return g_K * n**4 * (Vm - E_K)


"""
### Leak Channels   
"""
g_L = 1.6  # mS*cm**-2
E_L = -65  # mV


def I_leak(Vm):
    return g_L * (Vm - E_L)


"""
### L-type Channels   
"""
zkT = 52  # meV (z = +2, kT = 26 meV at room temperature)



