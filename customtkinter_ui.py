import customtkinter as ctk
from datetime import datetime
import PIL.Image, PIL.ImageTk
from PIL import Image

import os

width = 1400
height = 840
frame_height = 650
frame_width = 800

is_on = True
is_on1 = True
is_on2 = True
is_on3 = True
is_on4 = True
is_on5 = True
# Define Our Images
on = ctk.CTkImage(Image.open("assets\on.png"), size=(100, 50))
off = ctk.CTkImage(Image.open("assets\off.png"), size=(100, 50))

blink_count = 0


# the main app
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Eye App")
        self.geometry("1100x700")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")

        # data
        self.current_window = ctk.StringVar(value="overview")
        self.current_window.trace("w", self.change_window)

        # widgets
        self.menu = Menu(self, self.current_window)
        self.windows = {"overview": Overview(self), "view": View(self), "settings": Settings(self),
                        "analysis": Analysis(self), "user": User(self)}

        self.change_window()
        self.mainloop()

        # print("executed")

    def change_window(self, *args):
        for name, window in self.windows.items():
            if self.current_window.get() == name:
                window.start()
                # print(name)
            else:
                window.forget()


# the menu
class Menu(ctk.CTkFrame):
    def __init__(self, parent, window_string):
        super().__init__(master=parent, corner_radius=0)

        # variables
        self.font = ctk.CTkFont(size=15, weight="bold")
        self.window_string = window_string

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
        # self.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "eye_icon1.png")), size=(60, 60))
        self.overview_button_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "assets\home.png")),
                                                  dark_image=Image.open(os.path.join(image_path, "assets\home.png")),
                                                  size=(35, 35))
        self.view_button_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "assets\preview.png")),
                                              dark_image=Image.open(os.path.join(image_path, "assets\preview.png")),
                                              size=(35, 35))
        self.graph_button_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "assets\overview.png")),
                                               dark_image=Image.open(os.path.join(image_path, "assets\overview.png")),
                                               size=(35, 35))
        self.settings_button_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "assets\settings.png")),
                                                  dark_image=Image.open(os.path.join(image_path, "assets\settings.png")),
                                                  size=(35, 35))
        self.dp_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "assets/user.png")),
                                     dark_image=Image.open(os.path.join(image_path, "assets/user.png")), size=(35, 35))

        self.overview_button = ctk.CTkButton(self, corner_radius=120, height=40, border_spacing=10, text="",
                                             hover_color="light green",
                                             fg_color="transparent", text_color=("gray10", "gray90"),
                                             image=self.overview_button_image)
        self.view_button = ctk.CTkButton(self, corner_radius=20, height=40, border_spacing=10, text="",
                                         hover_color="light green",
                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                         image=self.view_button_image)
        self.graph_button = ctk.CTkButton(self, corner_radius=20, height=40, border_spacing=10, text="",
                                          hover_color="light green",
                                          fg_color="transparent", text_color=("gray10", "gray90"),
                                          image=self.graph_button_image)
        self.settings_button = ctk.CTkButton(self, corner_radius=20, height=40, border_spacing=10, text="",
                                             hover_color="light green",
                                             fg_color="transparent", text_color=("gray10", "gray90"),
                                             image=self.settings_button_image)
        self.user_button = ctk.CTkButton(self, corner_radius=20, height=40, border_spacing=10, text="",
                                         hover_color="light green",
                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                         image=self.dp_image)

        self.buttons = [self.overview_button, self.view_button, self.graph_button, self.settings_button]

        # self.overview_button.configure(command=lambda: self.window_changed(self.overview_button, "overview"))
        self.overview_button.configure(command=lambda: self.window_changed(self.overview_button, "overview"),
                                       fg_color="light blue")
        self.view_button.configure(command=lambda: self.window_changed(self.view_button, "view"))
        self.graph_button.configure(command=lambda: self.window_changed(self.graph_button, "analysis"))
        self.settings_button.configure(command=lambda: self.window_changed(self.settings_button, "settings"))
        self.user_button.configure(command=lambda: self.window_changed(self.user_button, "user"))
        # self.overview_button.grid(row=0, column=0, sticky="ew")
        # placing buttons
        for button in self.buttons:
            button.pack(fill="x", padx=20, pady=10, ipady=5)

        self.place(relwidth=0.1, relheight=1, relx=0, rely=0, anchor="nw")
        self.user_button.pack(fill="x", padx=20, pady=10, ipady=5, side="bottom")
        self.buttons.append(self.user_button)

    # def create_menu_button(self, title, toggled=False):
    #     button = ctk.CTkButton(master=self, text=title,
    #                            corner_radius=10, font=self.font,
    #                            hover_color="dark blue")
    #     if toggled:
    #         button.configure(fg_color="dark blue")
    #     else:
    #         button.configure(fg_color="dark blue")

    #     return button

    def window_changed(self, button, window_name):
        self.window_string.set(window_name)

        for i in self.buttons:
            if i is button:
                i.configure(fg_color="light blue")
            else:
                i.configure(fg_color="transparent")


