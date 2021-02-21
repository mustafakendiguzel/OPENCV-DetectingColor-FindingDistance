

import cv2
import numpy as np

kam = cv2.VideoCapture(0)
foto = cv2.imread('resim.jpg')

def foto_cevirme(fotogir):
    hsv = cv2.cvtColor(fotogir,cv2.COLOR_BGR2HSV)

    fotogir = cv2.blur(fotogir,(3,3))


    lower_red = np.array([0,120,70])

    upper_red = np.array([10,255,255])

    mask1 = cv2.inRange(hsv, lower_red, upper_red)
  

    lower_red = np.array([170,120,70])

    upper_red = np.array([180,255,255])

    mask2 = cv2.inRange(hsv,lower_red,upper_red)


    mask1 = mask1+mask2
    (contours,hierarchy) = cv2.findContours(mask1.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
      if cv2.contourArea(c) < 500:
        continue
      (x,y,w,h) = cv2.boundingRect(c)
      cv2.rectangle(fotogir,(x,y),(x+w,y+h),(255,0,0),3)
      global face_width 
      face_width = w
    return face_width

    res1 = cv2.bitwise_and(fotogir,fotogir,mask=mask1)
    cv2.imshow("foto",fotogir)

known_distance = 40  
known_width = 20   
 
def focal_length(measured_distance, real_width, width_in_rf_image):
   focal_length = (width_in_rf_image * measured_distance)/ real_width
   return focal_length

def distance_finder(Focal_length,real_face_width,face_width_in_frame):
   distance = (real_face_width* Focal_length)/ face_width_in_frame 
   return distance


fotokare = foto_cevirme(foto) 
ref_image_face_width = fotokare
focal_length_found = focal_length(known_distance,known_width,ref_image_face_width)
fonts = cv2.FONT_HERSHEY_COMPLEX


while True:
  
  ret, goruntu = kam.read()


  hsv = cv2.cvtColor(goruntu,cv2.COLOR_BGR2HSV)

  goruntu = cv2.blur(goruntu,(3,3))


  lower_red = np.array([0,120,70])

  upper_red = np.array([10,255,255])

  mask1 = cv2.inRange(hsv, lower_red, upper_red)


  lower_red = np.array([170,120,70])

  upper_red = np.array([180,255,255])

  mask2 = cv2.inRange(hsv,lower_red,upper_red)

 
  mask1 = mask1+mask2
  (contours,hierarchy) = cv2.findContours(mask1.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
  for c in contours:
    if cv2.contourArea(c) < 500:
      continue
    (x,y,w,h) = cv2.boundingRect(c)
    cv2.rectangle(goruntu,(x,y),(x+w,y+h),(255,0,0),3)
    genis = w
    


  
  Distance = distance_finder(focal_length_found,known_width,genis)
  cv2.putText(goruntu,f"Distance = {Distance}",(50,50),fonts,1,(0,0,255),2)

  res1 = cv2.bitwise_and(goruntu,goruntu,mask=mask1)

  stackImages
  cv2.imshow("orj",goruntu)
  cv2.imshow("mask",mask1)
  cv2.imshow("res",res1)
  
  
  if cv2.waitKey(30) & 0xFF == ord('q'):
    break
    

kam.release()
cv2.destroyAllWindows()
