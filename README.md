# Projeto de Tópicos Avançados de Banco de Dados

Thiago Garcia Santana - 22.122.003-1 <br>
Márcio Forner Nepomuceno Almeida - 22.122.040-3 <br>
Livia Lumi Miyabara - 22.122.045-2 <br>

## Projeto 3 - Graph Database

#### Coleções usadas para armazenar os dados
`(<label_nome>:Professor {nome:"nome professor"}),` - Professor <br>
`(<label_departamento>:Departamento {nome:"nome departamento"}),` - Departamento <br>
`(<label_curso>:Curso {nome:"nome curso"}),` - Curso <br>
`(<label_disciplina>:Disciplina {nome:"nome disciplina"}),` - Disciplina <br>
`(<label_tcc>:TCC {nome:"nome tcc"}),` - TCC <br>
`(<label_aluno>: {nome:"nome aluno", ra: "123456", semestre: x}),` - Aluno <br>

#### Relações
`(Professor)-[:CHEFIA]->(Departamento)` <br>
`(Professor)-[:FAZ_PARTE]->(Departamento)` <br>
`(Curso)-[:PERTENCE_A]->(Departamento)` <br>
`(Professor)-[:ORIENTOU]->(TCC)` <br>
`(Aluno)-[:DESENVOLVEU]->(TCC)` <br>
`(Aluno)-[:MATRICULADO]->(Curso)` <br>
`(Professor)-[:LECIONA]->(Disciplina)` <br>
`(Disciplina)-[:FAZ_PARTE]->(Departamento)` <br>
`(Curso)-[:POSSUI {semestre: x}]->(Disciplina)` <br>
`(Aluno)-[:REALIZOU {Ano: xxxx, Semestre: x, Nota: x.y}]->(Disciplina),` <br>

#### Como executar o projeto Graph Database (neo4j)
OBS: É necessário ter o Docker Desktop instalado para executar o projeto.
Para executar o projeto de Graph Database, siga os seguintes passos:

1. Faça o download da pasta GraphDatabase
2. Após o download, na pasta GraphDatabase, abra o cmd e execute o comando `docker-compose up` e aguarde
3. Após subir o contêiner, dê um start no Docker Desktop e acesse o localhost na porta 7474:7474 (`http://localhost:7474/`)
4. Por fim, execute o comando `pyhton ExecutarProjeto.python`
