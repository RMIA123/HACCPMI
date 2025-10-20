HACCP Web App - Istruzioni per GitHub e Railway

1. Estrai il contenuto del file ZIP.
2. Carica la cartella su GitHub come nuovo repository.
3. Vai su https://railway.app e crea un nuovo progetto.
4. Collega il tuo repository GitHub.
5. Railway rileverà Flask e avvierà il deploy.
6. L'app sarà disponibile su un URL pubblico.

Per aggiungere utenti:
- Modifica il file data/users.csv
- Formato: username,password_crittografata
- Usa Python per generare la password criptata:
  from werkzeug.security import generate_password_hash
  print(generate_password_hash("tua_password"))
