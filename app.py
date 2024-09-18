import streamlit as st


st.title("tågbiljett")
st.write("Beräkna kostnaden för en tågbiljett baserat på din ålder.")

ålder = st.slider("Ange din ålder", 0, 120)

def beräkna_pris(ålder):
    if ålder < 18:
        return 130
    elif 18 <= ålder <= 64:
        return 230
    else:
        return 100

if st.button("Beräkna pris"):
    pris = beräkna_pris(ålder)
    st.write(f"Biljettpriset är: {pris} kr")

st.info("Biljettpriser:\n- Under 18 år: 130 kr\n- 18-64 år: 230 kr\n- 65 år och över: 100 kr")

