from time import sleep
from gpiozero import PWMOutputDevice
import board 
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D18)
motor = PWMOutputDevice(17, frequency=1000)

def bereken_pwm(waarde, min_in, max_in):
    return max(0, min(1, (waarde - min_in) / (max_in - min_in))) 

while True :
    try :
        temperature_C = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print("temp: {:.1F}C      humidity: {}% " .format(temperature_C,humidity))
        
        pwm_temp = bereken_pwm(temperature_C, 15, 30)
        pwm_hum = bereken_pwm(humidity, 25, 70)
        pwm_motor = max(pwm_temp, pwm_hum)
        motor.value = pwm_motor

    except RuntimeError as error :
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error :
        dhtDevice.exit()
        raise error
    