import os
import imageio

file_lst = os.listdir("Assignment8/images")
file_lst.sort()
print(file_lst)

imgs = []

for file_name in  file_lst:
    file_path = "Assignment8/images/" + file_name
    image = imageio.imread(file_path)
    imgs.append(image)


imageio.mimsave("Assignment8/my_gif.gif",imgs, fps = 5)