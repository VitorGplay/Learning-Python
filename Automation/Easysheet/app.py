import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk  # Importar ttk para usar Progressbar
import openpyxl
from PIL import Image, ImageDraw, ImageFont

# Função para selecionar o arquivo .xlsx
def select_excel_file():
    filename = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if filename:
        excel_entry.delete(0, "end")  # Limpa a entrada antes de definir o novo valor
        excel_entry.insert(0, filename)  # Insere o novo valor na entrada

# Função para selecionar o local e o nome do arquivo .png
def select_folder():
    foldername = filedialog.askdirectory()
    if foldername:
        folder_entry.delete(0, tk.END)  # Limpa a entrada antes de definir o novo valor
        folder_entry.insert(0, foldername)  # Insere o novo valor na entrada

# Função para processar o arquivo .xlsx e gerar os arquivos .png
def process_files():
    excel_filename = excel_entry.get()
    folder_path = folder_entry.get()

    if excel_filename and folder_path:
        try:
            workbook = openpyxl.load_workbook(excel_filename)
            sheet = workbook.active
            total_rows = sheet.max_row - 1  # Excluindo a primeira linha de cabeçalho
            progress_bar["maximum"] = total_rows

            for indice, linha in enumerate(sheet.iter_rows(min_row=2), start=1):
                progress_bar["value"] = indice
                progress_label.configure(text=f"Progresso: {indice}/{total_rows}")
                progress_bar.update_idletasks()

                nome_curso = linha[0].value
                nome_participante = linha[1].value
                tipo_participacao = linha[2].value
                carga_horaria = linha[5].value
                data_inicio = linha[3].value
                data_fim = linha[4].value
                data_emissao = linha[6].value

                fonte_nome = ImageFont.truetype('./fontes/tahomabd.ttf', 90)
                fonte_geral = ImageFont.truetype('./fontes/tahoma.ttf', 80)
                fonte_data = ImageFont.truetype('./fontes/tahoma.ttf', 55)

                image = Image.open('./certificado_padrao.jpg')
                draw = ImageDraw.Draw(image)
                draw.text((1015, 827), nome_participante, fill='black', font=fonte_nome)
                draw.text((1060, 950), nome_curso, fill='black', font=fonte_geral)
                draw.text((1425, 1070), tipo_participacao, fill='black', font=fonte_geral)
                draw.text((1480, 1190), str(carga_horaria), fill='black', font=fonte_geral)
                draw.text((750, 1785), str(data_inicio), fill='black', font=fonte_data)
                draw.text((750, 1930), str(data_fim), fill='black', font=fonte_data)
                draw.text((2230, 1930), str(data_emissao), fill='black', font=fonte_data)

                image.save(f'{folder_path}/{indice} {nome_participante} certificado.png')

            messagebox.showinfo("Concluído", "Certificados gerados com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

# Criar a janela principal
root = ctk.CTk()
root.title("Gerador de Certificados")
root.geometry("600x300")

# Rótulos e entradas para selecionar o arquivo .xlsx e o local para salvar os arquivos .png
excel_label = ctk.CTkLabel(root, text="Selecione o arquivo .xlsx :")
excel_label.grid(row=0, column=0, padx=5, pady=5)
excel_entry = ctk.CTkEntry(root, width=50)
excel_entry.grid(row=0, column=1, padx=5, pady=5)
excel_button = ctk.CTkButton(root, text="Selecionar", command=select_excel_file)
excel_button.grid(row=0, column=2, padx=5, pady=5)

folder_label = ctk.CTkLabel(root, text="Selecione a pasta para salvar os certificados:")
folder_label.grid(row=1, column=0, padx=5, pady=5)
folder_entry = ctk.CTkEntry(root, width=50)
folder_entry.grid(row=1, column=1, padx=5, pady=5)
folder_button = ctk.CTkButton(root, text="Selecionar", command=select_folder)
folder_button.grid(row=1, column=2, padx=5, pady=5)

# Botão para iniciar o processamento
process_button = ctk.CTkButton(root, text="Gerar Certificados", command=process_files)
process_button.grid(row=2, column=1, padx=5, pady=5)

# Barra de progresso
progress_label = ctk.CTkLabel(root, text="Progresso: 0/0")
progress_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# Iniciar a interface gráfica
root.mainloop()
