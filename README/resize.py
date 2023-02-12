import cv2
import os

def show(m):
    cv2.imshow('z', m)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def resize(m, p):
    a, b, c = m.shape
    a, b = int(a * p), int(b * p)
    m = cv2.resize(m, (b, a))
    return m

for each in os.listdir():
    if each.endswith('.jpg') or each.endswith('.png'):
        m = cv2.imread(each, 1)
        
        m = resize(m, 0.25)
        # show(m)

        cv2.imwrite(each, m)

        
