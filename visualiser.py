from tkinter import *
import ttkbootstrap as ttk
import random
from bubbleSort import bubble_sort
from quickSort import quick_sort
from bsearch import binarySearch
from mergeSort import merge_sort

ui = '#60A3D9'
button = '#003B73'
bg_light = '#737373'
grad = [
    '#6b71f5',
    '#b1c8ed'
]
root = ttk.Window(themename="morphcustom")
# style = ttk.Style(root)
# root.tk.call("source", "Azure-ttk-theme-main/azure.tcl")
# root.tk.call("set_theme", "light")
root.title('Algorithm Visualisation')
root.maxsize(900, 900)
root.config()
theme_var = StringVar(root)
algo = StringVar
data = []
old_data = []

defaultsize = StringVar(root)
defaultsize.set("60")
defaulmin = StringVar(root)
defaulmin.set("0")
defaulmax = StringVar(root)
defaulmax.set("100")
retain = IntVar(root)


def main():
    def draw(data, color, swaps=0):
        canvas.delete("all")
        ch = 650
        cw = 810
        xwidth = cw / (len(data) + 1)
        offset = 50
        spacing = 8
        normaldata = [i / max(data) for i in data]

        for i, height in enumerate(normaldata):
            x0 = i * xwidth + offset + spacing
            y0 = ch - height * 440
            x1 = (i + 1) * xwidth + offset
            y1 = ch
            canvas.create_rectangle(x0, y0, x1, y1, fill=color[i], width=0)
            canvas.create_text(x0, y1 + 8, text=data[i], fill=color[i], font=('MS Sans Serif', 8))

        root.update()

    def set_theme():
        startButton.configure(state="active")
        # root.tk.call("set_theme", theme_var.get())
        pass
    def generate():
        global data
        try:
            min = int(minEntry.get())
        except:
            min = 1
        try:
            max = int(maxEntry.get())
        except:
            max = 99
        try:
            size = int(sizeEntry.get())
        except:
            size = 60
        data = []

        if min < 0:
            min = 0
        if max > 500:
            max = 500
        if size > 100:
            size = 100
        if size < 3:
            size = 3
        for _ in range(size):
            element = random.randint(min, max)
            data.append(element)
            old_data.append(element)
        startButton.configure(state=ACTIVE)   
        draw(data, [grad[i % 2] for i in range(len(data))], 0)
        # set_theme()
        

    def startAlgo():
        global data
        if not data:
            return
        if algomenu.get() == 'Quick Sort':
            quick_sort(data, 0, len(data) - 1, draw, speedScale.get())
            # draw(data, [grad[x % 2] for x in range(len(data))],0)

        elif algomenu.get() == 'Bubble Sort':
            bubble_sort(data, draw, speedScale.get())
            # draw(data, [grad[x % 2] for x in range(len(data))], 0)
        elif algomenu.get() == 'Merge Sort':
            merge_sort(data, draw, speedScale.get()+0.03)

        elif algomenu.get() == 'Binary Search':
            binarySearch(data, 0, len(data) - 1, int(xEntry.get()), draw, speedScale.get())

    UI_frame = ttk.Frame(root, width=900, height=50)
    UI_frame.pack(padx=0, pady=0, side=TOP)

    canvas = Canvas(root, width=1100, height=800)
    canvas.pack(side=BOTTOM)

    Label(UI_frame, text="Algorithm: ").grid(row=0, column=0, padx=0, pady=5, sticky=W)
    algomenu = ttk.Combobox(UI_frame, textvariable=algo,
                            values=['Bubble Sort', 'Quick Sort', 'Binary Search', 'Merge Sort'], width=14)
    algomenu.grid(row=0, column=1, padx=13, pady=5)
    algomenu.current(0)

    # Label(UI_frame, text="Light").grid(row=3, column=0, padx=0, pady=5, sticky=W)
    # theme_button = ttk.Checkbutton(UI_frame, style="Switch.TCheckbutton", variable=theme_var, onvalue="dark",
    #                                offvalue="light",
    #                                command=set_theme()).grid(row=3, column=0, padx=30, sticky=EW)
    # Label(UI_frame, text="Dark").grid(row=3, column=0, padx=6, pady=5, sticky=E)
    startButton = ttk.Button(UI_frame,)
    startButton.configure(
     text="      Start     ", style="Accent.TButton", command=startAlgo, state= DISABLED
    )
    startButton.grid(row=1, column=4, padx=13, pady=0)
    
    Label(UI_frame, text="Size of Data: ").grid(row=1, column=0, padx=0, pady=5, sticky=W)
    sizeEntry = ttk.Spinbox(UI_frame, from_=0, to=100, increment=1, textvariable=defaultsize, width=6)
    sizeEntry.grid(row=1, column=1, padx=13, pady=5, sticky=W)

    Label(UI_frame, text="Min Value: ").grid(row=0, column=2, padx=0, pady=5, sticky=W)
    minEntry = ttk.Spinbox(UI_frame, from_=0, to=100, increment=1, textvariable=defaulmin, width=6)
    minEntry.grid(row=0, column=3, padx=13, pady=5, sticky=W)

    Label(UI_frame, text="Max Value: ").grid(row=1, column=2, padx=0, pady=5, sticky=W)
    maxEntry = ttk.Spinbox(UI_frame, from_=0, to=100, increment=1, textvariable=defaulmax, width=6)
    maxEntry.grid(row=1, column=3, padx=13, pady=5, sticky=W)

    Label(UI_frame, text="Speed: ").grid(row=2, column=2, padx=0, pady=5, sticky=W)
    speedScale = ttk.Scale(UI_frame, from_=1, to_=0.000001, length=150)
    speedScale.set(0.25)
    speedScale.grid(row=2, column=3, padx=13)
    Label(UI_frame, text="").grid(row=2, column=4, padx=0, pady=5, sticky=W)

    Label(UI_frame, text="Find Element: ").grid(row=2, column=0, padx=0, pady=5, sticky=W)
    xEntry = ttk.Spinbox(UI_frame, from_=0, to=100, increment=1, width=6)
    xEntry.grid(row=2, column=1, padx=13, pady=5, sticky=W)

    ttk.Button(
        UI_frame, text="Create Data", style="Accent.TButton", command=generate
    ).grid(row=0, column=4, padx=0, pady=6)

    root.mainloop()


if __name__ == "__main__":
    main()
