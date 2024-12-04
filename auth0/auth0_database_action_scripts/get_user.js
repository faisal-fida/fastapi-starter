function getByEmail(email, callback) {
  const connectionString = configuration.DATABASE_URI;
  const { Client } = require("pg");
  const client = new Client({
    connectionString: connectionString,
    ssl: {
      rejectUnauthorized: true,
    },
  });
  client.connect((err) => {
    if (err) {
      return callback(err);
    }

    const query = `SELECT email FROM "Users" WHERE email = $1`;
    client.query(query, [email], (err, result) => {
      client.end();
      if (err) {
        return callback(new Error(err.message));
      } else if (result.rows.length === 0) {
        return callback(null);
      }
      const user = result.rows[0];
      return callback(null, user);
    });
  });
}
