const { Sequelize } = require('sequelize');
const fs = require("fs");

async function testScript() {
    const config = {
        username: "REDACTED",
        password: "REDACTED",
        host: "REDACTED",
        database: "postgres",
        dialect: "postgres",
        dialectOptions: {
            ssl: {
                ca: fs.readFileSync(__dirname + '/ssl/BaltimoreCyberTrustRoot.crt.pem')
            }
        }
    }

    const sequelize = new Sequelize(config);

    try {
        await sequelize.authenticate()
        console.log('Connection has been established successfully.');
    } catch (error) {
        console.error('Unable to connect to the database: ', error);
    }
}

testScript();