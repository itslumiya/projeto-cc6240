import subprocess; import sys; import importlib.util

def check_and_install_packages(packages, script_path):
    """
    Verifica se todas as bibliotecas ja estao instaladas.
    """
    missing_packages = []
    for package in packages:
        spec = importlib.util.find_spec(package)
        if spec is None:  # Package not found
            missing_packages.append(package)

    if missing_packages:
        print(f"Os seguintes pacotes não estão instalados: {', '.join(missing_packages)}")
        print(f"Executando o script {script_path} para instalar os pacotes...")

        try:
            subprocess.run([script_path], check=True)  # Run the .bat script
            print("Instalação concluída.")

            # Verify again and print messages accordingly
            for package in packages: # check novamente se estão instalados
                spec = importlib.util.find_spec(package)
                if spec is not None:
                    print(f"{package} está instalado.")
                else:
                    print(f"Erro ao instalar {package}. Certifique-se de que o script de instalação esteja correto.") # Erro na instalação de alguma biblioteca em especifico

        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar o script {script_path}: {e}")
            sys.exit(1) # Finaliza o programa caso erro na instalação das bibliotecas em geral
        except FileNotFoundError: # Erro na localização do arquivo
            print(f"Arquivo em {script_path} não encontrado. Verifique se o caminho está correto.")
            sys.exit(1) # Finaliza o programa caso erro na localização do arquivo
    else:
        print("Todos os pacotes necessários já estão instalados.")

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from faker import Faker; import random
import keyring; import os; from time import sleep

def get_conn(usern, passw):
    # Conectar ao MongoDB usando a URI fornecida
    uri = f"mongodb+srv://{usern}:{passw}@documentstore.a4qzd.mongodb.net/?retryWrites=true&w=majority&appName=documentstore"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['universidade']
    try: 
        db.admin.command('ping') 
        print("Pinged your deployment. You successfully connected to MongoDB!") 
    except Exception as e:
        print(e)
    return db

def popula_banco(usern, passw):
        db = get_conn(usern, passw)

        try:
            db.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

        # Listas de cursos, disciplinas e departamentos
        cursos = [
            "Engenharia Mecanica", 
            "Ciencias da Computacao", 
            "Administracao", 
            "Engenharia da Computacao", 
            "Ciencia de Dados"]

        disciplinas = [
            "Calculo I", 
            "Calculo II", 
            "Calculo III", 
            "Calculo IV", 
            "Calculo V", 
            "Financas", 
            "Estatistica", 
            "Fisica", 
            "Engenharia de Software", 
            "Fundamentos de Algoritmo", 
            "Desenvolvimento de Algoritmo", 
            "Computacao Movel", 
            "Algebra Linear",
            "Banco de Dados",
            "Fisica II",
            "Geometria Analitica",
            "Compiladores"]

        departamentos = [
            "Tecnologias", 
            "Engenharias"]

        # Função para gerar um nome aleatório
        def gerar_nome():
            # Criar um objeto Faker
            fake = Faker()
            # Gerar um nome aleatório
            nome = fake.name()
            return nome

        def gerar_registros(qtd_alunos, qtd_professores):
            registros = []
            for _ in range(qtd_alunos):
                curso = random.choice(cursos)
                historico = [{
                    "disciplina": random.choice(disciplinas), 
                    "semestre": random.choice(["1", "2"]),
                    "ano": random.randint(2020, 2023), 
                    "nota_final": random.uniform(0, 10)} 
                    for _ in range(5)]
                registros.append({
                    "tipo": "aluno",
                    "nome": gerar_nome(),
                    "curso": curso,
                    "disciplinas": [item["disciplina"] for item in historico],
                    "historico_escolar": historico
                })

            for _ in range(qtd_professores):
                registros.append({
                    "tipo": "professor",
                    "nome": gerar_nome(),
                    "departamento": random.choice(departamentos),
                    "disciplinas": random.sample(disciplinas, k=3),
                    "disciplinas_ministradas": [{
                        "disciplina": random.choice(disciplinas), 
                        "semestre": random.choice(["1", "2"]), 
                        "ano": random.randint(2020, 2023)} for _ in range(3)],
                    "chefe_departamento": random.choice([True, False])
                })

            return registros

        # Função para adicionar grupos de TCC
        def adicionar_grupos_tcc():
            grupos_tcc = []
            for i in range(1, 11):  # Supondo que temos 10 grupos de TCC
                alunos = random.sample(list(db.usuarios.find({"tipo": "aluno"})), 5)
                orientador = random.choice(list(db.usuarios.find({"tipo": "professor"})))
                grupo = {
                    "grupo_id": f"Grupo_{i}",
                    "alunos": [aluno["nome"] for aluno in alunos],
                    "orientador": orientador["nome"]
                }
                grupos_tcc.append(grupo)
            db.grupos_tcc.insert_many(grupos_tcc)

        # Adicionar matrizes curriculares ao banco de dados
        matriz_curricular = {
            "Engenharia Mecanica": ["Calculo I", "Calculo II", "Calculo III", "Fisica", "Algebra Linear", "Banco de Dados", "Fisica II", "Geometria Analitica", "Compiladores", "Calculo IV", "Calculo V"],
            "Ciencias da Computacao": ["Fundamentos de Algoritmo", "Desenvolvimento de Algoritmo", "Computacao Movel", "Engenharia de Software", "Algebra Linear", "Banco de Dados", "Fisica II", "Geometria Analitica", "Compiladores", "Calculo IV", "Calculo V"],
            "Administracao": ["Financas", "Estatistica", "Calculo I", "Calculo II", "Calculo III", "Banco de Dados", "Fisica II", "Geometria Analitica", "Compiladores", "Calculo IV", "Calculo V"],
            "Engenharia da Computacao": ["Calculo I", "Calculo II", "Calculo III", "Calculo IV", "Engenharia de Software", "Banco de Dados", "Fisica II", "Geometria Analitica", "Compiladores", "Calculo V"],
            "Ciencia de Dados": ["Estatistica", "Calculo I", "Calculo II", "Fundamentos de Algoritmo", "Ciencia de Dados Avancada", "Banco de Dados", "Fisica II", "Geometria Analitica", "Compiladores", "Calculo IV", "Calculo V"]
        }

        for curso, disciplinas in matriz_curricular.items():
            db.matrizes_curriculares.insert_one({
                "curso": curso,
                "disciplinas": disciplinas
            })
        # Gerados dados aleatorios
        registros = gerar_registros(185, 15)

        # Inserir registros no MongoDB
        db.usuarios.insert_many(registros)
        adicionar_grupos_tcc()

        print("Banco de dados populado com sucesso!")
        print("Limpando terminal...")
        sleep(3)
        # Limpar o terminal
        os.system('cls')

if __name__ == "__main__":
    popula_banco()