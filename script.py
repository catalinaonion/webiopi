import webiopi
import time

# デバッグ出力を有効に
webiopi.setDebug()

# GPIOライブラリの取得
GPIO = webiopi.GPIO

#GPIO arrangement
PWM0 = 21 #足回り
PWM1 = 20
PWM2 = 26 #アーム前後
PWM3 = 16 #アーム左右
PWM4 = 6 #arm up down
PWM5 = 5 #belt
PWM6 = 25 #belt

# WebIOPiの起動時に呼ばれる関数
def setup():
    webiopi.debug("Script with macros - Setup")
    # GPIOのセットアップ
    GPIO.setFunction(PWM0, GPIO.PWM)
    GPIO.setFunction(PWM1, GPIO.PWM)
    GPIO.setFunction(PWM2, GPIO.PWM)
    GPIO.setFunction(PWM3, GPIO.PWM)
    GPIO.setFunction(PWM4, GPIO.PWM)
    GPIO.setFunction(PWM5, GPIO.PWM)
    GPIO.setFunction(PWM6, GPIO.PWM)
    # 初期のデューティー比を7.5%に（静止状態）
    GPIO.pwmWrite(PWM0, 0.075)
    GPIO.pwmWrite(PWM1, 0.075)
    GPIO.pwmWrite(PWM2, 0.075)
    GPIO.pwmWrite(PWM3, 0.075)
    GPIO.pwmWrite(PWM4, 0.075)
    GPIO.pwmWrite(PWM5, 0.075)
    GPIO.pwmWrite(PWM6, 0.075)
    

# WebIOPiにより繰り返される関数
def loop():
    webiopi.sleep(5)

# WebIOPi終了時に呼ばれる関数
def destroy():
    webiopi.debug("Script with macros - Destroy")
    # GPIO関数のリセット（入力にセットすることで行う）
    GPIO.setFunction(PWM0, GPIO.IN)
    GPIO.setFunction(PWM1, GPIO.IN)
    GPIO.setFunction(PWM2, GPIO.IN)
    GPIO.setFunction(PWM3, GPIO.IN)
    GPIO.setFunction(PWM4, GPIO.IN)
    GPIO.setFunction(PWM5, GPIO.IN)
    GPIO.setFunction(PWM6, GPIO.IN)

@webiopi.macro
def leg(duty1,duty2):
    GPIO.pwmWrite(PWM0,duty1)
    GPIO.pwmWrite(PWM1,duty2)

@webiopi.macro
def arm_x(duty3):
    GPIO.pwmWrite(PWM2,duty3)

@webiopi.macro
def arm_y(duty4):
    GPIO.pwmWrite(PWM3,duty4)

@webiopi.macro
def arm_z(duty5):
    GPIO.pwmWrite(PWM4,duty5)

@webiopi.macro
def belt_trans(duty6):
    GPIO.pwmWrite(PWM5,duty6)

@webiopi.macro
def belt_turn(duty7):
    GPIO.pwmWrite(PWM6,duty7)





