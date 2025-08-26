👶 Baby Room Motion Monitor with Telegram Alerts

A simple and effective baby room monitoring system using **Arduino** and **Python**, which detects motion and sends real-time **Telegram notifications** to your phone.

Project Overview

This project combines:

* A **PIR motion sensor** connected to an **Arduino Uno**
* A **Python script** on your computer that reads the serial output
* A **Telegram bot** that sends alerts when motion is detected

Perfect for baby monitoring, pet detection, or basic home security applications.

---

🧰 Hardware Components

* Arduino Uno
* PIR Motion Sensor (HC-SR501 or similar)
* LED (optional – visual motion indicator)
* USB cable (to connect Arduino to computer)

---

🧠 How It Works

1. Arduino reads input from the PIR sensor.
2. When motion is detected:

   * The onboard LED turns on.
   * A message `"MOTION_DETECTED"` is sent via the serial port.
3. A Python script listens to the serial port.
4. Upon receiving the `"MOTION_DETECTED"` message, a **Telegram bot** sends a notification like:

   ```
   👶 Motion detected in the baby room!
   ```

---

 💻 Software Setup

1. **Upload the Arduino sketch** from `sketch_aug26a.ino`.

2. **Install Python dependencies**:

   ```bash
   pip install pyserial requests
   ```

3. **Edit `send_telegram.py`**:

   * Insert your bot's `BOT_TOKEN` and your personal `CHAT_ID`.

4. **Run the script**:

   ```bash
   python3 send_telegram.py
   ```

