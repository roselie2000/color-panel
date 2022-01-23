import tkinter as tk


root = tk.Tk()
root.title('Color Theme')
root.geometry('525x600')
root.resizable(0,0)
input_frame = tk.LabelFrame(root, padx=5, pady=5, bg='white')
radio_frame = tk.LabelFrame(root, padx=5, pady=5, bg='white')
input_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
radio_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

def get_red(slider_value):
    global red_value
    red_value = hex(int(slider_value))
    red_value = red_value.lstrip("0x")
    while len(red_value) < 2:
        red_value = "0" + str(red_value)
    update_color()

def get_green(slider_value):
    global green_value
    green_value = hex(int(slider_value))
    green_value = green_value.lstrip("0x")
    while len(green_value) < 2:
        green_value = "0" + str(green_value)
    update_color()

def get_blue(slider_value):
    global blue_value
    blue_value = hex(int(slider_value))
    blue_value = blue_value.lstrip("0x")
    while len(blue_value) < 2:
        blue_value = "0" + str(blue_value)
    update_color()

def update_color():
    color_box = tk.Label(input_frame, bg='#'+ red_value + green_value + blue_value, height=6, width=15)
    color_box.grid(row=1, column=3, columnspan=2, padx=35, pady=10)

    color_tuple.config(text='(' + str(red_slider.get()) + ')'+'(' + str(green_slider.get()) + ')'+'(' + str(blue_slider.get()) + ')')
    color_hex.config(text='#' + red_value + green_value + blue_value)

def set_color(r,g,b):
    red_slider.set(r)
    green_slider.set(g)
    blue_slider.set(b)

def store_color():
    global stored_colors
    red = str(red_slider.get())
    while len(red) < 3:
        red = '0' + red
    green = str(green_slider.get())
    while len(green) < 3:
        green = '0' + green
    blue = str(blue_slider.get())
    while len(blue) < 3:
        blue = '0' + blue
    stored_red = red_slider.get()
    stored_green = green_slider.get()
    stored_blue = blue_slider.get()
    recall_button = tk.Button(radio_frame, text="Recall Color",bg='gray', command=lambda:set_color(stored_red,stored_green,stored_blue))
    new_color_tuple = tk.Label(radio_frame, text='(' + red + ')'+'(' + green + ')'+'(' + blue + ')', bg='white')
    new_color_hex = tk.Label(radio_frame, text='#' + red_value + green_value + blue_value, bg='white')
    new_black_box = tk.Label(radio_frame, bg='black', width=3, height=1)
    new_white_box = tk.Label(radio_frame, bg='#' + red_value + green_value + blue_value, width=3, height=1)

    recall_button.grid(row=stored_color.get(), column=1, padx=20)
    new_color_tuple.grid(row=stored_color.get(), column=2, padx=20)
    new_color_hex.grid(row=stored_color.get(), column=3, padx=20)
    new_black_box.grid(row=stored_color.get(), column=4, pady=2, ipadx=5, ipady=5)
    new_white_box.grid(row=stored_color.get(), column=4)

    stored_colors[str(stored_color.get())] = [new_color_tuple.cget("text"), new_color_hex.cget("text")]

    if stored_color.get() < 5:
        stored_color.set(stored_color.get()+1)

#create widgets
red_label = tk.Label(input_frame, text="R", bg='white', fg='red')
red_slider = tk.Scale(input_frame, from_=0, to=255,bg='white', command=get_red)
red_button = tk.Button(input_frame, text="Red",bg='red', command=lambda :set_color(255,0,0))
red_label.grid(row=0, column=0, sticky='w')
red_slider.grid(row=1, column=0, sticky='w')
red_button.grid(row=2, column=0, padx=1, pady=1, ipadx=20)

green_label = tk.Label(input_frame, text="G", bg='white', fg='green')
green_slider = tk.Scale(input_frame, from_=0, to=255, bg='white', command=get_green)
green_button = tk.Button(input_frame, text="Green",bg='green', command=lambda:set_color(0,145,0))
green_label.grid(row=0, column=1, sticky='w')
green_slider.grid(row=1, column=1, sticky='w')
green_button.grid(row=2, column=1, padx=1, pady=1, ipadx=20)

