# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 16:30:40 2025

@author: eugen
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import scipy.io as sio
import scipy.ndimage as nd 
import scipy.interpolate as inter

#------------------------------------------------------------------------------
# Lectura de ECG #
#------------------------------------------------------------------------------


fs_ecg = 1000 # Hz

#------------------------------------------------------------------------------
# ECG con ruido
#------------------------------------------------------------------------------
# para listar las variables que hay en el archivo
sio.whosmat('ecg.mat')
mat_struct = sio.loadmat('ecg.mat')

ecg_one_lead = mat_struct['ecg_lead']

N = len(ecg_one_lead)

hb_1 = mat_struct['heartbeat_pattern1']
hb_2 = mat_struct['heartbeat_pattern2']
ecg_cortado = ecg_one_lead[5000:12000]
plt.figure(1)
plt.plot(ecg_one_lead[5000:12000])

plt.figure(2)
plt.plot(hb_1)

plt.figure(3)
plt.plot(hb_2)

##################
## ECG sin ruido
##################
ecg_one_lead = mat_struct('ecg_lead')

plt.figure(4)
plt.plot(ecg_one_lead)


#%%
#------------------------------------------------------------------------------
# ECG filtrado con mediana
#------------------------------------------------------------------------------

nd.median_filter(ecg_one_lead)






































primer_filt = nd.median_filter(ecg_cortado, 200)
Estimacion_ruido_lb = nd.median_filter(primer_filt, 600)

ECG_sin_Inter = ecg_cortado - Estimacion_ruido_lb

plt.figure(5)
plt.plot(ECG_sin_Inter)

#%%
latidos = mat_struct['qrs_detections'].reshape(1903) #Coordenadas en muestra de latidos
IsoElec = latidos - 30 #Coordenadas en muestras de ptos isoelectricos


Estimacion_Ruido = inter.CubicSpline(,IsoElec[6:15])