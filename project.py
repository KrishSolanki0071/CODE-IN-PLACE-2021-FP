"""
This is my Final Project of Stanford's Code In Place 2021
i.e 'Multi-Filter of Images'
Have Fun Using it!
"""

from simpleimage import SimpleImage

def darker(image):
    """
    
    This filter will make the image darker in comparision to the
    original image

    """
    # Demonstrate looping over all the pixels of an image,
    # changing each pixel to be half its original intensity.
    for pixel in image:
        pixel.red = pixel.red // 2
        pixel.green = pixel.green // 2
        pixel.blue = pixel.blue // 2




def red_screen(filename):
    """
    Changes the image as follows:
    Sets green and blue values' pixel to 0
    """
    image = SimpleImage(filename)
    for pixel in image:
        pixel.green = 0
        pixel.blue = 0
    return image




def luminosity_formula(red, green, blue):
    """
    Calculates the luminosity of a pixel using NTSC formula
    to weight red, green, and blue values.
    """
    return (0.299 * red) + (0.587 * green) + (0.114 * blue)




def grayscale(filename):
    """
    Change the image to be grayscale using the NTSC
    luminosity formula.
    """
    image = SimpleImage(filename)
    for pixel in image:
        luminosity = luminosity_formula(pixel.red, pixel.green, pixel.blue)
        pixel.red = luminosity
        pixel.green = luminosity
        pixel.blue = luminosity
    return image




def blue_screen(filename):
    """
    Changes the image as follows:
    Sets red and green values' pixel to 0
    """
    image = SimpleImage(filename)
    for pixel in image:
        pixel.red = 0
        pixel.green = 0
    return image




def green_screen(filename):
    """
    Changes the image as follows:
    Sets red and blue values' pixel to 0
    """
    image = SimpleImage(filename)
    for pixel in image:
        pixel.red = 0
        pixel.blue = 0
    return image



def contrast(filename):
    """"
    This Filter wil increase the pixels 
    brightness dynamically
    """
    image= SimpleImage(filename)
    for pixel in image:
        pixel.red = pixel.red * 0.7
        pixel.green = pixel.green * 1.5
        pixel.blue = pixel.blue * 1.5
    return image



def brightness(filename):
    """"
    This Filter wil increase the pixels 
    brightness dynamically
    """
    image= SimpleImage(filename)
    for pixel in image:
        pixel.red = pixel.red * 4.0
        pixel.green = pixel.green * 4.0
        pixel.blue = pixel.blue * 4.0
    return image



def brightnessN(filename):
    """"
    This Filter wil increase the pixels 
    brightness dynamically
    """
    image= SimpleImage(filename)
    for pixel in image:
        pixel.red = pixel.red * 2.5
        pixel.blue = pixel.green * 2.5
        pixel.green = pixel.blue * 2.5
    return image



def first_choice():
    """
 This Function will print the output by using the First filter by
 making the given image DARKER!
    """   
    print("Here is the original picture before applying your desired filter")
    simpsons = SimpleImage('the simpsons.jpg')
    simpsons.show()
    print("Now, here is the Picture with your Desired Filter!")
    darker(simpsons)
    simpsons.show()




def sec_choice():
    """
This Function will print the output by using the Second filter by
making the given image RED!
    """
    print("Here is the original picture before applying your desired filter")
    simpsons = SimpleImage('the simpsons.jpg')
    simpsons.show()
    print("Now, here is the Picture with your Desired Filter!")
    red_simpsons= red_screen('the simpsons.jpg')
    red_simpsons.show()




def third_choice():
    """
This Function will print the output by using the First filter by
making the given image GRAYSCALE!
    """
    print("Here is the original picture before applying your desired filter")
    simpsons = SimpleImage('the simpsons.jpg')
    simpsons.show()
    print("Now, here is the Picture with your Desired Filter!")
    grayscale_simpsons = grayscale('the simpsons.jpg')
    grayscale_simpsons.show()




def fourth_choice():
    """
    This Function will print the output by using the Fourth filter by
    making the given image BLUE!
    """
    print("Here is the original picture before applying your desired filter")
    simpsons = SimpleImage('the simpsons.jpg')
    simpsons.show()
    print("Now, here is the Picture with your Desired Filter!")
    blue_simpsons= blue_screen('the simpsons.jpg')
    blue_simpsons.show()




