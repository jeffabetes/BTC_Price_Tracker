import I2C_LCD_driver
import time
import requests
mylcd = I2C_LCD_driver.lcd()


while True:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    
    mylcd.lcd_display_string(" Bitcoin price:", 1)
    
    mylcd.lcd_display_string("  $" + (data["bpi"]["USD"]["rate"]), 2)
    
    time.sleep(60)
