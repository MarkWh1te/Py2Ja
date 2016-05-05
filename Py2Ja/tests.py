import os
path = os.getcwd()
print path

image_name = "77ca319c46128791609727b0fd061b97"
username = "SummyChou" 
os.rename(path+"/media/cropped_avatars/%s-40.jpeg" % image_name,
          path+"/media/cropped_avatars/%s-40.jpeg" % username)
os.rename(path+"/media/cropped_avatars/%s-120.jpeg" % image_name,
          path+"/media/cropped_avatars/%s-120.jpeg" % username)
