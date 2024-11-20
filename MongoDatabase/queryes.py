from pymongo.mongo_client import MongoClient; from pymongo.server_api import ServerApi
import warnings; warnings.filterwarnings("ignore", category=DeprecationWarning) # Suprimir warnings específicos 
import keyring; import pandas as pd
import os; user = os.getlogin()
import subprocess; import sys

def options():
    print('''1 - Historico escolar do aluno
2 - Disciplinas por professor
3 - Alunos formados e aprovados
4 - Professores chefes de departamentos
5 - Grupos de TCC ativos
6 - Popular banco
0 - Leave
''')

def historico_escolar_aluno(db):
    nome_aluno = input('Digite o nome do aluno: ')
    teste = []
    teste.append(nome_aluno)
    nome = teste[0].split()
    
    print('\n-------------------------- Resultado da query --------------------------\n')
    if len(nome) == 1:
        alunos = db.usuarios.find({"tipo": "aluno"})
        resultados = []
        for aluno in alunos:
            nome_completo = aluno["nome"]
            if nome_completo.split()[0].lower() == nome[0].lower():
                for historico in aluno["historico_escolar"]:
                    resultados.append({
                        "Aluno": aluno["nome"],
                        "Disciplina": historico["disciplina"],
                        "Semestre": historico["semestre"],
                        "Ano": historico["ano"],
                        "Nota Final": historico["nota_final"]
                    })
        df_resultados = pd.DataFrame(resultados)
        if df_resultados.empty:
            print(f"Nenhum histórico encontrado para o aluno com o primeiro nome {nome[0]}.")
        else:
            print(df_resultados)
            
    elif len(nome) == 2:
        aluno = db.usuarios.find_one({"tipo": "aluno", "nome": nome_aluno})
        if aluno:
            df_historico = pd.DataFrame(aluno["historico_escolar"])
            if df_historico.empty:
                print(f"Nenhum histórico encontrado para o aluno {nome_aluno}.")
            else:
                print(df_historico)
        else:
            print(f"Aluno {nome_aluno} não encontrado.")
    else:
        print("Formato de nome inválido.")

def historico_disciplinas_professor(db):
    nome_professor = input('Digite o nome de um professor: ')
    teste = []
    teste.append(nome_professor)
    nome = teste[0].split()
    
    print('\n-------------------------- Resultado da query --------------------------\n')
    if len(nome) == 1:
        professores = db.usuarios.find({"tipo": "professor"})
        resultados = []
        for professor in professores:
            nome_completo = professor["nome"]
            if nome_completo.split()[0].lower() == nome[0].lower():
                for ministrada in professor["disciplinas_ministradas"]:
                    resultados.append({
                        "Professor": professor["nome"],
                        "Disciplina": ministrada["disciplina"],
                        "Semestre": ministrada["semestre"],
                        "Ano": ministrada["ano"]
                    })
        df_resultados = pd.DataFrame(resultados)
        if df_resultados.empty:
            print(f"Nenhuma disciplina ministrada encontrada para o professor com o primeiro nome {nome[0]}.")
        else:
            print(df_resultados)
            
    elif len(nome) == 2:
        professor = db.usuarios.find_one({"tipo": "professor", "nome": nome_professor})
        if professor:
            df_disciplinas = pd.DataFrame(professor["disciplinas_ministradas"])
            if df_disciplinas.empty:
                print(f"Nenhuma disciplina ministrada encontrada para o professor {nome_professor}.")
            else:
                print(df_disciplinas)
        else:
            print(f"Professor {nome_professor} não encontrado.")
    else:
        print("Formato de nome inválido.")

def alunos_formados(db):
    semestre = input('Digite um semestre: ')
    ano = input('Digite um ano: ')
    cursos_matriz = list(db.matrizes_curriculares.find({}, {"_id": 0, "curso": 1}))
    formados = []
    for curso in cursos_matriz:
        alunos = db.usuarios.find({"tipo": "aluno", "curso": curso["curso"]})
        for aluno in alunos:
            historico = aluno.get("historico_escolar", [])
            aprovado_em_todas = all(disciplina["nota_final"] >= 5.0 for disciplina in historico if disciplina["semestre"] == semestre and disciplina["ano"] == ano)
            if aprovado_em_todas:
                formados.append(aluno["nome"])
    print('\n-------------------------- Resultado da query --------------------------\n')
    return print(pd.DataFrame(formados))

def professores_chefes_departamento(db):
    chefes = db.usuarios.find({"tipo": "professor", "chefe_departamento": True})
    print('\n-------------------------- Resultado da query --------------------------\n')
    return print(pd.DataFrame([{"nome": chefe["nome"], "departamento": chefe["departamento"]} for chefe in chefes]))

def grupos_tcc(db):
    grupos = db.grupos_tcc.find()
    print('\n-------------------------- Resultado da query --------------------------\n')
    return print(pd.DataFrame([{"grupo_id": grupo["grupo_id"], "alunos": grupo["alunos"], "orientador": grupo["orientador"]} for grupo in grupos]))