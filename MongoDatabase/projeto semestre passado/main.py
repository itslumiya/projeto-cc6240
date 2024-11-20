import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="juninho",
    password="1234",
    host="localhost",
    port="5432"
)

cur = conn.cursor()


# 1
create_table_query = """
CREATE TABLE Departamento (
    id int,
    nome varchar,
    PRIMARY KEY (id)
);
"""
cur.execute(create_table_query)

#2
create_table_query = """
CREATE TABLE Curso (
    id int,
    nome varchar,
    id_departamento int,
    PRIMARY KEY (id),
    FOREIGN KEY (id_departamento) REFERENCES Departamento(id)
);
"""
cur.execute(create_table_query)

# 3
create_table_query = """
CREATE TABLE Aluno (
    id int,
    nome varchar,
    sobrenome varchar,
    id_curso int,
    PRIMARY KEY (id),
    FOREIGN KEY (id_curso) REFERENCES Curso(id)
);
"""
cur.execute(create_table_query)

# 4 
create_table_query = """
CREATE TABLE Professor (
    id int,
    nome varchar,
    sobrenome varchar,
    id_departamento int,
    PRIMARY KEY (id),
    FOREIGN KEY (id_departamento) REFERENCES Departamento(id)
);
"""
cur.execute(create_table_query)

# 5
create_table_query = """
CREATE TABLE Disciplina (
    id int,
    nome varchar,
    id_departamento int,
    id_professor int,
    PRIMARY KEY (id),
    FOREIGN KEY (id_departamento) REFERENCES Departamento(id),
    FOREIGN KEY (id_professor) REFERENCES Professor(id)
);
"""
cur.execute(create_table_query)

# 6
create_table_query = """
CREATE TABLE Tcc (
    id int,
    titulo varchar,
    id_professor int,
    PRIMARY KEY (id),
    FOREIGN KEY (id_professor) REFERENCES Professor(id)
);
"""
cur.execute(create_table_query)

# 7
create_table_query = """
CREATE TABLE GrupoTcc (
    id_aluno int,
    id_tcc int,
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id),
    FOREIGN KEY (id_tcc) REFERENCES Tcc(id)
);
"""
cur.execute(create_table_query)

# 8
create_table_query = """
CREATE TABLE MatrizCurricular (
    id_curso int,
    id_disciplina int,
    semestre int,
    ano int,
    FOREIGN KEY (id_curso) REFERENCES Curso(id),
    FOREIGN KEY (id_disciplina) REFERENCES Disciplina(id)
);
"""
cur.execute(create_table_query)

#9

create_table_query = """
CREATE TABLE HistoricoEscolar (
    id_aluno int,
    id_disciplina int,
    semestre int,
    ano int,
    nota float,
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id),
    FOREIGN KEY (id_disciplina) REFERENCES Disciplina(id)
);
"""
cur.execute(create_table_query)





# Popular os dados 
insert = """
INSERT INTO Departamento VALUES (1, 'Tecnologia');
"""
cur.execute(insert)

insert = """
INSERT INTO Departamento VALUES (2, 'Engenharias');
"""
cur.execute(insert)

insert = """
INSERT INTO Curso VALUES (11, 'Ciencias da computacao', 1);
"""
cur.execute(insert)

insert = """
INSERT INTO Curso VALUES (21, 'Engenharia mecanica', 2);
"""
cur.execute(insert)


insert = """
INSERT INTO Aluno VALUES (111, 'Marcio', 'Forner', 11);
"""
cur.execute(insert)

insert = """
INSERT INTO Aluno VALUES (211, 'Thiago', 'Garcia', 21);
"""
cur.execute(insert)

insert = """
INSERT INTO Professor VALUES (1111, 'Leonardo', 'Anjoleto', 1);
"""
cur.execute(insert)
insert = """
INSERT INTO Professor VALUES (1112, 'Danilo', 'Pereira', 1);
"""
cur.execute(insert)

insert = """
INSERT INTO Professor VALUES (2111, 'Ariovaldo', 'Junior', 2);
"""
cur.execute(insert)
insert = """
INSERT INTO Professor VALUES (2112, 'Antonio', 'Neto', 2);
"""
cur.execute(insert)

insert = """
INSERT INTO Disciplina VALUES (11111, 'Fundamentos de algoritmo', 1, 1111);
"""
cur.execute(insert)

insert = """
INSERT INTO Disciplina VALUES (11113, 'Desenvolvimento de algoritmo', 1, 1111);
"""
cur.execute(insert)

insert = """
INSERT INTO Disciplina VALUES (11112, 'Computação movel', 1, 1112);
"""
cur.execute(insert)

insert = """
INSERT INTO Disciplina VALUES (21111, 'Algebra Linear', 2, 2111);
"""
cur.execute(insert)

insert = """
INSERT INTO Tcc VALUES (111111, 'Work Again', 1111);
"""
cur.execute(insert)

insert = """
INSERT INTO GrupoTcc VALUES (111, 111111);
"""
cur.execute(insert)

insert = """
INSERT INTO GrupoTcc VALUES (211, 111111);
"""
cur.execute(insert)

insert = """
INSERT INTO MatrizCurricular VALUES (11, 11111, 1, 2022);
"""
cur.execute(insert)
insert = """
INSERT INTO MatrizCurricular VALUES (11, 11113, 3, 2023);
"""
cur.execute(insert)


insert = """
INSERT INTO MatrizCurricular VALUES (11, 11112, 2, 2022);
"""
cur.execute(insert)

insert = """
INSERT INTO HistoricoEscolar VALUES (111, 11111, 1, 2022, 5.0);
"""
cur.execute(insert)

insert = """
INSERT INTO HistoricoEscolar VALUES (111, 11112, 2, 2022, 7.0);
"""
cur.execute(insert)

insert = """
INSERT INTO HistoricoEscolar VALUES (111, 11113, 3, 2023, 7.0);
"""
cur.execute(insert)

insert = """
INSERT INTO HistoricoEscolar VALUES (211, 21111, 1, 2023, 4.0);
"""
cur.execute(insert)

alter_table_query = """
ALTER TABLE Departamento ADD id_professor_chefe int;
ALTER TABLE Departamento ADD CONSTRAINT fk_professor FOREIGN KEY(id_professor_chefe) REFERENCES Professor(id);
"""
cur.execute(alter_table_query)

update_values = """
UPDATE Departamento
SET id_professor_chefe = 1111
WHERE id = 1
"""
cur.execute(update_values)

update_values = """
UPDATE Departamento
SET id_professor_chefe = 2111
WHERE id = 2
"""
cur.execute(update_values)

conn.commit()

conn.close()


print("Sucesso")