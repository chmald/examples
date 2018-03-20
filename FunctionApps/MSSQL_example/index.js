const sql = require('mssql');
const config = {
    user: 'username',
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

module.exports = function (context, req) {
    context.log('JavaScript HTTP trigger function processed a request.');

    pool.connect().then(err => {
        return pool.request().query('select * from dbo.yourTable');
    }).then(result => {
        context.log(result);
        context.res = {
            status: 200,
            body: result.recordset
        }

        context.done();
        pool.close();
    });

    pool.on('error', err => {
        context.log(err);
        context.res = {
                status: 200,
                body: "No data"
            }

            context.done();
    })
};