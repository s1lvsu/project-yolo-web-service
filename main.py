from exif import Image

with open("PHOTO_1.JPG", "rb") as r_1_file:
    im1 = Image(r_1_file)

with open("PHOTO_2.JPG", "rb") as r_2_file:
    im2 = Image(r_2_file)
    
images = [im1, im2]

for index, image in enumerate(images):
    if image.has_exif:
        # for index, image in enumerate(images):
            print(f"Coordinates - Image {index + 1}")
            print(f"Latitude: {image.gps_latitude} {image.gps_latitude_ref}")
            print(f"Longitude: {image.gps_longitude} {image.gps_longitude_ref}\n")
    else:
        status = "does not contain any EXIF information."
        print(f"Image {index + 1} {status}")
