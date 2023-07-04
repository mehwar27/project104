import cv2


img = cv2.imread("solar-system.jpg")
cv2.imshow("Display Image",img)


text_to_show = "SUN"


cv2.putText(img,  
           text_to_show,
           (130, 120),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=1,  
           color=(0,0,255)
           )



cv2.imshow("output",img)


cv2.putText(img,  
           "Mercury",
           (120, 175),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )


cv2.imshow("output",img)


cv2.putText(img,  
           "Venus",
           (178, 258),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )


cv2.imshow("output",img)


cv2.putText(img,  
           "Earth",
           (280, 165),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,0,0)
           )


cv2.imshow("output",img)





cv2.putText(img,  
           "Mars",
           (380, 185),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )


cv2.imshow("output",img)

cv2.putText(img,  
           "Jupiter",
           (450, 70),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )


cv2.imshow("output",img)

cv2.putText(img,  
           "Saturn",
           (660, 135),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )



cv2.imshow("output",img)

cv2.putText(img,  
           "Uranus",
           (960, 120),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )


cv2.imshow("output",img)

cv2.putText(img,  
           "Neptune",
           (1080, 120), 
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )


cv2.imshow("output",img)







cv2.waitKey(0)

# python solar_planets.py