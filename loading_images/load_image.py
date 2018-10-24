import cv2
import matplotlib.pyplot as plt


image= "smarties.jpg"


def load_images(file_path):
  
    img_color = cv2.imread(file_path, cv2.IMREAD_COLOR)           # load bgr
    img_alpha = cv2.imread(file_path, cv2.IMREAD_UNCHANGED) # load rgba
    img_gray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)  # load grayscale
    

    print('BGR shape: ', img_color.shape)        # Rows, columss, channels
    print ('ARGB shape:', img_alpha.shape)
    print ('Gray shape:', img_gray.shape)
    print ('img.dtype: ', img_color.dtype)
    print ('img.size: ', img_color.size)


    img_list = [img_color,img_alpha, img_gray]
    for i in img_list:
        cv2.imshow("Image-{}".format(i), i)
        cv2.waitKey(800)
    
        cv2.destroyAllWindows()
    



load_images(image)