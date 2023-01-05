
int rightMotor1 = 5;                
int rightMotor2 = 6;
int leftMotor1 = 2;                
int leftMotor2 = 3;

const int L_S =52;  
const int S_S =50;  
const int R_S =44;

const int trig = 10;
const int echo = 11;
const int led1 = 13;
const int led2 = 12;

int left_sensor_state;
int s_sensor_state;   
int right_sensor_state;

unsigned long thoigian;
int khoangcach;

byte command;

void setup() {
  // Set pin modes
  pinMode(rightMotor1, OUTPUT);
  pinMode(rightMotor2, OUTPUT);
  pinMode(leftMotor1, OUTPUT);
  pinMode(leftMotor2, OUTPUT);
  pinMode(L_S,INPUT);
  pinMode(R_S,INPUT);
  pinMode(S_S,INPUT);
  pinMode(trig, OUTPUT); 
  pinMode(echo, INPUT); 
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(led2,HIGH);
 
  
  left_sensor_state = digitalRead(L_S);
  s_sensor_state = digitalRead(S_S);
  right_sensor_state = digitalRead(R_S);

  digitalWrite(trig,0); 
  delayMicroseconds(2); 
  digitalWrite(trig,1); 
  delayMicroseconds(10); 
  digitalWrite(trig,0);
  
  thoigian = pulseIn (echo, HIGH);

  khoangcach = int (thoigian / 2 / 29.412); 

  if (khoangcach<10){
    digitalWrite(led1,HIGH);
  }
  if (khoangcach>10){
    digitalWrite(led1,LOW);
  }


  command = Serial.read();
  if ((command == 'n') && (khoangcach>10)){n();}
  if ((command == 'n') && (khoangcach<10))){s();}
  if ((command == 's')){s();}
 
}
void n(){
  if ((digitalRead(L_S) == 0)&&(digitalRead(S_S) == 1)&&(digitalRead(R_S) == 0)){f();}// đi tiến

  if ((digitalRead(L_S) == 1)&&(digitalRead(S_S) == 1)&&(digitalRead(R_S) == 0)){l();} // rẻ trái
  if ((digitalRead(L_S) == 1)&&(digitalRead(S_S) ==0)&&(digitalRead(R_S) == 0)) {l();} // rẻ trái

  if ((digitalRead(L_S) == 0)&&(digitalRead(S_S) == 1)&&(digitalRead(R_S) == 1)){r();} // rẻ phải
  if ((digitalRead(L_S) == 0)&&(digitalRead(S_S) == 0)&&(digitalRead(R_S) == 1)){r();}// rẻ phải

  if ((digitalRead(L_S) == 1)&&(digitalRead(S_S) == 1)&&(digitalRead(R_S) == 1)){s();}// dung
  
}

void f(){
    // forward motion
    digitalWrite(rightMotor1, HIGH);
    digitalWrite(rightMotor2, LOW);
    digitalWrite(leftMotor1, HIGH);
    digitalWrite(leftMotor2, LOW);
  }
void b(){
    // Backward motion
    digitalWrite(rightMotor1, LOW);
    digitalWrite(rightMotor2, HIGH);
    digitalWrite(leftMotor1, LOW);
    digitalWrite(leftMotor2, HIGH);
  }

void r(){
    // Right turn
    digitalWrite(rightMotor1, LOW);
    digitalWrite(rightMotor2, HIGH);
    digitalWrite(leftMotor1, HIGH);
    digitalWrite(leftMotor2, LOW);
  }

void l(){
    // Left turn
    digitalWrite(rightMotor1, HIGH);
    digitalWrite(rightMotor2, LOW);
    digitalWrite(leftMotor1, LOW);
    digitalWrite(leftMotor2, HIGH);
  }

void s(){
    // Stops the robot/car
    digitalWrite(rightMotor1, LOW);
    digitalWrite(rightMotor2, LOW);
    digitalWrite(leftMotor1, LOW);
    digitalWrite(leftMotor2, LOW);
  }
