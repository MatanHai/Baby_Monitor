const int pirPin = 2;      // חיישן PIR
const int ledPin = 3;      // נורת לד
bool motionSent = false;   // נשלחה הודעה על תנועה?

void setup() {
  Serial.begin(9600);
  pinMode(pirPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int pirState = digitalRead(pirPin);

  if (pirState == HIGH && !motionSent) {
    digitalWrite(ledPin, HIGH);               // הדלקת לד
    Serial.println("MOTION_DETECTED");        // שליחת הודעה
    motionSent = true;                        // סמן שנשלחה
  }

  if (pirState == LOW && motionSent) {
    digitalWrite(ledPin, LOW);                // כיבוי לד
    motionSent = false;                       // איפוס לדיווח הבא
  }

  delay(100);
}
