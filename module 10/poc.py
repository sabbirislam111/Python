# computer vision
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    cv2.imshow("output", frame)

    if cv2.waitKey(10)  == ord('q'):
        break

# kaj ses howar pore reslese kore felte hobe
cap.release()
cv2.destroyAllWindows()