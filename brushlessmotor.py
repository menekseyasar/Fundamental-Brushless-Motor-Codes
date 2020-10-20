from future import division 
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

kademe = 0.25
motor_pwm = 2048

if L1 == 1:
    kademe += 0.25 
    if kademe>1.0:                # Kademenin %25 ve %100 sınırlandırması.
        kademe -=1.0              # Tam güçten sonra %25 değerine döner

motor_pwm = ((2048*kademe) * analog) + 2048
zıt_motor_pwm = 2048 - ((2048*kademe) * analog)

# Not: Aracın 'yön hareketleri' denemede belirlenir, kalibre edilmesi gerekir.
# axis değişkeni konsolda analog'un eksenlerini ifade eder. 

if axis == 0: # Sol X       # Araç ileri-geri hareketi    
    pwm.set_pwm(0, 0, motor_pwm)       #pwm.set_pwm(kanal, on, off)
    pwm.set_pwm(1, 0, motor_pwm)        
    pwm.set_pwm(2, 0, motor_pwm)    
    pwm.set_pwm(3, 0, motor_pwm)

if axis == 1: #Sol Y        # Araç sağa ya da sola dönmesi-rotate     
    pwm.set_pwm(0, 0, motor_pwm)       
    pwm.set_pwm(1, 0, zıt_motor_pwm)        
    pwm.set_pwm(2, 0, motor_pwm)    
    pwm.set_pwm(3, 0, zıt_motor_pwm)

if axis == 2 and x == 0: # Sağ Y       # Araç yukarı ya da aşağı kayma işlemi   
    pwm.set_pwm(4, 0, motor_pwm)       
    pwm.set_pwm(5, 0, motor_pwm)        
    pwm.set_pwm(6, 0, motor_pwm)
    pwm.set_pwm(7, 0, motor_pwm)        

if axis == 3: #Sağ X        # Araç sağa ya da sola kayma işlemi  
    pwm.set_pwm(0, 0, motor_pwm)       
    pwm.set_pwm(1, 0, zıt_motor_pwm)        
    pwm.set_pwm(2, 0, zıt_motor_pwm)    
    pwm.set_pwm(3, 0, motor_pwm)

if axis == 2 and x==1: #Sağ Y ve X butonu       # Aracın önünü kaldırıp indirme
    if motor_pwm>2048:
        pwm.set_pwm(4, 0, motor_pwm)       
        pwm.set_pwm(5, 0, motor_pwm) 
    if motor_pwm<2048:
        pwm.set_pwm(6, 0, motor_pwm)       
        pwm.set_pwm(7, 0, motor_pwm) 
