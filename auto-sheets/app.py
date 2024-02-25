import openpyxl
from PIL import Image, ImageDraw, ImageFont

workbook_alunos = openpyxl.load_workbook('planilhas/planilha_alunos.xlsx')
sheet_alunos = workbook_alunos['Sheet1']

for indice, linha in enumerate(sheet_alunos.iter_rows(min_row=2)):
    #Acessar cada celula que precisamos
    nome_curso = linha[0].value
    nome_participante = linha[1].value
    tipo_participacao = linha[2].value
    carga_horaria = linha[5].value

    data_inicio = linha[3].value
    data_fim = linha[4].value

    data_emicao = linha[6].value

    #Transferir os dados da planilha para a imagem do certificado
    #Fonte a ser usada
    fonte_nome = ImageFont.truetype('./tahomabd.ttf', 90)
    fonte_geral = ImageFont.truetype('./tahoma.ttf', 80)
    fonte_data = ImageFont.truetype('./tahoma.ttf', 55)


    image = Image.open('./certificado_padrao.jpg')
    desenhar = ImageDraw.Draw(image)
    desenhar.text((1015, 827), nome_participante, fill='black', font=fonte_nome)
    desenhar.text((1060, 950), nome_curso, fill='black', font=fonte_geral)
    desenhar.text((1425, 1070), nome_participante, fill='black', font=fonte_geral)
    desenhar.text((1480, 1190), str(carga_horaria), fill='black', font=fonte_geral)

    desenhar.text((700, 1750), str(data_inicio), fill='black', font=fonte_geral)
    desenhar.text((700, 1900), str(data_fim), fill='black', font=fonte_geral)

    desenhar.text((2150, 1900), str(data_emicao), fill='black', font=fonte_geral)




    image.save(f'./{indice} {nome_participante} certificado.png')




