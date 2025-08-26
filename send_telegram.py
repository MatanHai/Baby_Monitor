import serial
import time
import requests

BOT_TOKEN = "8179185642:AAF_FBAUj35ZWUK1UMNLi0Jy8ECe18YTOSI"
CHAT_ID = "394756951"
SERIAL_PORT = "/dev/tty.usbmodem11201"
BAUD_RATE = 9600

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    try:
        response = requests.post(url, data=payload)
        print("Telegram sent:", response.text)
    except Exception as e:
        print("Failed to send Telegram message:", e)

def monitor_serial():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print("Connected to serial port.")
        time.sleep(2)
        while True:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if line:
                print("Received:", repr(line))
                if "motion" in line.lower():
                    print("Motion detected!")
                    send_telegram_message("👶 Motion detected in the baby room!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    monitor_serial()