# head class for all windows
class Window(ctk.CTkFrame):
    def __init__(self, parent, name):
        super().__init__(master=parent, fg_color="transparent")

        self.window_name = name

    def start(self):
        self.place(relwidth=0.8, relheight=1, relx=0.15, rely=0, anchor="nw")

    def forget(self):
        self.place_forget()


class Overview(Window):
    def __init__(self, parent):
        super().__init__(parent=parent, name="overview")

        self.overview_frame = ctk.CTkFrame(self, height=frame_height, width=frame_width, fg_color="transparent")
        self.overview_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.refresh_switch()

    def refresh_switch(self):
        print("refreshed")
        self.overview_frame.forget()
        self.overview_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.overview_frame_label = ctk.CTkLabel(self.overview_frame, text="Overview",
                                                 font=ctk.CTkFont(size=35, weight="bold"))
        self.overview_frame_label.place(relx=0.2, rely=0.1, anchor="center")
        self.refresh_button = ctk.CTkButton(self.overview_frame, text="Refresh", corner_radius=10,
                                            font=ctk.CTkFont(size=15, weight="bold"), hover_color="light green",
                                            command=self.refresh_switch)
        self.refresh_button.place(relx=0.5, rely=0.9, anchor="center")

        # Execute the SELECT query for face detection
        # Print or use the count as neededy
        # print(f"Number of entries with face not detected = 0: {face_not_detected}")
        # print(f"Number of entries with eye open = 0: {eyes_open}")
        # print(f"Number of entries with eye closed = 0: {eyes_closed}")


# a window to create to do lists and etc
class View(Window):
    # print("hello1")
    def __init__(self, parent, video_source=0):
        # print("hello")
        # self.video_source = video_source
        # self.vid = MyVideoCapture(0)
        super().__init__(parent=parent, name="view")
        # print("hello")
        self.video_source = video_source

        # frame to diaplay camera output
        self.camera_frame = ctk.CTkFrame(self, height=frame_height, width=frame_width, fg_color="transparent")
        self.camera_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.canvas = ctk.CTkCanvas(self.camera_frame, width=width, height=height)
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")
        self.delay = 15
        self.update()

        self.preview_label = ctk.CTkLabel(self.camera_frame, text="Camera Preview",
                                          font=ctk.CTkFont(size=25, weight="bold"))
        self.preview_label.place(relx=0.29, rely=0.875)

        self.home_frame_button_1 = ctk.CTkButton(self.camera_frame, image=on if is_on5 else off, text="",
                                                 fg_color="transparent", text_color=("gray10", "gray90"),
                                                 hover_color=("gray30", "gray30"), command=self.switch5)
        self.home_frame_button_1.place(relx=0.54, rely=0.857)

        # Update bar heights with new blendshape values
        # for i, rect in enumerate(bar_plot):

    def animation_mode(self):
        self.add_progress1 = ctk.CTkProgressBar(self.camera_frame, orientation="vertical")
        self.add_progress1.place(relx=0.03, rely=0.5, anchor=ctk.CENTER)

        self.add_progress2 = ctk.CTkProgressBar(self.camera_frame, orientation="vertical")
        self.add_progress2.place(relx=0.98, rely=0.5, anchor=ctk.CENTER)

    def switch5(self):
        global is_on5

        # Determine is on or off
        if is_on5:
            self.home_frame_button_1.configure(image=off)
            print("button is pressed")
            is_on5 = False
        else:
            self.home_frame_button_1.configure(image=on)
            print("button is pressed")
            # self.my_label.configure(text = "The Switch is On")#, fg = "green")
            is_on5 = True


