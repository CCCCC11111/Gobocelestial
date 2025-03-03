from manim import *
from Star import *
import struct
Stars = []
with open("PPM", "rb") as f:
        header_data = f.read(28)
        # Read the 28-byte header
        header_format = ">7i"
        unpacked= struct.unpack(header_format,header_data)
        print(unpacked)
        for i in range(378910):
                star_data= f.read(28)
                magnitude= struct.unpack(">h",star_data[18:20])[0]
                if magnitude<=560:
                    ascension= struct.unpack(">d",star_data[0:8])[0]
                    print("Ascension: ",ascension)
                    declination= struct.unpack(">d",star_data[8:16])[0]
                    print("Declination ",declination)
                    spectral_type= struct.unpack(">2c",star_data[16:18])
                    print("Spectral Type: ", spectral_type[0], spectral_type[1])
                    print("Magnitude: ",magnitude)
                    ascensionMotion= struct.unpack(">f",star_data[20:24])[0]
                    declinationMotion= struct.unpack(">f",star_data[24:28])[0]
                    Stars.append(Star(ascension,declination,spectral_type,magnitude,ascensionMotion,declinationMotion))
print(Stars[0].getpos())
print(len(Stars))
magnitudes=[]
for s in Stars:
  magnitudes.append(s.mag)
magnitudes.sort()
#print(magnitudes)
class CreateCircle(ThreeDScene):
    def construct(self):
        self.camera.light_source.set_x(0)
        self.camera.light_source.set_y(0)
        sky = Cylinder(3, 0.001, [1., 0., 0.], resolution=(4, 3))
        ecliptic = Circle(3)
        equator = Circle(3,WHITE)
        ecliptic.rotate_about_origin(23.44*DEGREES,RIGHT)
        circles=VGroup()
        '''
        circles.add(ecliptic)
        circles.add(equator)
        granularity_3d = 100
        for circle_3d in circles:
             circle_3d.pieces = VGroup(
                *circle_3d.get_pieces(granularity_3d)
            )
             circle_3d.add(circle_3d.pieces)
             circle_3d.set_stroke(width=0, family=False)
             circle_3d.set_shade_in_3d(True) 
        '''
             #self.add(circle_3d)
        sky.set_color("#19243A")
        for s in Stars:
              size= 0.02/(1.58489319246**(s.mag/100))
              if s.mag > 100:
                star = Dot3D(s.getpos(),size,resolution=(3, 2))
              else:
                star = Dot3D(s.getpos(),size,resolution=(4, 4))
              self.add(star)  # show the circle on screen
        self.add(sky)
        
        r=1.14239732858
        self.begin_ambient_camera_rotation(rate=r)
        def rotatesky(o):
            o.rotate_about_origin(r/60)
        sky.add_updater(rotatesky)
        self.set_camera_orientation(phi=90 * DEGREES, theta=0*DEGREES,gamma=0)
        self.wait(1)


