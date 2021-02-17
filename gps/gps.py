import Adafruit_BBIO.UART as UART
from ublox_gps import UbloxGps
import serial

UART.setup("UART1")

# UART1: /dev/ttyO1, Rx: P9_26, Tx: P9_24
ser = serial.Serial(port="/dev/ttyO1", baudrate=38400)
gps = UbloxGps(ser)

def run():
  lat_prev = 0
  lon_prev = 0
  try: 
    print("Listenting for UBX Messages.")
    while True:
      try: 
        coords = gps.geo_coords()
        gps_time = gps.date_time()
        
        print("error lat: ", coords.lat - lat_prev)
        print("error lon: ", coords.lon - lon_prev)
        lat_prev = coords.lat
        lon_prev = coords.lon

        print(coords.lat, coords.lon)
        print("{}/{}/{}".format(gps_time.day, gps_time.month,
                                          gps_time.year))
        print("UTC Time {}:{}:{}".format(gps_time.hour, gps_time.min,
                                          gps_time.sec))
        print("Valid date:{}\nValid Time:{}".format(gps_time.valid.validDate,
                                                             gps_time.valid.validTime))
      except (ValueError, IOError) as err:
        print(err)
  
  finally:
    ser.close()

if __name__ == '__main__':
  run()
