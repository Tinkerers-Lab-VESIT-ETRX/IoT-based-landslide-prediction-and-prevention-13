#define Moisture_Pin A0 
#define Vibration_Pin 2

void setup() {

pinMode (Moisture_Pin, INPUT);
pinMode (Vibration_Pin, INPUT);

Serial.begin(9600);
}
void loop()
{
float Moisture_Value = 0;
String Vibration = "NO";

float temp = analogRead (Moisture_Pin); 
Moisture_Value = (temp/1023)*100;

if(digitalRead (Vibration_Pin))
  Vibration = "YES";

Serial.println("Moisture :"+String (Moisture_Value) +",Vibration :"+ Vibration);

delay(500);
}
