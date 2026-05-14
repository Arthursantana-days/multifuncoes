# Autor: Arthur Santana
import customtkinter as ctk 
import requests 

# Configuração visual
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Janela principal
app = ctk.CTk()
app.title("Sistema Multi Funções")
app.geometry("800x600")
# frame Menu (esquerda)
frame_menu = ctk.CTkFrame(app, width=200, fg_color= "#FFE1B2")
frame_menu.pack(side="left", fill="y")

# frame Conteúdo
frame_conteudo = ctk.CTkFrame(app, fg_color= "#f1ffdc")
frame_conteudo.pack(side = "right", fill="both", expand = True)
# botões
ctk.CTkButton(frame_menu, text="Juros Simples", fg_color= "#543200").pack(pady=10, padx=10)
# Loop
app.mainloop()