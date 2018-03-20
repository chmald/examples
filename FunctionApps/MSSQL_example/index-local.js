const sql = require('mssql');
const config = {
    user: 'cmaldonado',
    password: 'password',
    server: 'mssql-server-name.database.windows.net',
    database: 'database-name',
    pool: {
        max: 100,
        min: 0,
        idleTimeoutMillis: 30000
    },
    options: {
        encrypt: true,
    }
}

const pool = new sql.ConnectionPool(config);

console.log('JavaScript HTTP trigger function processed a request.');

pool.connect().then(err => {
    return pool.request().query('select * from dbo.yourTable');
}).then(result => {
    console.log(result);
    pool.close();
});

pool.on('error', err => {
    console.log(err);
});