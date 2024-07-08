import tkinter as tk
from PIL import Image, ImageTk, ImageDraw

def create_rounded_rectangle_image(width, height, radius, color):
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    # Draw the rounded rectangle
    draw.rounded_rectangle(
        (0, 0, width, height),
        radius=radius,
        fill=color
    )
    
    return image

def main():
    # Window dimensions
    window_width = 300
    window_height = 200
    radius = 20  # Radius for rounded corners
    background_color = (100, 100, 255, 255)  # RGBA color

    root = tk.Tk()

    # Create rounded rectangle image
    rounded_rect_image = create_rounded_rectangle_image(window_width, window_height, radius, background_color)
    tk_image = ImageTk.PhotoImage(rounded_rect_image)

    # Create a canvas and set the image as background
    canvas = tk.Canvas(root, width=window_width, height=window_height, highlightthickness=0)
    canvas.pack()
    canvas.create_image(0, 0, anchor='nw', image=tk_image)

    # Example content
    label = tk.Label(root, text="Hello, World!", bg='#6464FF', fg='white', font=('Arial', 18))
    label.place(x=50, y=80)

    # Set window attributes
    root.overrideredirect(True)  # Remove window decorations
    root.geometry(f'{window_width}x{window_height}')
    root.config(bg='#6464FF')

    # Add window drag functionality
    def on_mouse_press(event):
        root.startX = event.x
        root.startY = event.y

    def on_mouse_drag(event):
        x = root.winfo_pointerx() - root.startX
        y = root.winfo_pointery() - root.startY
        root.geometry(f'+{x}+{y}')

    root.bind('<Button-1>', on_mouse_press)
    root.bind('<B1-Motion>', on_mouse_drag)

    root.mainloop()

if __name__ == '__main__':
    main()
