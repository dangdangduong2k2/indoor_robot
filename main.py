#import thư viện
import pygame,sys
import serial
import pyfirmata
from button import Button
from time import sleep

#khởi tạo của sổ
pygame.init()

#giao tiếp giữa máy tính và xe qua bluetooth
robot = serial.Serial("COM8", 9600)

#giao tiếp giữa máy tính và cảm biến hồng ngoại ở các điểm:
    #khai báo cổng và các chân tín hiệu trên uno
board = pyfirmata.Arduino('COM5')
it = pyfirmata.util.Iterator(board)
it.start()
inp0 = board.get_pin('d:8:i')
inp1 = board.get_pin('d:9:i')
inp2 = board.get_pin('d:10:i')
inp3 = board.get_pin('d:11:i')
inp4 = board.get_pin('d:12:i')


#cài đặt thông số kích thước cho cửa sổ phần mềm
window = pygame.display.set_mode((700,400))  

#load ảnh, sửa size
bg  = pygame.image.load("bg.png")
bg  = pygame.transform.scale(bg, (700,400))

car = pygame.image.load("car.png")
car = pygame.transform.scale(car, (40, 40))
car = pygame.transform.rotate(car, 90)

#lấy font chữ bằng hàm sysfont
def get_font(size): 
    return pygame.font.SysFont(None,size)

#biến để chạy vòng lặp 1 = True
run = 1

#Vòng lặp*****
while run:
    signal0 = inp0.read()
    signal1 = inp1.read()
    signal2 = inp2.read()
    signal3 = inp3.read()
    signal4 = inp4.read()
    #lấy tọa độ con trỏ chuột
    MOUSE_POS = pygame.mouse.get_pos()

    #vòng for lấy các giá trị của click chuột để gửi lệnh cho xe 
    for event in pygame.event.get():

        #click vào biểu tượng quit = tắt hết chương trình 
        if event.type == pygame.QUIT:
            run = 0
            sys.exit()
        
    #cài đặt ảnh nền và tọa độ
    window.blit(bg, (0, 0))          

    #khởi tạo nút nhấn bằng Button và vẽ nó lên bằng Update
    BUTTON_0 = Button(image=car, pos=(90, 210), 
                            text_input="RUN", font=get_font(20), base_color="#d7fcd4", hovering_color="Red")
    BUTTON_0.update(window)

    if BUTTON_0.checkForInput(MOUSE_POS):
        robot.write(b'n')
    if signal0 is False:
        robot.write(b's')

    BUTTON_1 = Button(image=car, pos=(220, 132), 
                            text_input="RUN", font=get_font(20), base_color="#d7fcd4", hovering_color="Red")
    BUTTON_1.update(window)

    if BUTTON_1.checkForInput(MOUSE_POS):
        robot.write(b'n')
    if signal1 is False:
        robot.write(b's')

    BUTTON_2 = Button(image=car, pos=(460, 82), 
                            text_input="RUN", font=get_font(20), base_color="#d7fcd4", hovering_color="Red")
    BUTTON_2.update(window)

    if BUTTON_2.checkForInput(MOUSE_POS):
        robot.write(b'n')
    if signal2 is False:
        robot.write(b's')

    BUTTON_3 = Button(image=car, pos=(560, 200), 
                            text_input="RUN", font=get_font(20), base_color="#d7fcd4", hovering_color="Red")
    BUTTON_3.update(window)

    if BUTTON_3.checkForInput(MOUSE_POS):
        robot.write(b'n')
    if signal3 is False:
        robot.write(b's')
    

    BUTTON_4 = Button(image=car, pos=(425, 320), 
                            text_input="RUN", font=get_font(20), base_color="#d7fcd4", hovering_color="Red")
    BUTTON_4.update(window)

    #code tới đâu chạy code thì hiển thị tới đó
    pygame.display.update() 

