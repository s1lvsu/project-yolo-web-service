from exif import Image

with open("CAT.JPG", "rb") as r_1_file:
    im1 = Image(r_1_file)

def dms_coordinates_to_dd_coordinates(coordinates, coordinates_ref):
    decimal_degrees = coordinates[0] + \
                      coordinates[1] / 60 + \
                      coordinates[2] / 3600
    
    if coordinates_ref == "S" or coordinates_ref == "W":
        decimal_degrees = -decimal_degrees
    
    return decimal_degrees

images = [im1]

for index, image in enumerate(images):
    if image.has_exif:
        if hasattr(image, 'gps_latitude') and hasattr(image, 'gps_longitude'):
            print(f"Coordinates - Image {index + 1}")
            print(f"Latitude (DD): {dms_coordinates_to_dd_coordinates(image.gps_latitude, image.gps_latitude_ref)}")
            print(f"Longitude (DD): {dms_coordinates_to_dd_coordinates(image.gps_longitude, image.gps_longitude_ref)}\n")
        else:
            status = "does not contain any gps information."
            print(f"Image {index + 1} {status}")
    else:
        status = "does not contain any EXIF information."
        print(f"Image {index + 1} {status}")