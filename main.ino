#include <DHT.h>

#define BUTTON_P 13
#define BUTTON_K 12
#define LDR_PIN 34
#define DHT_PIN 27
#define RELAY_PIN 14

DHT dht(DHT_PIN, DHT22);

void setup() {
  Serial.begin(9600);
  pinMode(BUTTON_P, INPUT_PULLUP);
  pinMode(BUTTON_K, INPUT_PULLUP);
  pinMode(RELAY_PIN, OUTPUT);
  dht.begin();
}

void loop() {
  // Leitura dos sensores
  bool hasPhosphorus = !digitalRead(BUTTON_P);
  bool hasPotassium = !digitalRead(BUTTON_K);
  int phRaw = analogRead(LDR_PIN);
  float humidity = dht.readHumidity();

  // Conversão analógica (simulando pH)
  float ph = map(phRaw, 0, 4095, 0, 14);

  // Exibição dos valores
  Serial.print("P: "); Serial.print(hasPhosphorus ? "Sim" : "Não");
  Serial.print(" | K: "); Serial.print(hasPotassium ? "Sim" : "Não");
  Serial.print(" | pH: "); Serial.print(ph);
  Serial.print(" | Umidade: "); Serial.print(humidity); Serial.println("%");

  // Lógica de irrigação
  if (humidity < 40 || !hasPhosphorus || !hasPotassium || ph < 5 || ph > 7) {
    digitalWrite(RELAY_PIN, HIGH); // Liga bomba
    Serial.println("Bomba: Ligada");
  } else {
    digitalWrite(RELAY_PIN, LOW); // Desliga bomba
    Serial.println("Bomba: Desligada");
  }

  delay(5000); // Intervalo entre leituras
}
