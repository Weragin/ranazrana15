import tkinter as tk


def display_colored(root: tk.Tk,
                    character: str,
                    colors: list,
                    index: int
                    ) -> None:
    """
    Displays a character to the GUI in a color
    :param character: character to print
    :param colors: list of color to choose from
    :param index: index of the color to choose

    :return: None
    """
    pass


def parser(text: str):
    index = 0
    color_indeces = []
    for character in text:
        if character == '(':
            color_indeces.append(index)
            index = (index + 1)%7
    return color_indeces


def displayer(canvas: tk.Canvas,
              text: str,
              colors: list,
              color_indeces: list
             ) -> None:
    color_stack = []
    number_of_chars = 0
    for character in text:
        if character == '(':
            color = colors[color_indeces.pop(0)]
            color_stack.append(color)
            canvas.create_text(10 + number_of_chars*10, 10, text=character, fill=color)
        if character == ")":
            try:
                canvas.create_text(10 + number_of_chars*10, 10, text=character, fill=color_stack.pop())
            except IndexError:
                canvas.delete("all")
                canvas.create_text(10, 10, text="WRONG!!")
                return
        else:
            canvas.create_text(10 + number_of_chars*10, 10, text=character)
        number_of_chars += 1
            

def main(canvas: tk.Canvas) -> None:
    global COLORS
    text = input("Write text: ")
    color_indeces = parser(text)
    print(color_indeces)
    displayer(canvas, text, COLORS, color_indeces)


COLORS = ["red", "green", "blue", "yellow", "orange", "purple", "black", "white"]

root = tk.Tk()
root.title("Color Print")
root.geometry("500x50")

canvas = tk.Canvas(root, width=500, height=50)
canvas.pack()

main(canvas)

root.mainloop()

