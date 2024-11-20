import subprocess; import sys; import subprocess; import importlib.util
from popula_banco import popula_banco, get_conn, check_and_install_packages
required_packages = ["pandas", "keyring", "faker", "pymongo"]; batch_script_path = "libs.bat" 
check_and_install_packages(required_packages, batch_script_path)
from queryes import historico_disciplinas_professor, professores_chefes_departamento, alunos_formados, grupos_tcc, historico_escolar_aluno, options
from pymongo.mongo_client import MongoClient; from pymongo.server_api import ServerApi
import warnings; warnings.filterwarnings("ignore", category=DeprecationWarning) # Suprimir warnings específicos 
import keyring; import os; user = os.getlogin()

usern = 'thiaguera1' # -> Colocar username aqui e na biblioteca popula_banco
passw = keyring.get_password("MONGO_DB", usern) # -> Colocar senha aqui e na biblioteca popula_banco, ou registrar nas credenciais do windows
db = get_conn(usern, passw)

# Limpar o terminal
os.system('cls')

while True:
    print('\ndigite uma das opções de query: \n')
    options()
    try:
        choose = int(input('Opção: '))

        if choose == 0:
            break
        elif choose == 1:
            popula_banco(usern, passw)
        elif choose == 2:
            historico_disciplinas_professor(db)
        elif choose == 3:
            formados_df = alunos_formados(db)
        elif choose == 4:
            professores_chefes_departamento(db)
        elif choose == 5:
            grupos_tcc(db)
        elif choose == 6:
            historico_escolar_aluno(db)
        else:
            print('Digite uma opção válida.')
            
    except ValueError:
        print('Digite um número inteiro válido.')

    
