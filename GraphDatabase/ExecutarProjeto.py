from neo4j import GraphDatabase

uri = "neo4j://localhost:7687"
username = "neo4j"
password = "senha1234"
driver = GraphDatabase.driver(uri, auth=(username, password))

def obterQueryCypher():
    with open("neo4j.cypher", 'r', encoding='utf-8') as file:
        return file.read()

def popularBanco():
    with driver.session() as session:
        print("Obtendo query para popular o banco...")
        query = obterQueryCypher()
        print("Populado o banco...")
        try:
            session.run(query)
            print("Banco populado com sucesso :)\n")
        except exceptions.Neo4jError as e:
            print(f"Erro ao popular o banco: {e}")

def limparBanco():
    with driver.session() as session:
        query = """
                MATCH (n) 
                DETACH DELETE n
                """
        try:
            session.run(query)
        except exceptions.Neo4jError as e:
            print(f"Erro ao limpar o banco: {e}")

# histórico escolar de qualquer aluno, retornando o código e nome da disciplina, semestre e ano que a disciplina foi cursada e nota final
def obterHistoricoEscolar():
    print("\n======================================")
    print("      HISTÓRICO DE ALUNOS            ".center(38))
    print("======================================\n")
    with driver.session() as session:
        query = """
                MATCH (aluno:Aluno)-[rel:REALIZOU]->(disciplina:Disciplina)
                RETURN 
                    aluno.nome AS NomeAluno, 
                    disciplina.codigo AS CodigoDisciplina, 
                    disciplina.nome AS NomeDisciplina, 
                    rel.Semestre AS Semestre,
                    rel.Ano AS Ano,
                    rel.Nota AS NotaFinal
                ORDER BY aluno.nome ASC, rel.Ano ASC, rel.Semestre ASC
                """
        result = session.run(query)
        
        for record in result:
            print(f"{record['NomeAluno']} - {record['NomeDisciplina']} ({record['CodigoDisciplina']}) | {record['Semestre']}º semestre de {record['Ano']} | Nota final: {record['NotaFinal']}")

# histórico de disciplinas ministradas por qualquer professor, com semestre e ano
def obterDisciplinasMinistradas():
    print("\n======================================")
    print("      DISCIPLINAS MINISTRADAS        ".center(38))
    print("======================================\n")
    with driver.session() as session:
        query = """
                MATCH 
                    (professor:Professor)-[:LECIONA]->(disciplina:Disciplina)<-[rel:REALIZOU]-(aluno:Aluno)
                RETURN 
                    DISTINCT professor.nome AS NomeProfessor,
                    disciplina.codigo AS CodigoDisciplina,
                    disciplina.nome AS NomeDisciplina,
                    rel.Ano AS Ano,
                    rel.Semestre AS Semestre
                ORDER BY professor.nome ASC, disciplina.codigo, rel.Ano ASC, rel.Semestre ASC
                """
        result = session.run(query)
        
        for record in result:
            print(f"{record['NomeDisciplina']} | Ministrada no {record['Semestre']}º semestre de {record['Ano']} por {record['NomeProfessor']}")

# listar alunos que já se formaram (foram aprovados em todos os cursos de uma matriz curricular) em um determinado semestre de um ano
def obterAlunosAprovados():
    print("\n======================================")
    print("        ALUNOS FORMADOS              ".center(38))
    print("======================================\n")
    with driver.session() as session:
        query = """
                MATCH (aluno:Aluno)-[:MATRICULADO]->(curso:Curso)-[:POSSUI]->(disciplina:Disciplina)
                MATCH (aluno)-[:REALIZOU]->(disciplina)
                WHERE EXISTS {
                    MATCH (aluno)-[rel:REALIZOU]->(disciplina)
                    WHERE rel.Nota >= 5
                }
                WITH aluno, curso, COLLECT(DISTINCT disciplina) AS disciplinasRealizadas
                MATCH (curso)-[:POSSUI]->(todasDisciplinas:Disciplina)
                WITH aluno, curso, disciplinasRealizadas, COLLECT(todasDisciplinas) AS todasDisciplinas
                WHERE SIZE(disciplinasRealizadas) = SIZE(todasDisciplinas)

                MATCH (curso)-[:POSSUI]->(ultimaDisciplina:Disciplina)
                WHERE ultimaDisciplina IN disciplinasRealizadas
                WITH aluno, curso, ultimaDisciplina
                ORDER BY ultimaDisciplina.semestre DESC, ultimaDisciplina.codigo DESC

                WITH aluno, curso, COLLECT(ultimaDisciplina)[0] AS ultimaDisciplina

                MATCH (aluno)-[rel:REALIZOU]->(ultimaDisciplina)
                RETURN aluno.nome AS nome_aluno, curso.nome AS nome_curso, rel.Ano AS ano, rel.Semestre AS semestre
                ORDER BY aluno.nome ASC
                """
        result = session.run(query)
        
        for record in result:
            print(f"{record['nome_aluno']} | Formado em {record['nome_curso']} no {record['semestre']}º semestre de {record['ano']}")

# listar todos os professores que são chefes de departamento, junto com o nome do departamento
def obterChefesDepto():
    print("\n======================================")
    print("         CHEFES DE DEPTO             ".center(38))
    print("======================================\n")
    with driver.session() as session:
        query = """
                MATCH (pessoa:Professor)-[:CHEFIA]->(departamento:Departamento)
                RETURN pessoa.nome AS NomeProfessor, departamento.nome AS NomeDepartamento
                """
        result = session.run(query)
        
        for record in result:
            print(f"{record['NomeDepartamento']} é chefiado por {record['NomeProfessor']}")

# saber quais alunos formaram um grupo de TCC e qual professor foi o orientador
def obterGruposTcc():
    print("\n======================================")
    print("         GRUPOS DE TCC              ".center(38))
    print("======================================\n")
    with driver.session() as session:
        query = """
                MATCH (a:Aluno)-[:DESENVOLVEU]->(t:TCC)<-[:ORIENTOU]-(p:Professor)
                WITH t.nome AS TCC, p.nome AS Orientador, collect(a.nome) AS Alunos
                RETURN TCC, Orientador, Alunos
                """
        result = session.run(query)
        
        for record in result:
            alunos = ", ".join(record['Alunos'])
            print(f"TCC: {record['TCC']} | Orientador: {record['Orientador']} | Alunos: {alunos}")

popularBanco()
obterHistoricoEscolar()
obterDisciplinasMinistradas()
obterAlunosAprovados()
obterChefesDepto
obterGruposTcc()
limparBanco()