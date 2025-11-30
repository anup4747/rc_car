import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/baburao/Desktop/rc_car/rc_car_workspace/install/rc_car_workspace'
