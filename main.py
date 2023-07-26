import customtkinter
import os
from PIL import Image

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.toplevel_window = None

        self.title("Info-Komputer")
        self.resizable(False, False)
        self.iconbitmap("images/icon/icon.ico")
        
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.winfo_width()) // 2
        y = (screen_height - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")
        
        # grid 2x2
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # load images with light and dark mode image
        lightImage_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images\light")
        darkImage_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images\dark")
        
        
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
        
         # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=2)

        self.banner_text = customtkinter.CTkLabel(self.home_frame, text="Info Computer",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.banner_text.grid(row=0, column=0, sticky="nsew", ipady=10)
        self.description_text = customtkinter.CTkLabel(self.home_frame, text="Some information about your computer",
                                                  font=customtkinter.CTkFont(size=15))
        self.description_text.grid(row=1, column=0, padx=35, sticky="n")
        
        self.computername_label = customtkinter.CTkLabel(self.home_frame, text="Username", font=customtkinter.CTkFont(size=14), image=self.username_image, compound="left")
        self.computername_label.grid(row=2, column=0, padx=0, pady=10, sticky="nsew")
        self.username_entry = customtkinter.CTkEntry(self.home_frame, width=200, placeholder_text="Username")
        self.username_entry.grid(row=2, column=0, padx=30, pady=(15, 15), ipady=5)
        
        
        self.username_label = customtkinter.CTkLabel(self.home_frame, text="Computer name", font=customtkinter.CTkFont(size=14), image=self.laptop_image, compound="left")
        self.username_label.grid(row=3, column=0, padx=0, pady=10, sticky="nsew")
        
        self.serial_label = customtkinter.CTkLabel(self.home_frame, text="Serial Number", font=customtkinter.CTkFont(size=14), image=self.serial_image, compound="left")
        self.serial_label.grid(row=4, column=0, padx=0, pady=10, sticky="nsew")
        
        self.windows_label = customtkinter.CTkLabel(self.home_frame, text="Windows version", font=customtkinter.CTkFont(size=14), image=self.windows_image, compound="left")
        self.windows_label.grid(row=5, column=0, padx=0, pady=10, sticky="nsew")
        
        self.wifi_label = customtkinter.CTkLabel(self.home_frame, text="WI-FI IP Address", font=customtkinter.CTkFont(size=14), image=self.wifi_image, compound="left")
        self.wifi_label.grid(row=6, column=0, padx=0, pady=10, sticky="nsew")
        
        self.ethernet_label = customtkinter.CTkLabel(self.home_frame, text="Ethernet IP Address", font=customtkinter.CTkFont(size=14), image=self.ethernet_image, compound="left")
        self.ethernet_label.grid(row=7, column=0, padx=0, pady=10, sticky="nsew")
        
        self.servicedesk_label = customtkinter.CTkLabel(self.home_frame, text="Servicedesk phone", font=customtkinter.CTkFont(size=14), image=self.servicedesk_image, compound="left")
        self.servicedesk_label.grid(row=8, column=0, padx=0, pady=10, sticky="nsew")
        
        self.website_label = customtkinter.CTkLabel(self.home_frame, text="Servicedesk website", font=customtkinter.CTkFont(size=14), image=self.website_image, compound="left")
        self.website_label.grid(row=9, column=0, padx=0, pady=10, sticky="nsew")
        
        self.home_frame.grid(row=0, column=1)
        
        
if __name__ == "__main__":
    app = App()
    app.mainloop()