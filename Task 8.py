#Q1. a python class called circle with constructor which will take a List as an argument for the task. The list is [10, 501, 22, 37, 100, 999, 87, 351]. #

class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list

radius = [10, 501, 22, 37, 100, 999, 87, 351]
my_circle = Circle(radius)

# Accessing the list within the Circle class
print("Radius values within the Circle class:", my_circle.radius_list)

#Output- Radius values within the Circle class: [10, 501, 22, 37, 100, 999, 87, 351]


#Q2. proper member variables inside the task if required and use them when necessary. For example for this task create a class private variable named pi= 3.141. #

class Circle:
    pi = 3.141  # Private class variable

    def __init__(self, radius_list):
        self.radius_list = radius_list

    def __area__(self, radius):
        return Circle.pi * radius**2

radius = [10, 501, 22, 37, 100, 999, 87, 351]
my_circle = Circle(radius)

# Accessing and printing the list within the Circle class
print("Radius values within the Circle class:", my_circle.radius_list)

# Calculating and printing the areas for each radius
for radius in my_circle.radius_list:
    area = my_circle.__area__(radius)
    print(f"Area of a circle with radius {radius}: {area}")

#Output- Area of a circle with radius 10: 314.1, Area of a circle with radius 501: 788394.1410000001, Area of a circle with radius 22: 1520.244, Area of a circle with radius 37: 4300.029, Area of a circle with radius 100: 31410.0, Area of a circle with radius 999: 3134721.141, Area of a circle with radius 87: 23774.229, Area of a circle with radius 351: 386974.341
    

#Q3. the given List create two class Methods Area and perimeter which will be going to calculate the Area and Perimeter. #
    
class Circle:
    pi= 3.14

    def __init__(self, radius_list):
        self.radius_list = radius_list
    
    def __area__(self, radius):
        return Circle.pi * radius**2
    
    def __perimeter__(self, radius):
        return 2 * Circle.pi * radius

radius = [10, 501, 22, 37, 100, 999, 87, 351]
my_circle = Circle(radius)

# Calculating and printing the area and perimeter for each radius
for radius in my_circle.radius_list:
    area = my_circle.__area__(radius)
    perimeter = my_circle.__perimeter__(radius)
    print(f"Radius: {radius}, Area: {area}, Perimeter: {perimeter}")

#Output- Radius: 10, Area: 314.0, Perimeter: 62.800000000000004; Radius: 501, Area: 788143.14, Perimeter: 3146.28; Radius: 22, Area: 1519.76, Perimeter: 138.16; Radius: 37, Area: 4298.66, Perimeter: 232.36; Radius: 100, Area: 31400.0, Perimeter: 628.0; Radius: 999, Area: 3133723.14, Perimeter: 6273.72; Radius: 87, Area: 23766.66, Perimeter: 546.36; Radius: 351, Area: 386851.14, Perimeter: 2204.28
    

#Q4. Part A) visit the URL and convert the UML diagram into a Python class #
    
class TV:
    def __init__(self, brand, price, inches):
        self.brand= brand
        self.price= price
        self.inches= inches
        self.channel= 1
        self.volume = 50
        self.on_off = False  # TV is initially turned off

    def increase_volume(self):
        #Increase the volume if the TV is on
        if self.on_off:
            self.volume = min(self.volume + 1, 100)

    def decrease_volume(self):
        #Decrease the volume if the TV is on
        if self.on_off:
            self.volume = max(self.volume - 1, 0)

    def set_channel(self, new_channel):
        #Set the channel within the valid range if the TV is on
        if self.on_off:
            self.channel = min(max(new_channel, 1), 50)

    def reset_tv(self):
        #Reset the TV to default settings
        self.channel = 1
        self.volume = 50

    def power(self):
        self.on_off = not self.on_off
        if not self.on_off:
            self.reset_tv()

    def __str__(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"

class Panasonic(TV):
     def __init__(self, brand= 'Panasonic', price= 0, inches=0):
        # Call the __init__ method of the parent class (TV)
        super().__init__(brand, price, inches)
        self.brand= 'Panasonic'
        self.channel= 8
        self.volume= 75 

panasonic_tv = Panasonic()
# Display the status of the TV 
print(panasonic_tv)

#Output- Panasonic at channel 8, volume 75.



#Q4. Part B) visit the URL and convert the UML diagram into a Python class #

class LEDTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        # Call the __init__ method of the parent class (TV)
        super().__init__(brand, price, inches)
        # Initialize additional properties specific to LEDTV
        self.screen_thickness= screen_thickness
        self.energy_usage= energy_usage
        self.lifespan= lifespan
        self.refresh_rate= refresh_rate
        self.viewing_angle = None
        self.backlight = None
        self.display_details = None

    def set_display_details(self, viewing_angle, backlight, display_details):
        #Set the display details of the LEDTV
        self.viewing_angle = viewing_angle
        self.backlight = backlight
        self.display_details = display_details

    def get_detailed_features(self):
        #Get a detailed feature description of the LEDTV
        return f"{self.brand} - {self.inches}\" LED TV\n" \
               f"Price: ${self.price}\n" \
               f"Screen Thickness: {self.screen_thickness}\n" \
               f"Energy Usage: {self.energy_usage}\n" \
               f"Lifespan: {self.lifespan} years\n" \
               f"Refresh Rate: {self.refresh_rate} Hz\n" \
               f"Viewing Angle: {self.viewing_angle}\n" \
               f"Backlight: {self.backlight}\n" \
               f"Display Details: {self.display_details}"
    
led_tv = LEDTV('Panasonic', 240, 30, 'Ultra-thin', 'Low', 10, 150)
led_tv.set_display_details('Wide', 'LED', '4K')
print(led_tv.get_detailed_features())

#Output- Panasonic - 30" LED TV; Price: $240; Screen Thickness: Ultra-thin; Energy Usage: Low; Lifespan: 10 years; Refresh Rate: 150 Hz; Viewing Angle: Wide; Backlight: LED; Display Details: 4K.

