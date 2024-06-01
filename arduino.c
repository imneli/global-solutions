#include <LiquidCrystal.h>

#define RED_LED 2
#define GREEN_LED 3

LiquidCrystal lcd(6, 7, 8, 9, 10, 11);
int sensor = 0;
float sensorValue;
float outputVoltage;
float temperature;
bool alertaEnviado = false;
int buzzPin = 13;

void setup() {
  Serial.begin(9600);
  Serial.println("O Arduino foi iniciado!");

  pinMode(RED_LED, OUTPUT);
  pinMode(GREEN_LED, OUTPUT);

  lcd.begin(16, 2);
}

void loop() {
  lcd.clear();

  sensorValue = analogRead(sensor);

  temperature = sensorValue / 1024;    //Saber a porcentagem da temperatura
  temperature *= 5;                    // Saber o valor da tensão
  temperature -= 0.5;                  //Retirar o deslocamento
  temperature *= 100;                  //Converter para graus Celsius
  
  int tempCerta = map(temperature, -40, 124,-10, 40);

  lcd.setCursor(2, 0);
  lcd.print("Temp. atual");
  lcd.setCursor(4, 2);
  lcd.print(tempCerta);
  lcd.print(" C");

  if (tempCerta >= 25 && !alertaEnviado) {
    Serial.println("Temperatura elevada, mandando alerta às Organizacoes!");
    lcd.setCursor(2, 0);
    lcd.print("Temp Elevada!");
    tone(buzzPin, 1000); 

    digitalWrite(RED_LED, HIGH);
    digitalWrite(GREEN_LED, LOW);

    alertaEnviado = true; // Definir a variável como verdadeira para indicar que o alerta foi enviado
  } else if (tempCerta < 25 && alertaEnviado) {
    
    noTone(buzzPin); 
 
    lcd.setCursor(2, 0);
    lcd.print("Temp Normal!");
   

    digitalWrite(GREEN_LED, HIGH);
    digitalWrite(RED_LED, LOW); // alterar o Led
    
    alertaEnviado = false; // Redefinir a variável como falsa para indicar que o alerta não foi mais enviado
  }

  delay(1000);
}

