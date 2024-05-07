import customtkinter
from sound_player import SoundPlayer
from PIL import Image

class Player:
    def __init__(self, master):
        self.sound = ['./sounds/coffee.wav','./sounds/toaster-2.wav']
        self.pointer = 0
        self.frame = customtkinter.CTkFrame(master)
        self.frame.grid(row=1, column=1, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.frame_label = customtkinter.CTkLabel(self.frame, text="Player Controls", font= ("Arial", 16))
        self.frame_label.grid(row=0, column=2, padx=(5, 5), pady=(5, 5), sticky="nsew")
        #self.frame.grid_columnconfigure(0, weight=0)
        self.render_buttons()
        self.render_wave_icon()
        self.render_sound_name()
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(4, weight=1)
        self.frame.grid_rowconfigure(2, weight=1)

    def update(self, sound):
        # a string list of sound file paths
        self.sound = sound
        self.pointer = 0

    def render_wave_icon(self):
        self.wave_icon = customtkinter.CTkImage(light_image=Image.open('default-cover-art.png'), dark_image=Image.open('default-cover-art.png'), size=(180,180))
        self.label = customtkinter.CTkLabel(self.frame, text="", image=self.wave_icon)
        self.label.grid(row=1, column=2, padx=(5, 5), pady=(5, 5), sticky="ew")

    def render_sound_name(self):
        self.sound_name = customtkinter.CTkLabel(master=self.frame, text=self.sound[self.pointer])
        self.sound_name.grid(row=2, column=2, sticky="ew")

    def render_buttons(self):
         self.prev_button = customtkinter.CTkButton(master=self.frame, text="⏮", command=lambda: self.prev_sound(), font= ("Arial", 20))
         self.prev_button.grid(row=3, column=1, padx=(5, 5), pady=(5, 5), sticky="ew")
         self.play_button = customtkinter.CTkButton(master=self.frame, text="⏵", command=lambda: self.play(), font= ("Arial", 20))
         self.play_button.grid(row=3, column=2, padx=(5, 5), pady=(5, 5), sticky="ew")
         self.next_button = customtkinter.CTkButton(master=self.frame, text="⏭", command=lambda: self.next_sound(), font= ("Arial", 20))
         self.next_button.grid(row=3, column=3, padx=(5, 5), pady=(5, 5), sticky="ew")

    def play(self):
        SoundPlayer.play_files(SoundPlayer, [self.sound[self.pointer]])
        self.next_sound()

    def next_sound(self):
        try:
            self.pointer += 1
            self.sound_name.configure(text=self.sound[self.pointer])
        except:
            self.pointer = 0
            self.sound_name.configure(text=self.sound[self.pointer])
    
    def prev_sound(self):
        try:
            self.pointer -= 1
            self.sound_name.configure(text=self.sound[self.pointer])
        except:
            self.pointer = len(self.sound) - 1
            self.sound_name.configure(text=self.sound[self.pointer])
     