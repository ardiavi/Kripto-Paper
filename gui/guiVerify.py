
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as tkmb
import guiLanding
import sys
sys.path.append("../Kripto_3-MAIN/src/")
import verification
import RSA


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame3")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Verify(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, width = 1200, height = 800, bg = "#FFFFFF")
        self.canvas = Canvas(
            master,
            bg = "#FFFFFF",
            height = 800,
            width = 1200,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.pubkey = (0, 0)

        def read_key():
            self.entry_2.delete(1.0, END)
            filetypes = [('public key', ".pub")]
            filename = ""
            filename = fd.askopenfile(filetypes=filetypes)
            filename = str(filename).split("'")[1]
            with open(filename, "r") as f:
                keystring = f.read()
                keystring = keystring.replace("(", "").replace(")", "")
                self.pubkey = tuple(map(int, keystring.split(",")))
            self.entry_2.insert(END, self.pubkey[0])

        self.istext = True

        def upload_pressed():
            self.entry_3.delete(1.0, END)
            filetypes = [('All files', '*.*'),('text files', '*.txt')]
            filename = ""
            filename = fd.askopenfile(filetypes=filetypes)
            filename = str(filename).split("'")[1]
            self.entry_3.insert(END, filename)
            self.istext = False
        
        def read_sign():
            self.entry_4.delete(1.0, END)
            filetypes = [('signature', ".txt")]
            filename = ""
            filename = fd.askopenfile(filetypes=filetypes)
            filename = str(filename).split("'")[1]
            self.entry_4.insert(END, filename)  
        
        def verify_pressed():
            if self.entry_3.get(1.0, END).replace("\n","") == "" or self.entry_2.get(1.0, END).replace("\n","") == "" or self.pubkey == (0, 0):
                tkmb.showerror("Error", "Please fill in all required fields")
            elif self.entry_4.get(1.0, END).replace("\n","") == "": #signature included in file
                if self.entry_3.get(1.0, END).replace("\n","").endswith(".txt"):
                    with open(self.entry_3.get(1.0, END).replace("\n",""), "r") as f:
                        lines = f.readlines()                
                        if lines[-1] == '*** End of digital signature ****' and lines[-3] == '*** Begin of digital signature ****\n':
                            signature = lines[-2][:-1]
                            lines[-4] = lines[-4].replace("\n","")
                            message = "".join(lines[:-3])
                            message = RSA.hashstring(message)
                            update_verify(verification.verification(message, signature, self.pubkey))
                        else:
                            tkmb.showerror("Error", "signature not found")
                else:
                    tkmb.showerror("Error", "signature not found")
            else: #signature in separate file
                with open(self.entry_4.get(1.0, END).replace("\n",""), "r") as f:
                    lines = f.readlines()                
                    if lines[-1] == '*** End of digital signature ****' and lines[-3] == '*** Begin of digital signature ****\n':
                        signature = lines[-2][:-1]
                    else:
                        tkmb.showerror("Error", "signature not found")
                if self.istext:
                    message = RSA.hashstring(self.entry_3.get(1.0, END).replace("\n",""))
                else:
                    message = RSA.hashfile(self.entry_3.get(1.0, END).replace("\n",""))
                update_verify(verification.verification(message, signature, self.pubkey))

                    
        
        def update_verify(status):
            if status == True:
                self.entry_1.config(text="Verified")
            else:
                self.entry_1.config(text="Not Verified")

                



        self.canvas.place(x = 0, y = 0)

        scrollbar = Scrollbar(orient="horizontal")

        self.canvas.create_text(
            319.999755859375,
            40.0,
            anchor="nw",
            text="Verifying Digital Signature",
            fill="#28293D",
            font=("Poppins SemiBold", 42 * -1)
        )

        self.canvas.create_text(
            95.0,
            126.837646484375,
            anchor="nw",
            text="Public Key",
            fill="#000000",
            font=("OpenSansRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            95.0,
            235.5958251953125,
            anchor="nw",
            text="Message/File hasil scan QR",
            fill="#000000",
            font=("OpenSansRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            556.0,
            456.0,
            anchor="nw",
            text="Result",
            fill="#28293D",
            font=("OpenSansRoman Bold", 26 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            600.0,
            577.9814453125,
            image=self.entry_image_1
        )

        self.entry_1 = Label(
            text="",
            bd=0,
            bg="#D9E4E8",
            fg="#000716",
            font=("OpenSansRoman Regular", 25 * -1),
            highlightthickness=0,
            justify="center"
        )
        self.entry_1.place(
            anchor="n",
            x=600,
            y=530,
            width=970,
            height=94.0,
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            600.0,
            188.5,
            image=self.entry_image_2
        )
        self.entry_2 = Text(
            bd=0,
            bg="#D9E4E8",
            fg="#000716",
            font=("OpenSansRoman Regular", 20 * -1),
            highlightthickness=0,
            xscrollcommand=scrollbar.set
        )
        self.entry_2.place(
            x=111.86170387268066,
            y=178.0,
            width=920,
            height=25.0
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            600.0,
            304.0,
            image=self.entry_image_3
        )
        self.entry_3 = Text(
            bd=0,
            bg="#D9E4E8",
            fg="#000716",
            font=("OpenSansRoman Regular", 20 * -1),
            highlightthickness=0,
            xscrollcommand=scrollbar.set
        )
        self.entry_3.place(
            x=111.86170387268066,
            y=294.0,
            width=920,
            height=25.0
        )

        self.canvas.create_text(
            95.0,
            346.0,
            anchor="nw",
            text="Digital Signature File (if digital signature in separate file)",
            fill="#000000",
            font=("OpenSansRoman Regular", 20 * -1)
        )

        self.entry_bg_4 = self.canvas.create_image(
            600.0,
            404.0,
            image=self.entry_image_3
        )
        self.entry_4 = Text(
            bd=0,
            bg="#D9E4E8",
            fg="#000716",
            font=("OpenSansRoman Regular", 20 * -1),
            highlightthickness=0,
            xscrollcommand=scrollbar.set
        )
        self.entry_4.place(
            x=111.86170387268066,
            y=394.0,
            width=920,
            height=25.0
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.master.switch_frame(guiLanding.Landing),
            relief="flat"
        )
        self.button_1.place(
            x=617.78369140625,
            y=695.80810546875,
            width=216.114501953125,
            height=68.191650390625
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: verify_pressed(),
            relief="flat"
        )
        self.button_2.place(
            x=366.0,
            y=695.80810546875,
            width=215.0653076171875,
            height=68.19140625
        )


        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: read_key(),
            relief="flat"
        )
        self.button_6.place(
            x=1050,
            y=178.0,
            width=25,
            height=25,
            anchor=NW
        )

        self.button_7 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: upload_pressed(),
            relief="flat"
        )
        self.button_7.place(
            x=1050,
            y=294.0,
            width=25,
            height=25,
            anchor=NW
        )

        self.button_8 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: read_sign(),
            relief="flat"
        )
        self.button_8.place(
            x=1050,
            y=394.0,
            width=25,
            height=25,
            anchor=NW
        )