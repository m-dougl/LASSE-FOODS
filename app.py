import streamlit as st
from src.database import LasseFoodsDB


def main():
    st.set_page_config(page_icon="🍖", page_title="LASSE FOODS", layout="wide")
    st.title("LASSE FOODS")

    username = st.text_input(label="NOME: ")
    food_order = st.text_area(label="PEDIDO: ")
    send = st.button(label="Enviar")
    show_orders = st.button(label="Mostrar pedidos")
    
    database = LasseFoodsDB(db_path="lassefoods.db")
    if send:
        database.create_table()
        database.add_data(username=username, food_order=food_order)
    
    if show_orders:
        df = database.get_data()
        st.dataframe(data=df)
            

if __name__ == "__main__":
    main()
