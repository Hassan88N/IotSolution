#library
import nidaqmx
import matplotlib.animation as animation
#---------------------------------------------
import paho.mqtt.client as mqtt
import time
# Air Heater System
import numpy as np
import time
import matplotlib.pyplot as plt

topic="Sensor/temperature/temperatureout" 
topic2="Sensor/temperature/setpoint"  

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Received message: " + msg.topic + " -> " + msg.payload.decode("utf-8"))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# create the client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set("nawal12345", "Passord12345")# set username and password
client.connect("e8ffbe80fec84f149f9d583523ed4867.s1.eu.hivemq.cloud", 8883) # connect to HiveMQ Cloud on port 8883
# subscribe to the topic "my/test/topic"
client.subscribe("Sensor/temperature/temperatureout") 
client.subscribe("Sensor/temperature/setpoint")
# Model Parameters
Kh = 3.5
theta_t = 22
theta_d = 2
Tenv = 21.5
# Simulation Parameters
Ts = 0.1 # Sampling Time
Tstop = 200 #stop simulation
N = int(Tstop/Ts) # Number of samples
Tout = np.zeros(N+2) 
Tout[0] = Tenv # Initial Vaue

#Controller settings
Kp = 0.8
Ti = 18
r = 26 # Reference value [degC]
e = np.zeros(N+2) # Initialization
e[0]=0
u = np.zeros(N+2) # Initialization
t = np.arange(0,Tstop+2*Ts,Ts) #Create the Time Series
u_stored=0
e_stored=0 
Tf=5*Ts
a=Ts/(Tf+Ts)
yf = np.zeros(N+2)
yf[0] = Tenv

# plot appearence 
t = np.arange(0,Tstop+2*Ts,Ts)
plt.figure(1)
plt.title('Control Signal')
plt.xlabel('t [s]')
plt.ylabel('u [V]')
plt.grid()

plt.figure(2)
plt.title('Temperature')
plt.xlabel('t [s]')
plt.ylabel('Tout [degC]')
plt.grid()

#Simulation
for k in range(N+1):
#PI Controller
    e[k] = r - Tout[k]
    u[k] = u[k-1] + Kp*(e[k] - e[k-1]) + (Kp/Ti)*e[k] 
    
    if u[k]>5:
        u[k] = 5
    if u[k]<0:
        u[k]=0
        
# Process Model
    Tout[k+1] = Tout[k] + (Ts/theta_t) * (-Tout[k] + Kh*u[int(k-theta_d/Ts)] + Tenv)
    #print("t = %2.1f, u = %3.2f, Tout = %3.2f" %(t[k], u[k], Tout[k+1]))
#filter
    
    yf[k+1]=(1-a)*yf[k]+a*Tout[k+1]
    yf[k]=yf[k+1]
    Tout[k+1]=yf[k+1]
    
    

    if k%10 == 0: #live plot
        #Control Signal
        plt.figure(1)
        plt.plot(t[k],u[k], '-o', markersize=5, color='red')
        plt.ylim(0, 5)
        plt.show()
        plt.pause(Ts)
        
        #Temperature
        plt.figure(2)
        plt.plot(t[k],Tout[k+1], '-gD', markersize=5, color='blue')
        plt.plot(t[k],r, '-o', markersize=5, color='green')
        plt.ylim(20, 32)
        plt.show()
        plt.pause(Ts)
        #plt.pause(Ts)
        
    control="{:3.2f}".format(u[k])
    setpoint=r
    data="{:3.2f}".format(Tout[k])
    print ("the temperature out is: %s" %(data))
    print ("the setpoint is: %.2f" %(setpoint))
    #print("Measured temperature value: %3.2f" %float(data))
    client.publish(topic,data)   
    client.publish(topic2,setpoint)  
    
    data= Tout[k+1]    
    time.sleep(Ts)
    
#DAQ--------------------------------------------------------
# Read from DAQ Device
#task = nidaqmx.Task()
#task.ai_channels.add_ai_voltage_chan("TC02/ai0", min_val=0, max_val=10)
#task.start()
#def writedaq(value):
#    task1 = nidaqmx.Task()
#    task1.ao_channels.add_ao_voltage_chan('TC02/ao0','mychannel',0,5)
#    task1.start()
#    task1.write(value)
#    task1.stop()
#    task1.close()
#DAQ-------------------------------------------------------

