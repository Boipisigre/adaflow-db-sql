#!/home/pboizot/src/DB-sql/bin/python

# import du driver de connection sqlite3
import sqlite3

# Etablissement de la connection
DBCon = sqlite3.connect('chinook.db')

print("Connection established ..........")

# lister les tables

# Ouvrir un curseur
verif = DBCon.cursor()
version = verif.execute("select sqlite_version()").fetchone()
print(version)

DBCon.close()
