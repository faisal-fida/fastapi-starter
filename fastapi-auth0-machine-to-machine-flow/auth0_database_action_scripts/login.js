function login(email, password, callback) {
  console.log("In Login");
  const bcrypt = require("bcrypt");
  const { Client } = require("pg");
  const connectionString = configuration.DATABASE_URI;

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

    const query = `SELECT "userId", "email", "password" FROM "Users" WHERE "email" = $1`;
    client.query(query, [email], function (err, result) {
      if (err || result.rows.length === 0)
        return callback(err || new WrongUsernameOrPasswordError(email));

      const user = result.rows[0];
      bcrypt.compare(password, user.password, function (err, isValid) {
        if (err || !isValid)
          return callback(err || new WrongUsernameOrPasswordError(email));

        return callback(null, {
          user_id: user.userId,
          email: user.email,
        });
      });
    });
  });
}
