# from sketchpy import canvas
# import turtle as tur
# import datetime
# today1 = datetime.datetime.now()
# tur.hideturtle()
# tur.penup()

# # Center the turtle at the top of the window
# tur.goto(0, tur.getscreen().window_height() / 3- 7)
# # Set text color
# tur.color("red")
# tur.title("My Turtle") #<----change name
# message = "Anwar.\n\nToday is " + today1.strftime("%A") + ', ' + today1.strftime("%d") \
#         + ', ' + today1.strftime("%B") + ', ' + today1.strftime("%Y") 

# # Center the text
# tur.write(message, move=False, font=('arial', 12, 'bold'), align='center')

# # #sketching
# # obj=canvas.sketch_from_image('C:\\Users\\ADMIN\\Desktop\\python\\.png')
# # # obj=canvas.sketch_from_image('C:\\Users\\ADMIN\\Desktop\\python\\dho.jpg')
# # print("Hello")
# # obj.draw()

# # # from sketch import canvas
# o=canvas.sketch_from_image('C:\\Users\\ADMIN\\Desktop\\python\\Tarique-Anwar.png')
# o.draw()


# from sketchpy import canvas
# f=canvas.sketch_from_image('C:\\Users\\ADMIN\\Desktop\\python\\Tarique-Anwar.png')
# f.draw()


        #show only image

from PIL import Image, ImageDraw

# Load the image
image_path = 'C:\\Users\\ADMIN\\Desktop\\python\\Tarique-Anwar.png'
image = Image.open(image_path)

# Create a drawing object
draw = ImageDraw.Draw(image)

# Your drawing operations go here (e.g., draw.line(), draw.rectangle(), etc.)

# Save or display the modified image
image.show()
# or
# image.save('output_sketch.png')
# from sketchpy import canvas
# i=canvas.sketch_from_image("drive and image path")
# i.draw()
