import { Client } from 'cassandra-driver';

// Conectar ao cluster Cassandra
const client = new Client({
  contactPoints: ['127.0.0.1'],
  localDataCenter: 'datacenter1'
});

client.connect()

await client.execute(`CREATE KEYSPACE IF NOT EXISTS cc6240 WITH REPLICATION = { 'class': 'NetworkTopologyStrategy', 'replication_factor' :1};`)
await client.execute(`CREATE TABLE IF NOT EXISTS cc6240.historico_escolar ( nome text, disciplina text, codigo_disciplina int, semestre int, ano int, nota double, PRIMARY KEY ((nome), disciplina) );`); 
await client.execute('CREATE INDEX IF NOT EXISTS ON cc6240.historico_escolar (codigo_disciplina);'); 
await client.execute(`CREATE TABLE IF NOT EXISTS cc6240.historico_disciplinas ( nome_professor text, disciplina text, codigo_disciplina int, semestre int, ano int, PRIMARY KEY ((disciplina), nome_professor) );`); 
await client.execute('CREATE INDEX IF NOT EXISTS ON cc6240.historico_disciplinas (codigo_disciplina);'); 
await client.execute(`CREATE TABLE IF NOT EXISTS cc6240.formandos ( nome text, semestre int, ano int, PRIMARY KEY ((nome), semestre) );`); 
await client.execute('CREATE INDEX IF NOT EXISTS ON cc6240.formandos (ano);'); 
await client.execute(`CREATE TABLE IF NOT EXISTS cc6240.chefes_departamento ( nome_professor text, nome_departamento text, PRIMARY KEY ((nome_professor), nome_departamento) );`); 
await client.execute(`CREATE TABLE IF NOT EXISTS cc6240.grupos_tcc ( id_grupo int, nome_aluno text, nome_orientador text, PRIMARY KEY ((nome_aluno), nome_orientador) );`);

const queries = [ // Queries para a tabela historico_escolar 
"INSERT INTO cc6240.historico_escolar (nome, disciplina, codigo_disciplina, semestre, ano, nota) VALUES ('Ana', 'Matemática', 101, 1, 2023, 8.5)",
"INSERT INTO cc6240.historico_escolar (nome, disciplina, codigo_disciplina, semestre, ano, nota) VALUES ('Bruno', 'História', 102, 1, 2023, 7.0)",
"INSERT INTO cc6240.historico_escolar (nome, disciplina, codigo_disciplina, semestre, ano, nota) VALUES ('Carla', 'Física', 103, 1, 2023, 9.2)",
"INSERT INTO cc6240.historico_escolar (nome, disciplina, codigo_disciplina, semestre, ano, nota) VALUES ('Daniel', 'Química', 104, 1, 2023, 6.8)",
"INSERT INTO cc6240.historico_escolar (nome, disciplina, codigo_disciplina, semestre, ano, nota) VALUES ('Eva', 'Biologia', 105, 1, 2023, 7.9)",
 // Queries para a tabela historico_disciplinas 
"INSERT INTO cc6240.historico_disciplinas (nome_professor, disciplina, codigo_disciplina, semestre, ano) VALUES ('Prof. Silva', 'Matemática', 101, 1, 2023)",
"INSERT INTO cc6240.historico_disciplinas (nome_professor, disciplina, codigo_disciplina, semestre, ano) VALUES ('Prof. Santos', 'História', 102, 1, 2023)", 
"INSERT INTO cc6240.historico_disciplinas (nome_professor, disciplina, codigo_disciplina, semestre, ano) VALUES ('Prof. Pereira', 'Física', 103, 1, 2023)",
"INSERT INTO cc6240.historico_disciplinas (nome_professor, disciplina, codigo_disciplina, semestre, ano) VALUES ('Prof. Souza', 'Química', 104, 1, 2023)", 
"INSERT INTO cc6240.historico_disciplinas (nome_professor, disciplina, codigo_disciplina, semestre, ano) VALUES ('Prof. Costa', 'Biologia', 105, 1, 2023)", 
// Queries para a tabela formandos 
"INSERT INTO cc6240.formandos (nome, semestre, ano) VALUES ('Ana', 2, 2023)", 
"INSERT INTO cc6240.formandos (nome, semestre, ano) VALUES ('Bruno', 2, 2023)", 
"INSERT INTO cc6240.formandos (nome, semestre, ano) VALUES ('Carla', 2, 2023)", 
"INSERT INTO cc6240.formandos (nome, semestre, ano) VALUES ('Daniel', 2, 2023)", 
"INSERT INTO cc6240.formandos (nome, semestre, ano) VALUES ('Eva', 2, 2023)", 
// Queries para a tabela chefes_departamento 
"INSERT INTO cc6240.chefes_departamento (nome_professor, nome_departamento) VALUES ('Prof. Silva', 'Matemática')", 
"INSERT INTO cc6240.chefes_departamento (nome_professor, nome_departamento) VALUES ('Prof. Santos', 'História')", 
"INSERT INTO cc6240.chefes_departamento (nome_professor, nome_departamento) VALUES ('Prof. Pereira', 'Física')", 
"INSERT INTO cc6240.chefes_departamento (nome_professor, nome_departamento) VALUES ('Prof. Souza', 'Química')", 
"INSERT INTO cc6240.chefes_departamento (nome_professor, nome_departamento) VALUES ('Prof. Costa', 'Biologia')", 
// Queries para a tabela grupos_tcc 
"INSERT INTO cc6240.grupos_tcc (id_grupo, nome_aluno, nome_orientador) VALUES (1, 'Ana', 'Prof. Silva')", 
"INSERT INTO cc6240.grupos_tcc (id_grupo, nome_aluno, nome_orientador) VALUES (1, 'Bruno', 'Prof. Silva')", 
"INSERT INTO cc6240.grupos_tcc (id_grupo, nome_aluno, nome_orientador) VALUES (2, 'Carla', 'Prof. Santos')", 
"INSERT INTO cc6240.grupos_tcc (id_grupo, nome_aluno, nome_orientador) VALUES (2, 'Daniel', 'Prof. Santos')", 
"INSERT INTO cc6240.grupos_tcc (id_grupo, nome_aluno, nome_orientador) VALUES (3, 'Eva', 'Prof. Pereira')"];

for (const query of queries) {
  await client.execute(query);
  console.log(query) 
}

await client.shutdown();
console.log("Sucesso ao criar o keyspace")

