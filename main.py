import customtkinter
import os
from PIL import Image



class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.label_list = []
        self.button_list = []

    def add_item(self, item, image=None):
        label = customtkinter.CTkLabel(self, text=item, image=image, compound="left", padx=5, anchor="w")
        button = customtkinter.CTkButton(self, text="Command", width=100, height=24)
        if self.command is not None:
            button.configure(command=lambda: self.command(item))
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)
        self.label_list.append(label)
        self.button_list.append(button)

    def remove_item(self, item):
        for label, button in zip(self.label_list, self.button_list):
            if item == label.cget("text"):
                label.destroy()
                button.destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                return


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Info-Komputer")
        self.resizable(False, False)
        self.iconbitmap("images/icon/icon.ico")
        
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.winfo_width()) // 2
        y = (screen_height - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")
        
        # load images with light and dark mode image
        lightImage_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images", "light")
        darkImage_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images", "dark")

        
        
        self.username_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(darkImage_path, "username_dark.png")),
                                                        dark_image=Image.open(os.path.join(lightImage_path, "username_light.png")), size=(30, 30))
        self.laptop_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(darkImage_path, "laptop_dark.png")),
                                                        dark_image=Image.open(os.path.join(lightImage_path, "laptop_light.png")), size=(30, 30))
        self.serial_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(darkImage_path, "serial_dark.png")),
                                                        dark_image=Image.open(os.path.join(lightImage_path, "serial_light.png")), size=(30, 30))
        self.windows_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(darkImage_path, "windows_dark.png")),
                                                        dark_image=Image.open(os.path.join(lightImage_path, "windows_light.png")), size=(30, 30))
        self.version_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(darkImage_path, "version_dark.png")),
                                                        dark_image=Image.open(os.path.join(lightImage_path, "version_light.png")), size=(30, 30))
        self.wifi_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(darkImage_path, "wifi_dark.png")),
                                                        dark_image=Image.open(os.path.join(lightImage_path, "wifi_light.png")), size=(30, 30))
        self.ethernet_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(darkImage_path, "ethernet_dark.png")),
                                                        dark_image=Image.open(os.path.join(lightImage_path, "ethernet_light.png")), size=(30, 30))
        self.servicedesk_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(darkImage_path, "servicedesk_dark.png")),
                                                        dark_image=Image.open(os.path.join(lightImage_path, "servicedesk_light.png")), size=(30, 30))
        self.website_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(darkImage_path, "website_dark.png")),
                                                        dark_image=Image.open(os.path.join(lightImage_path, "website_light.png")), size=(30, 30))
        
        
        computer_titles= ["Computer name","Serial Number","Windows name","Windows version","bit","Wi-Fi IP address","Ethernet IP address","CPU","GPU","RAM","BIOS"]
        computer_images=["laptop", "serial", "windows","version","bit","wifi","ethernet","cpu","gpu","ram","bios"]
        
        user_titles = ["Username","Domain","E-mail","Account status","Password expiry","Servicedesk phone","Servicedesk website"]
        user_images = ["username","domain","email","account-status","password-expiry","servicedesk", "website"]

        # create scrollable label and button frame
        self.scrollable_userInfo = ScrollableLabelButtonFrame(master=self, width=300, command=self.label_button_frame_event, label_text="Computer information")
        self.scrollable_userInfo.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")
        
        for i, text in enumerate(user_titles):
            image_filename = user_images[i]

            # Tworzenie ścieżek do obrazków dla obu trybów (light i dark)
            light_image_path = os.path.join(lightImage_path, f"{image_filename}_light.png")
            dark_image_path = os.path.join(darkImage_path, f"{image_filename}_dark.png")

            # Tworzenie obiektu CTkImage
            image = customtkinter.CTkImage(light_image=Image.open(dark_image_path), dark_image=Image.open(light_image_path), size=(30, 30))

            # Dodawanie elementu do listy
            self.scrollable_userInfo.add_item(f"{text}", image=image)

        # create scrollable label and button frame
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.scrollable_computerInfo = ScrollableLabelButtonFrame(master=self, width=300, command=self.label_button_frame_event, label_text="User information")
        self.scrollable_computerInfo.grid(row=0, column=2, padx=15, pady=15, sticky="nsew")
        
        for i, text in enumerate(computer_titles):
            image_filename = computer_images[i]

            # Tworzenie ścieżek do obrazków dla obu trybów (light i dark)
            light_image_path = os.path.join(lightImage_path, f"{image_filename}_light.png")
            dark_image_path = os.path.join(darkImage_path, f"{image_filename}_dark.png")

            # Tworzenie obiektu CTkImage
            image = customtkinter.CTkImage(light_image=Image.open(dark_image_path), dark_image=Image.open(light_image_path), size=(30, 30))

            # Dodawanie elementu do listy
            self.scrollable_computerInfo.add_item(f"{text}", image=image)

    def label_button_frame_event(self, item):
        print(f"label button frame clicked: {item}")


if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    app = App()
    app.mainloop()