'''
전체 틀 잡음
rfid는 정수로 0,1만 받아옴 -> if 1:열림, else: 안열림
finger는 이름으로 받아옴 -> if 등록한 이름이 뜨면:열리고 이름 출력, else:안열리고 Not admin
camera는 idnex로 처리 -> if 인식된 얼굴:열리고 이름 출력, else:안열리고 Not admin
'''

while True:
    index = ['bob', 'micle']
    rfid = int(input())

    # rfid
    if rfid == 1:
        print('rfid : open')
        print('rfid : welcome')
    else:
        print('rfid : getout')

    # finger
    finger = input()
    if finger == 'bob':
        print('finger : open')
        print('finger : hello bob')
    elif finger == 'mingzzi':
        print('finger : open')
        print('finger : hello mingzzi')
    else:
        print('finger : no open')
        print('finger : get out')
    camera = input()
    # camera for only bob
    for i in range(0, len(index)):
        if camera == index[i]:
            print('camera : hello ' + index[i])