blue_label = tk.Label(input_frame, text="B", bg='white', fg='blue')
blue_slider = tk.Scale(input_frame, from_=0, to=255,bg='white', command=get_blue)
blue_button = tk.Button(input_frame, text="Blue",bg='blue', command=lambda:set_color(0,0,145))
blue_label.grid(row=0, column=2, sticky='w')
blue_slider.grid(row=1, column=2, sticky='w')
blue_button.grid(row=2, column=2, padx=1, pady=1, ipadx=20)

yellow_button = tk.Button(input_frame, text="Yellow", bg='yellow', command=lambda:set_color(255,255,0))
gray_button = tk.Button(input_frame, text="Gray", bg='gray', command=lambda:set_color(128,128,128))
magenta_button = tk.Button(input_frame, text="Magenta", bg='magenta', command=lambda:set_color(255,0,255))
rosybrn_button = tk.Button(input_frame, text="Brown", bg='brown', command=lambda:set_color(150,75,0))
pink_button = tk.Button(input_frame, text="Pink", bg='pink', command=lambda:set_color(255,20,147))
indigo_button = tk.Button(input_frame, text="Indigo", bg='indigo', command=lambda:set_color(75,0,130))
teal_button = tk.Button(input_frame, text="Teal", bg='teal', command=lambda:set_color(0,120,120))
maroon_button = tk.Button(input_frame, text="Maroon", bg='maroon', command=lambda:set_color(128,0,0))
olive_button = tk.Button(input_frame, text="Olive", bg='olive', command=lambda:set_color(128,128,0))

yellow_button.grid(row=3, column=0,  padx=1, pady=1, sticky='we')
gray_button.grid(row=3, column=1, padx=1, pady=1, sticky='we')
magenta_button.grid(row=3, column=2, padx=1, pady=1, sticky='we')
rosybrn_button.grid(row=4, column=0, padx=1, pady=1, sticky='we')
pink_button.grid(row=4, column=1, padx=1, pady=1, sticky='we')
indigo_button.grid(row=4, column=2, padx=1, pady=1, sticky='we')
teal_button.grid(row=5, column=0, padx=1, pady=1, sticky='we')
maroon_button.grid(row=5, column=1, padx=1, pady=1, sticky='we')
olive_button.grid(row=5, column=2, padx=1, pady=1, sticky='we')

store_button = tk.Button(input_frame, text="Store Color", width=20,bg='gray', command=store_color)
quit_button = tk.Button(input_frame, text="Quit",bg='gray', command=root.destroy)
store_button.grid(row=6, column=0, columnspan=3, padx=1, pady=1, sticky='we')
quit_button.grid(row=7, column=0, columnspan=7, padx=1, pady=2, sticky='we')


color_box = tk.Label(input_frame, bg='black', height=6, width=15)
color_tuple = tk.Label(input_frame, text="(0), (0), (0)", bg='white')
color_hex = tk.Label(input_frame, text="#000000", bg='white')
color_box.grid(row=1, column=3, columnspan=2, padx=35, pady=10, ipadx=10, ipady=10)
color_tuple.grid(row=2, column=3, columnspan=2)
color_hex.grid(row=3, column=3, columnspan=2)

#radio Frame
stored_colors = {}
stored_color = tk.IntVar()

for i in range(6):
    radio = tk.Radiobutton(radio_frame, variable=stored_color, value=i, bg='white')
    radio.grid(row=i, column=0, sticky='w')

    recall_button = tk.Button(radio_frame, text="Recall color", state=tk.DISABLED, bg='gray')
    new_color_tuple = tk.Label(radio_frame, text="(255), (255), (255)", bg='white')
    new_color_hex = tk.Label(radio_frame, text="#ffffff", bg='white')
    new_black_box = tk.Label(radio_frame, bg="black", width=3, height=1)
    new_white_box = tk.Label(radio_frame, bg="white", width=3, height=1)

    recall_button.grid(row=i, column=1, padx=20)
    new_color_tuple.grid(row=i, column=2, padx=20)
    new_color_hex.grid(row=i, column=3, padx=20)
    new_black_box.grid(row=i, column=4, pady=2, ipadx=5, ipady=5)
    new_white_box.grid(row=i, column=4)

red_value = "00"
green_value = "00"
blue_value = "00"


root.mainloop()
