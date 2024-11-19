import { Client } from 'cassandra-driver';

// Conectar ao cluster Cassandra
const client = new Client({
  contactPoints: ['127.0.0.1'],
  localDataCenter: 'datacenter1'
});

client.connect()

client.execute(`CREATE KEYSPACE IF NOT EXISTS cc6240 WITH REPLICATION = { 'class': 'NetworkTopologyStrategy', 'replication_factor' :1};`)
client.execute('USE cc6240')
//client.execute(``)

client.execute(`CREATE TABLE IF NOT EXISTS cc6240.historico_escolar(
    nome text,
    disciplina text,
    codigo_disciplina int,
    semestre int,
    ano int,
    nota double,
    primary key((name), disciplina))
);
`)

client.execute('CREATE INDEX ON cc6240.historico_escolar(codigo_disciplina);')

client.execute(`CREATE TABLE IF NOT EXISTS  cc6240.historico_disciplinas (
    name text,
    dept_name text,
    tot_cred tinyint,
    advisor text,
    primary key((name), dept_name)
);
`)


//client.execute(`CREATE INDEX ON cc6240.instructor(dept_name);`)

const queries = [ "INSERT INTO instructor (name, dept_name, salary) VALUES('McKinnon', 'Cybernetics', 94333.99)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Pingr', 'Statistics', 59303.62)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Mird', 'Marketing', 119921.41)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Luo', 'English', 88791.45)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Murata', 'Athletics', 61387.56)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Konstantinides', 'Languages', 32570.50)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Levine', 'Elec. Eng.', 89805.83)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Shuming', 'Physics', 108011.81)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Queiroz', 'Biology', 45538.32)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Sullivan', 'Elec. Eng.', 90038.09)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Bertolino', 'Mech. Eng.', 51647.57)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Hau', 'Accounting', 43966.29)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Voronina', 'Physics', 121141.99)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Soisalon-Soininen', 'Psychology', 62579.61)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Moreira', 'Accounting', 71351.42)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Arias', 'Statistics', 104563.38)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Mingoz', 'Finance', 105311.38)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Yazdi', 'Athletics', 98333.65)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Lembr', 'Accounting', 32241.56)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Choll', 'Statistics', 57807.09)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Valtchev', 'Biology', 77036.18)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Arinb', 'Statistics', 54805.11)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Bawa', 'Athletics', 72140.88)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Kenje', 'Marketing', 106554.73)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Vicentino', 'Elec. Eng.', 34272.67)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Dusserre', 'Marketing', 66143.25)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Jaekel', 'Athletics', 103146.87)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Desyl', 'Languages', 48803.38)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('DAgostino', 'Psychology', 59706.49)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Sarkar', 'Pol. Sci.', 87549.80)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Ullman', 'Accounting', 47307.10)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Bancilhon', 'Pol. Sci.', 87958.01)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Liley', 'Languages', 90891.69)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Morris', 'Marketing', 43770.36)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Yin', 'English', 46397.59)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Gustafsson', 'Elec. Eng.', 82534.37)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Bondi', 'Comp. Sci.', 115469.11)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Lent', 'Mech. Eng.', 107978.47)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Pimenta', 'Cybernetics', 79866.95)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Bourrier', 'Comp. Sci.', 80797.83)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Gutierrez', 'Statistics', 45310.53)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Sakurai', 'English', 118143.98)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Romero', 'Astronomy', 79070.08)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Mahmoud', 'Geology', 99382.59)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Kean', 'English', 35023.18)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Bietzk', 'Cybernetics', 117836.50)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Atanassov', 'Statistics', 84982.92)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Tung', 'Athletics', 50482.03)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Wieland', 'Pol. Sci.', 124651.41)", 
  "INSERT INTO instructor (name, dept_name, salary) VALUES('Dale', 'Cybernetics', 93348.83)",
  "INSERT INTO student (name, dept_name, tot_cred, advisor) VALUES('Schrefl', 'History', 4, 'Moreira')", 
  "INSERT INTO student (name, dept_name, tot_cred, advisor) VALUES('Rumat', 'Finance', 100, 'Arias')", 
  "INSERT INTO student (name, dept_name, tot_cred, advisor) VALUES('Miliko', 'Statistics', 116, 'Mingoz')", 
  "INSERT INTO student (name, dept_name, tot_cred, advisor) VALUES('Moszkowski', 'Civil Eng.', 73, 'Yazdi')", 
  "INSERT INTO student (name, dept_name, tot_cred, advisor) VALUES('Prieto', 'Biology', 91, 'Lembr')", 
  "INSERT INTO student (name, dept_name, tot_cred, advisor) VALUES('Marcol', 'Cybernetics', 15, 'Choll')", 
  "INSERT INTO student (name, dept_name, tot_cred, advisor) VALUES('Quimby', 'History', 4, 'Valtchev')", 
  "INSERT INTO student (name, dept_name, tot_cred, advisor) VALUES('Sowerby', 'English', 108, 'Arinb')", 
  "INSERT INTO student (name, dept_name, tot_cred, advisor) VALUES('Coppens', 'Math', 58, 'Bawa')", 
  "INSERT INTO student (name, dept_name, tot_cred, advisor) VALUES('Cirsto', 'Math', 115, 'Kenje')"];

for (const query of queries) {
  await client.execute(query);
  console.log(query) 
}

await client.shutdown();
console.log("Sucesso ao criar o keyspace")

