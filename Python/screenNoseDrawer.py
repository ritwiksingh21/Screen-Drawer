import cv2

def getFace(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(13,13),0)
    faces = faceCascade.detectMultiScale(imgBlur, 1.1,4)
    newPoints = []
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(50,255,0),4)
        cv2.line(img,((x+w//2)-10, y+(h+30)//2),((x+w//2)+10, y+(h+30)//2),(190,0,60),2)
        cv2.line(img,((x+w//2), (y+(h+30)//2)-10),((x+w//2), (y+(h+30)//2)+10),(190,0,60),2)
        cv2.putText(img,"TABLE",(x,y+h+20), cv2.FONT_HERSHEY_PLAIN,1.5,(70,255,0),2)
        if x!=0and y!=0:
            newPoints.append([x+w//2,y+(h+15)//2])
    return newPoints
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,90)
myPoints = []
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def drawOnCanvas(points):
    for point in points:
        cv2.circle(imgResult,(point[0],point[1]),6,(230,200,130),cv2.FILLED)
