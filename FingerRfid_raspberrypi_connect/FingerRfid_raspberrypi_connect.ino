#include <SPI.h>
#include <MFRC522.h>
#include <Adafruit_Fingerprint.h>

#define SS_PIN 10   //SS 핀 설정
#define RST_PIN 9   //RST 핀 설정

MFRC522 rfid(SS_PIN, RST_PIN);  //클래스 객체 선언
SoftwareSerial mySerial(2, 3);

Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);

void setup() {
  Serial.begin(9600);
  //rfid
  SPI.begin();      //SPI 통신 시작
  rfid.PCD_Init();  //RFID 초기화

  //finger
  while (!Serial);
  delay(100);
  finger.begin(57600);
  delay(5);
  if (finger.verifyPassword()) {
  } else {
    while (1) {
      delay(1);
    }
  }

  finger.getTemplateCount();
}

void loop() {
  //finger
  getFingerprintIDez();

  //rfid
  //새 카드가 인식되면 넘어감
  if (! rfid.PICC_IsNewCardPresent())
    return;
  //카드가 제대로 읽혀지면 넘어감
  if (!rfid.PICC_ReadCardSerial())
    return;

  //현재 접촉되는 카드 타입 읽어오기
  String content = "";
  byte letter;
  for (byte i = 0; i < rfid.uid.size; i++)
  {
    content.concat(String(rfid.uid.uidByte[i] < 0x10 ? " 0" : " "));
    content.concat(String(rfid.uid.uidByte[i], HEX));
  }

  content.toUpperCase();

  //UID값이 지정해 둔 값과 같으면 출입 가능
  if (content.substring(1) == "21 CE 50 D3") //key1
  {
    same();
  }

  //UID값이 다르면 출입금지
  else
  {
    notsame();
  }
}

//rfid
//출입가능 함수 선언
void same() {
  Serial.println("1");
  delay(500);
}

//출입불가능 함수 선언
void notsame() {
  Serial.println("0");
  delay(500);
}


//finger
uint8_t getFingerprintID() {
  uint8_t p = finger.getImage();
  switch (p) {
    case FINGERPRINT_OK:
      break;
    case FINGERPRINT_NOFINGER:
      return p;
    case FINGERPRINT_PACKETRECIEVEERR:
      return p;
    case FINGERPRINT_IMAGEFAIL:
      return p;
    default:
      return p;
  }

  // OK success!

  p = finger.image2Tz();
  switch (p) {
    case FINGERPRINT_OK:
      break;
    case FINGERPRINT_IMAGEMESS:
      return p;
    case FINGERPRINT_PACKETRECIEVEERR:
      return p;
    case FINGERPRINT_FEATUREFAIL:
      return p;
    case FINGERPRINT_INVALIDIMAGE:
      return p;
    default:
      return p;
  }

  // OK converted!
  p = finger.fingerFastSearch();
  if (p == FINGERPRINT_OK) {
  } else if (p == FINGERPRINT_PACKETRECIEVEERR) {
    return p;
  } else if (p == FINGERPRINT_NOTFOUND) {
    return p;
  } else {
    return p;
  }

  return finger.fingerID;
}

// returns -1 if failed, otherwise returns ID #
int getFingerprintIDez() {
  uint8_t p = finger.getImage();
  if (p != FINGERPRINT_OK)  {
    return -1;
  }

  p = finger.image2Tz();
  if (p != FINGERPRINT_OK) {
    return -1;
  }

  p = finger.fingerFastSearch();
  if (finger.confidence < 100) {
  }
   printID();
}

void printID() {
  if (finger.fingerID == 1) {
    Serial.println("K_EUNJIN2013");
    delay(5000);
    }
  else if (finger.fingerID == 2) {
    Serial.println("0l0jjo");
    delay(5000);
    }
  else if (finger.fingerID == 3) {
    Serial.println("BBOGGO");
    delay(5000);
    }
  else if (finger.fingerID == 4) {
    Serial.println("17__APR");
    delay(5000);
    }
  return finger.fingerID;
}