# a window to measure time spent on studying and working
class Analysis(Window):
    def __init__(self, parent):
        super().__init__(parent=parent, name="analysis")

        self.analysis_frame = ctk.CTkFrame(self, height=frame_height, width=frame_width, fg_color="red")
        self.analysis_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.analysis_label = ctk.CTkLabel(self.analysis_frame, text="Analysis",
                                           font=ctk.CTkFont(size=35, weight="bold"))
        self.analysis_label.place(relx=0.2, rely=0.1, anchor="center")


class Settings(Window):
    # print("hello")
    def __init__(self, parent):
        # print("hello1")
        super().__init__(parent=parent, name="settings")
        # print("hello2")

        self.settings_frame = ctk.CTkFrame(self, height=frame_height, width=frame_width, fg_color="transparent")
        self.settings_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.settings_frame_label = ctk.CTkLabel(self.settings_frame, text="settings",
                                                 font=ctk.CTkFont(size=40, weight="bold"))
        self.settings_frame_label.place(relx=0.25, rely=0.1, anchor="e")

        # self.appearence_mode_label = ctk.CTkLabel(self.settings_frame, text="Appearence Mode", font=ctk.CTkFont(size=20, weight="bold"))
        # self.appearence_mode_label.place(relx=0.2,rely=0.3,anchor=ctk.CENTER)

        # self.appearance_mode_menu = ctk.CTkOptionMenu(self.settings_frame,height=50,width=150,corner_radius=50, values=["Light", "Dark", "System"],
        #                                                         command=self.change_appearance_mode_event)
        # self.appearance_mode_menu.place(relx=0.4,rely=0.3,anchor=ctk.W)

        self.default_animation_button = ctk.CTkButton(self.settings_frame, text="", image=on if is_on else off,
                                                      border_spacing=10, fg_color="transparent",
                                                      text_color=("gray10", "gray90"), anchor="w", command=self.switch)
        self.default_animation_button.place(relx=0.4, rely=0.3, anchor=ctk.W)

        self.default_animation_label = ctk.CTkLabel(self.settings_frame, text="Eye Animation",
                                                    font=ctk.CTkFont(size=20, weight="bold"))
        self.default_animation_label.place(relx=0.2, rely=0.3, anchor="center")

        self.notification_label = ctk.CTkLabel(self.settings_frame, text="Notification",
                                               font=ctk.CTkFont(size=20, weight="bold"))
        self.notification_label.place(relx=0.17, rely=0.45, anchor=ctk.CENTER)

        self.notification_button = ctk.CTkButton(self.settings_frame, text="", image=on if is_on1 else off,
                                                 border_spacing=10, fg_color="transparent",
                                                 text_color=("gray10", "gray90"), anchor="w", command=self.switch1)
        self.notification_button.place(relx=0.4, rely=0.45, anchor=ctk.W)

        self.sound_label = ctk.CTkLabel(self.settings_frame, text="Sound", font=ctk.CTkFont(size=20, weight="bold"))
        self.sound_label.place(relx=0.14, rely=0.6, anchor=ctk.CENTER)

        self.sound_button = ctk.CTkButton(self.settings_frame, text="", image=on if is_on2 else off, border_spacing=10,
                                          fg_color="transparent", text_color=("gray10", "gray90"), anchor="w",
                                          command=self.switch2)
        self.sound_button.place(relx=0.4, rely=0.6, anchor=ctk.W)

        self.eye_button = ctk.CTkButton(self.settings_frame, text="", image=on if is_on3 else off, border_spacing=10,
                                        fg_color="transparent", text_color=("gray10", "gray90"), anchor="w",
                                        command=self.switch3)
        self.eye_button.place(relx=0.4, rely=0.75, anchor=ctk.W)

        self.eye_button_label = ctk.CTkLabel(self.settings_frame, text="Eye",
                                             font=ctk.CTkFont(size=20, family='brasika', weight="bold"))
        self.eye_button_label.place(relx=0.13, rely=0.75, anchor=ctk.CENTER)

        self.both_eye = ctk.CTkButton(self.settings_frame, text="", image=on if is_on4 else off, border_spacing=10,
                                      fg_color="transparent", text_color=("gray10", "gray90"), anchor="w",
                                      command=self.switch4)
        self.both_eye.place(relx=0.4, rely=0.9, anchor=ctk.W)

        self.both_eye_label = ctk.CTkLabel(self.settings_frame, text="Both Eye",
                                           font=ctk.CTkFont(size=20, weight="bold"))
        self.both_eye_label.place(relx=0.15, rely=0.9, anchor=ctk.CENTER)

        self.accuracy_label = ctk.CTkLabel(self.settings_frame, text="Accuracy",
                                           font=ctk.CTkFont(size=20, weight="bold"))
        self.accuracy_label.place(relx=0.9, rely=0.8, anchor=ctk.CENTER)

        self.threshlod_bar = ctk.CTkSlider(self.settings_frame, orientation="vertical", from_=0.01, height=210,
                                           to=0.7)  # , number_of_steps=4)
        self.threshlod_bar.place(relx=0.9, rely=0.5, anchor=ctk.CENTER)

        self.overview_label = ctk.CTkLabel(self.settings_frame, text="Overview",
                                           font=ctk.CTkFont(size=20, weight="bold"))
        self.overview_label.place(relx=0.7, rely=0.9, anchor=ctk.CENTER)

        self.overview_bar = ctk.CTkSlider(self.settings_frame, orientation='vertical', height=420, from_=0.01, to=24,
                                          number_of_steps=28)
        self.overview_bar.place(relx=0.7, rely=0.55, anchor=ctk.CENTER)

        # updated_threshold_value = cursor.execute('SELECT threshold FROM defaut_data').fetchone()[0] if cursor.execute('SELECT threshold FROM defaut_data').fetchone() else None

        # print(overview_bar_save)
        # cursor.execute('''INSERT INTO defaut_data (default_overview,notification) VALUES (?)''', (overview_bar_save,))

    # def change_appearance_mode_event(self, new_appearance_mode):
    #     ctk.set_appearance_mode(new_appearance_mode)

    def switch(self):
        global is_on

        # Determine is on or off
        if is_on:
            self.default_animation_button.configure(image=off)
            print("button is pressed")
            is_on = False
        else:
            self.default_animation_button.configure(image=on)
            print("button is pressed")
            # self.my_label.configure(text = "The Switch is On")#, fg = "green")
            is_on = True

    def switch1(self):
        global is_on1

        # Determine is on or off
        if is_on1:
            self.notification_button.configure(image=off)
            print("button is pressed")
            is_on1 = False
        else:
            self.notification_button.configure(image=on)
            print("button is pressed")
            # self.my_label.configure(text = "The Switch is On")#, fg = "green")
            is_on1 = True

    def switch2(self):
        global is_on2

        # Determine is on or off
        if is_on2:
            self.sound_button.configure(image=off)
            print("button is pressed")
            is_on2 = False
        else:
            self.sound_button.configure(image=on)
            print("button is pressed")
            # self.my_label.configure(text = "The Switch is On")#, fg = "green")
            is_on2 = True

    def switch3(self):
        global is_on3

        # Determine is on or off
        if is_on3:
            self.eye_button.configure(image=off)
            print("button is pressed")
            is_on3 = False
        else:
            self.eye_button.configure(image=on)
            print("button is pressed")
            # self.my_label.configure(text = "The Switch is On")#, fg = "green")
            is_on3 = True

    def switch4(self):
        global is_on4

        # Determine is on or off
        if is_on4:
            self.both_eye.configure(image=off)
            print("button is pressed")
            is_on4 = False
        else:
            self.both_eye.configure(image=on)
            print("button is pressed")
            # self.my_label.configure(text = "The Switch is On")#, fg = "green")
            is_on4 = True


class User(Window):
    def __init__(self, parent):
        super().__init__(parent=parent, name="user")

        self.user_frame = ctk.CTkFrame(self, height=frame_height, width=frame_width, fg_color="transparent")
        self.user_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.user_frame_label = ctk.CTkLabel(self, text="User", font=ctk.CTkFont(size=35, weight="bold"))
        self.user_frame_label.place(relx=0.2, rely=0.1, anchor="center")
        # print("user")


if __name__ == '__main__':
    App()