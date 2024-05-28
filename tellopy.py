from djitellopy import Tello
tello = Tello()
try:
    tello.connect()
    print("연결 성공!")
    print("배터리 상태:", tello.get_battery())
    tello.takeoff()
    tello.land()
except Exception as e:
    print("연결 실패:", e)
finally:
    tello.end()
