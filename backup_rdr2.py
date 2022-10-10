from pathlib import Path
import shutil
import os
import time


def check_folder(hoje_nome_do_diretorio):
	diretorio_origem = Path(r"C:\Users\USER\Documents\Rockstar Games\Red Dead Redemption 2\Profiles\PASTACOMNOMEDEUSUARIO") #pasta com config e saves (checar diretório de save do RDR2)
	diretorio = Path (r"D:\Folder Temp\RDR2") #pasta de backup
	path = os.path.join(diretorio, hoje_nome_do_diretorio)#pasta backup + pasta do dia
	checar_pasta = os.path.isdir(path) #checando se o caminho existe
	if not checar_pasta: #se o backup não ter sido feito no dia, ele assim fará
		shutil.copytree(diretorio_origem, path, dirs_exist_ok=True)
		return
	else:
		return


hoje_nome_do_diretorio = str(time.strftime('%Y-%m-%d')) #nome da pasta com data no formato Ano-Mês-Dia
check_folder(hoje_nome_do_diretorio)