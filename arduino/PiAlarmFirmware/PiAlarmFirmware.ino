#define RELAY_CTL_PIN 7

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(RELAY_CTL_PIN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  char Message = Serial.read();
  if(Message == 'a')
  {
    Serial.println("on");
    digitalWrite(RELAY_CTL_PIN, HIGH);
  }
  if(Message == 'b')
  {
    Serial.println("off");
    digitalWrite(RELAY_CTL_PIN, LOW);
  }
}
