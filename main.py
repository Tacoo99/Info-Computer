import time
import customtkinter
import os
from PIL import Image
import platform
import psutil
import wmi
import re
import threading


class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.label_list = []
        self.button_list = []

    def add_item(self, item, copy_image, info, image=None):
        label = customtkinter.CTkLabel(self, text=item, image=image, compound="left", padx=5, anchor="w", font = ('', 12, 'bold'))
        button = customtkinter.CTkButton(self, width=40, height=24, text="", image=copy_image, compound='right')
        button2 = customtkinter.CTkButton(self, text=info, width=40, height=24)
        if self.command is not None:
            button.configure(command=lambda: self.command(item))
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        button2.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)
        button.grid(row=len(self.button_list), column=2, pady=(0, 10), padx=5)
        self.label_list.append(label)
        self.button_list.append(button)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.progressbar = customtkinter.CTkProgressBar(self, orientation="horizontal", determinate_speed=2)
        
        self.after(0, self.load_information(self.progressbar))
        self.title("Info-Komputer")
        self.resizable(False, False)
        self.iconbitmap("images/icon/icon.ico")
        self.grid_columnconfigure((0), weight=1)

        
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
        self.ethernet_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(darkImage_path, "ethernet_dark.png")),
                                                        dark_image=Image.open(os.path.join(lightImage_path, "ethernet_light.png")), size=(30, 30))
        self.servicedesk_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(darkImage_path, "servicedesk_dark.png")),
                                                        dark_image=Image.open(os.path.join(lightImage_path, "servicedesk_light.png")), size=(30, 30))
        self.website_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(darkImage_path, "website_dark.png")),
                                                        dark_image=Image.open(os.path.join(lightImage_path, "website_light.png")), size=(30, 30))
        self.copy_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(darkImage_path, "copy_dark.png")),
                                                        dark_image=Image.open(os.path.join(lightImage_path, "copy_light.png")), size=(23, 23))
        
        
        
        computer_titles= ["Computer name","Serial Number","Windows name","Windows version","BIT","IP Address","CPU","GPU","RAM"]
        computer_images=["laptop", "serial", "windows","version","bit","ethernet","cpu","gpu","ram"]
        
        user_titles = ["Username","Domain","E-mail","Account status","Password expiry","Servicedesk phone","Servicedesk website"]
        user_images = ["username","domain","email","account-status","password-expiry","servicedesk", "website"]
        
        
        self.progressbar.grid(row=0, column=0, padx=20, pady=8, sticky="ew", columnspan=2)

        # create scrollable label and button frame
        self.scrollable_userInfo = ScrollableLabelButtonFrame(self, width=300, command=self.label_button_frame_event, label_text="Computer information")
        self.scrollable_userInfo.grid(row=1, column=0, padx=15, pady=5, sticky="nsew")
        
        
        for i, text in enumerate(user_titles):
            image_filename = user_images[i]

            light_image_path = os.path.join(lightImage_path, f"{image_filename}_light.png")
            dark_image_path = os.path.join(darkImage_path, f"{image_filename}_dark.png")

            image = customtkinter.CTkImage(light_image=Image.open(dark_image_path), dark_image=Image.open(light_image_path), size=(30, 30))

            self.scrollable_userInfo.add_item(f"{text}", image=image, copy_image=self.copy_image, info='test')

        # create scrollable label and button frame
        self.scrollable_computerInfo = ScrollableLabelButtonFrame(self, width=300, command=self.label_button_frame_event, label_text="User information")
        self.scrollable_computerInfo.grid(row=1, column=1, padx=15, pady=5, sticky="nsew")
        
        for i, text in enumerate(computer_titles):
            image_filename = computer_images[i]

            light_image_path = os.path.join(lightImage_path, f"{image_filename}_light.png")
            dark_image_path = os.path.join(darkImage_path, f"{image_filename}_dark.png")

            image = customtkinter.CTkImage(light_image=Image.open(dark_image_path), dark_image=Image.open(light_image_path), size=(30, 30))

            self.scrollable_computerInfo.add_item(f"{text}", image=image, copy_image=self.copy_image, info='test')

    def label_button_frame_event(self, item):
        print(f"Kliknięto w {item}")
        
    
    def load_information(self, progressbar):
        thread = threading.Thread(target=self.getAllInformations)
        progressbar.start()
        thread.start()
        
    def get_active_interface_ips(self):
        c = wmi.WMI()
        adapters = c.Win32_NetworkAdapterConfiguration(IPEnabled=True)
        active_interface_ip = None

        for adapter in adapters:
            if adapter.IPAddress:
                for ip in adapter.IPAddress:
                    if not ip.startswith("127.") and not ip.startswith("169.254."):
                        active_interface_ip = ip
                        break

            if active_interface_ip:
                break

        return active_interface_ip
    
    def getUsername(self, user_informations):
        self.add_informations(user_informations, os.getlogin())
    
    def getDomain(self, user_informations):
        self.add_informations(user_informations, 'mpl.mee.com')
        
    def getEmail(self, user_informations):
        self.add_informations(user_informations, '@mpl.mee.com')
        
    def getAccountStatus(self, user_informations):
        self.add_informations(user_informations, 'locked/unlocked')
        
    def getPasswordExpiry(self, user_informations):
        self.add_informations(user_informations, 'data haselka')
        
    def getServicedeskPhone(self, user_informations):
        self.add_informations(user_informations, 'numer do servicedesk')
    
    def getServicedeskWebsite(self, user_informations):
        self.add_informations(user_informations, 'servicedesk.mpl.mee.com')
    
    def getComputerName(self, my_system, computer_informations):
        self.add_informations(computer_informations, my_system.node)
    
    def getWindowsName(self, my_system, computer_informations):
        windowsName = my_system.system + ' ' + my_system.release
        self.add_informations(computer_informations, windowsName)
    
    def getWindowsVersion(self, my_system, computer_informations):
        self.add_informations(computer_informations, my_system.version)
    
    def getBIT(self, my_system, computer_informations):
        self.add_informations(computer_informations, my_system.machine)
    
    def getIP(self, computer_informations):
        active_ip = self.get_active_interface_ips()
        
        if active_ip:
            IP = active_ip
        else:
            IP = 'No connection'
            
        self.add_informations(computer_informations, IP)
        
    
    def getSerialNumber(self, computer_informations):
        command = "wmic bios get serialnumber"
        output = os.popen(command).read()
        serial_number = re.search(r"\bSerialNumber\b\s*(\S+)", output)
        
        self.add_informations(computer_informations, serial_number.group(1))
    
    def getCPU(self, wmi, computer_informations):
        self.add_informations(computer_informations, wmi.Win32_Processor()[0].name)
    
    def getGPU(self, wmi, computer_informations):
        self.add_informations(computer_informations, wmi.Win32_VideoController()[0].name)
    
    def getRAM(self, computer_informations):
        self.add_informations(computer_informations, f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
    
    def add_informations(self, informations_array, data):
        informations_array.append((data))
        
    
    def getAllInformations(self):
        my_system = platform.uname()
        pc = wmi.WMI()
        
        user_informations = []
        computer_informations = []
        
        # Info o userze
        self.getUsername(user_informations)
        self.getDomain(user_informations)
        self.getDomain(user_informations)
        self.getEmail(user_informations)
        self.getAccountStatus(user_informations)
        self.getPasswordExpiry(user_informations)
        self.getServicedeskPhone(user_informations)
        self.getServicedeskWebsite(user_informations)
    
    
        # Info o komputerze
        self.getComputerName(my_system, computer_informations)
        self.getSerialNumber(computer_informations)
        self.getWindowsName(my_system, computer_informations)
        self.getWindowsVersion(my_system, computer_informations)
        self.getBIT(my_system, computer_informations)
        self.getIP(computer_informations)
        
        self.getCPU(pc, computer_informations)
        self.getGPU(pc, computer_informations)
        self.getRAM(computer_informations)



if __name__ == "__main__":
    app = App()
    app.grid_columnconfigure((0), weight=1)
    app.mainloop()