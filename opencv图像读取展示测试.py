import os
import sys
import cv2

image = cv2.imread('C:\\Users\\qinfeng\\Desktop\\opencv_tabletext_ extraction\\img_table\\table1.jpg', 1)
print(type(image))

cv2.imshow('table1', image)
cv2.waitKey(0)                                # 按任意键退出
# while True:
#     if cv2.waitKey(0) == 32:                # 空格键
#         cv2.destroyAllWindows()
#         break

print('over')