def fifth_choice():
    """
    This Function will print the output by using the Fifth filter by
    making the given image GREEN!
    """
    print("Here is the original picture before applying your desired filter")
    simpsons = SimpleImage('the simpsons.jpg')
    simpsons.show()
    print("Now, here is the Picture with your Desired Filter!")
    green_simpsons= green_screen('the simpsons.jpg')
    green_simpsons.show()




def sixth_choice():
    """
    This Function will print the output by using the Sixth filter by
    increasing the contrast of each pixel dynamically!
    """
    print("Here is the original picture before applying your desired filter")
    simpsons = SimpleImage('the simpsons.jpg')
    simpsons.show()
    print("Now, here is the Picture with your Desired Filter!")
    contrast_simpsons= contrast('the simpsons.jpg')
    contrast_simpsons.show()



def seventh_choice():
    """
    This Function will print the output by using the Seventh filter by
    increasing the brightness of the picture!
    """
    print("Here is the original picture before applying your desired filter")
    simpsons = SimpleImage('the simpsons.jpg')
    simpsons.show()
    print("Now, here is the Picture with your Desired Filter!")
    brightness_simpsons= brightness('the simpsons.jpg')
    brightness_simpsons.show()




def eighth_choice():
    """
    This Function will print the output by using the Eighth filter by
    increasing the brightness negatively!
    """
    print("Here is the original picture before applying your desired filter")
    simpsons = SimpleImage('the simpsons.jpg')
    simpsons.show()
    print("Now, here is the Picture with your Desired Filter!")
    brightnessN_simpsons= brightnessN('the simpsons.jpg')
    brightnessN_simpsons.show()





def ninth_choice():
    print("\t \t \t \t \t \tTHANK YOU FOR USING THE ONLINE IMAGE FILTER! And have a nice day :) ")






def main():
    """
    The main function will display the menu and the desired choice will bring
    the interpreter to the desired filter's function and display the filtered image!
    """
  
    
    print("\t \t \t \t \t \t WELCOME TO THE MULTI-FILTER OF IMAGES!\n \nHERE ARE YOUR OPTIONS:")
    print("Press 1 for making the image DARKER")
    print("Press 2 for making the image RED")
    print("Press 3 for making the image GREYSCALE")
    print("Press 4 for making the image BLUE")
    print("Press 5 for making the image GREEN")
    print("Press 6 to increase the contrast of each pixel dynamically")
    print("Press 7 to increase the brightness of the picture")
    print("Press 8 to increase the brightness of each pixel negatively")
    print("Press 9 to END")
    choice = int(input("Enter your CHOICE:"))
    if(choice == 1):
        first_choice()
        print("\t \t \t \t \t \t \tTHANK YOU FOR USING THE ONLINE IMAGE FILTER! And have a nice day :) ")
    elif(choice == 2):
        sec_choice()
        print("\t \t \t \t \t \t \tTHANK YOU FOR USING THE ONLINE IMAGE FILTER! And have a nice day :) ")
    elif(choice == 3):
        third_choice()
        print("\t \t \t \t \t \t \tTHANK YOU FOR USING THE ONLINE IMAGE FILTER! And have a nice day :) ")
    elif(choice == 4):
        fourth_choice()
        print("\t \t \t \t \t \tTHANK YOU FOR USING THE ONLINE IMAGE FILTER! And have a nice day :) ")
    elif(choice == 5):
        fifth_choice()
        print("\t \t \t \t \t \tTHANK YOU FOR USING THE ONLINE IMAGE FILTER! And have a nice day :) ")
    elif(choice == 6):
        sixth_choice()
        print("\t \t \t \t \t \tTHANK YOU FOR USING THE ONLINE IMAGE FILTER! And have a nice day :) ")
    elif(choice == 7):
        seventh_choice()
        print("\t \t \t \t \t \tTHANK YOU FOR USING THE ONLINE IMAGE FILTER! And have a nice day :) ")
    elif(choice == 8):
        eighth_choice()
        print("\t \t \t \t \t \tTHANK YOU FOR USING THE ONLINE IMAGE FILTER! And have a nice day :) ")
    elif(choice == 9):
        ninth_choice()
    else:
        print("You entered an invalid input!")
    
            





if __name__ == '__main__':
    main()