from tkinter import *
import requests


# function to pull in quotes from an API that houses a number of Kanye West quotes
def get_quote():
    kanye_data = requests.get("https://api.kanye.rest")
    # raise for status returns a HTTPError status if an error occurs when pulling in the data
    kanye_data.raise_for_status()
    # puts the text from the Kanye data variable (in json form) into the canvas created in the code below
    canvas.itemconfig(quote_text, text=kanye_data.json()["quote"])

# create a GUI using tkinter
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
# this GUI is using the grid system for the layout
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
# when the user clicks the Kanye icon, the command pulls in the get_quote function that is created above
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

# this allows the window to remain open
window.mainloop()

