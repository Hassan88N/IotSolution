i=0
Sp=26



import pyodbc
import time
from datetime import datetime
import database
import paho.mqtt.client as mqtt

Ts=0.1
sensorName="tmp36"
unit= u"\N{DEGREE SIGN}"+"C"
topic="Sensor/temperature/temperatureout"
topic2="Sensor/temperature/setpoint"



#connecting to databse
#connectionString =database.GetConnectionString()
#conn=pyodbc.connect(connectionString)
#cursor= conn.cursor()
#query = "INSERT INTO MeasurementDatabase (SensorName,MeasurementValue,ReferenceValue, Unit, MeasurementDateTime) VALUES (?,?,?,?,?)"


#query = "INSERT INTO MeasurementD (MeasurementValue,ControlSignal, Setpoint, MeasurementDateTime) VALUES (?,?,?)"
def on_connect(client, userdata, flags, rc): #MQTT connection
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))

def on_message(client, userdata, msg): #PUBLISH message is received from the server.
    print("Received message: " + msg.topic + " -> " + msg.payload.decode("utf-8"))
    
    value=float(msg.payload.decode("utf-8"))   
    measurementValue="{:.2f}".format(value)#measurement value
    now=datetime.now()
    datetimeformat="%Y-%m-%d %H:%M:%S"
    measurementDateTime=now.strftime(datetimeformat)
    Rf=Sp
    referenceValue="{:.2f}".format(Rf)#measurement value  
    print ("Received message:Sensor/temperature/setpoint --> %s" %(referenceValue))
    
    #parameters=sensorName,measurementValue,referenceValue,unit,measurementDateTime  #inserting data
    #cursor.execute(query,parameters)
    #cursor.commit()
    time.sleep(Ts)

client = mqtt.Client()# create the client
client.on_connect = on_connect
client.on_message = on_message
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS) # enable TLS
client.username_pw_set("nawal12345", "Passord12345") # set username and password
client.connect("e8ffbe80fec84f149f9d583523ed4867.s1.eu.hivemq.cloud", 8883) # connect to HiveMQ Cloud on port 8883
client.subscribe("Sensor/temperature/temperatureout")# subscribe to the topic 

#client.subscribe("Sensor/temperature/controlsignal")  
#client.subscribe("Sensor/temperature/setpoint") 

client.loop_forever()















