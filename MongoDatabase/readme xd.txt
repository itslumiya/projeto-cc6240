readme xd

--------------------------------------------------------------------------

Coleções criadas:
grupos_tcc -> armazena 10 grupos de TCC com 5 alunos e 1 orientador.
matrizes curriculares -> armazena 5 cursos com 5 disciplinas em cada.
usuários -> armazena 100 usuários, entre eles alunos e professores. 
Aluno contendo = curso, matriz com as disciplinas e histórico escolar
Professor contendo = departamento, disciplinas, disciplinas ministradas e se é chefe de departamento

------------------------------------------------------------------------------------------------------------------

Coleções usadas:

------------------------------------------------------------------------------------------------------------------

Usuarios:

Esta collection armazena registros de alunos e professores. Cada documento contém informações sobre o tipo de usuário (aluno ou professor), nome, curso (para alunos), departamento (para professores), disciplinas e históricos.

Estrutura dos documentos:

json
{
  "tipo": "aluno" ou "professor",
  "nome": "Nome do usuário",
  "curso": "Nome do curso" (somente para alunos),
  "departamento": "Nome do departamento" (somente para professores),
  "disciplinas": ["Lista de disciplinas"],
  "historico_escolar": [
    {
      "disciplina": "Nome da disciplina",
      "semestre": "1" ou "2",
      "ano": "Ano",
      "nota_final": "Nota final"
    }
  ] (somente para alunos),
  "disciplinas_ministradas": [
    {
      "disciplina": "Nome da disciplina",
      "semestre": "1" ou "2",
      "ano": "Ano"
    }
  ] (somente para professores),
  "chefe_departamento": true ou false (somente para professores)
}

------------------------------------------------------------------------------------------------------------------

Matrizes_curriculares:

Armazena as matrizes curriculares dos cursos oferecidos pela universidade. Cada documento contém o nome do curso e a lista de disciplinas que compõem a matriz curricular.

Estrutura dos documentos:

json
{
  "curso": "Nome do curso",
  "disciplinas": ["Lista de disciplinas"]
}

------------------------------------------------------------------------------------------------------------------

Grupos_tcc:

Armazena informações sobre os grupos de Trabalho de Conclusão de Curso (TCC). Cada documento contém um ID do grupo, a lista de alunos no grupo e o nome do professor orientador.

Estrutura dos documentos:

json
{
  "grupo_id": "Identificador do grupo",
  "alunos": ["Lista de nomes de alunos"],
  "orientador": "Nome do professor orientador"
}

------------------------------------------------------------------------------------------------------------------

como usar o programa,

1 -> colocar o login e username na main.py
2 -> Executar o main.py e escolher a opção 6 para poder popular o banco de dados.
3 -> assim que terminar de popular o banco de dados, escolher uma opção no menu.
4 -> verificar os resultados da query.