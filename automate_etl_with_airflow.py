import psycopg2

# Establish a connection to the database
conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="oushesh",
    password="12345"
)

# Create a cursor object
cursor = conn.cursor()

# Execute the SQL command to fetch all rows from the "suppliers" table
sql = "SELECT * FROM suppliers;"
cursor.execute(sql)

# Fetch all the rows and column names
rows = cursor.fetchall()
column_names = [desc[0] for desc in cursor.description]

# Print the column names
print(column_names)

# Print the data rows
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()

## Prisma or Supabase are better options.
