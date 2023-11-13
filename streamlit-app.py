import snowflake.connector
import streamlit

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
streamlit.text("Hello from Snowflake:")



def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values('" +new_fruit+ "')")
    return "Thanks for adding" + new_fruit 

add_my_fruit=streamlit.text_input('What fruits would u like to add?')
if streamlit.button("Add fruit"):
  back_from_connection=insert_row_snowflake(add_my_fruit)
  streamlit.txt(back_from_connection)
