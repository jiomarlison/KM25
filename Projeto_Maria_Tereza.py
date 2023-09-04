import streamlit as st
import pandas as pd
from datetime import *

st.set_page_config(
    page_title="Horarios Maria Tereza KM-25",
    page_icon=":trolleybus:",
    layout='wide',
    initial_sidebar_state="collapsed"
)
with open("CSS/style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

# VALIDAÇÃO DE DATA, DIAS DA SEMANA
dias_horarios = ['SEGUNDA À SEXTA', 'SABADO', 'DOMINGO E FERIADOS']
sem = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")

if date.today().weekday() < 5:
    dia_hoje = dias_horarios[0]
elif date.today().weekday() == 5:
    dia_hoje = dias_horarios[1]
else:
    dia_hoje = dias_horarios[2]

# CABECALHO DA PAGINA
st.header(":scroll: TABELA DE HORÁRIOS DO PROJETO MARIA TEREZA")
st.subheader(f"Dia: :red[_{sem[date.today().weekday()]}_]", divider="rainbow")

# SELEÇÃO DOS HORARIOS DE QUAIS DIAS DA SEMANA
st.header(
    " :date: **Selecione ou remova os dias dos horarios que deseja ver**",
    help="**Selecione Segunda á Sexta para ver os horários desses dias**",
    anchor="dias_horarios"
)
dias_horarios_selecionados = st.multiselect(
    "# :pushpin: **_Selecione o(s) dia(s) que deseja ver_**",
    options=dias_horarios,
    default=dia_hoje
)
# AVISO CASO NÃO TENHA NENHUM DIA SELECIONADO
if len(dias_horarios_selecionados) == 0:
    st.error(":red[**Selecione ao menos 1 dia da semana**]", icon="🚨")
st.subheader("", divider="rainbow")

# SELECÇÃO DOS LOCAIS DE SAIDA
st.header(
    ":beginner: **Selecione ou remova o local de saida para saber os horários**",
    help="Do **KM-25** a **Petrolina** selecione **KM-25**,"
         " do **Petrolina** para **KM-25** selecione **Petrolina**",
    anchor="ponto_saida"
)
local_saida = st.multiselect(
    "# :busstop: **Ponto de Saida**",
    options=["KM-25", "Petrolina"],
    default=["KM-25", "Petrolina"],
    disabled=len(dias_horarios_selecionados) == 0
)
st.subheader("", divider="rainbow")

# MOSTRA O(S) HORÁRIO(S) DISPONIVEIS DE ACORDO COM A SELEÇÃO DAS
# INFORMAÇÕES ACIMA
st.header(":watch: Horários Disponiveis", anchor="horários")
cabecalho_horarios = pd.MultiIndex.from_product(
    [
        ["Horário Proj. Maria Tereza KM-25"],
        dias_horarios_selecionados,
        local_saida,
        ["Veiculo", "Horário", "Área"]
    ]
)
# CRIAÇÃO DA TABELA
horario_segunda_sexta = pd.DataFrame(columns=cabecalho_horarios)
# horario_segunda_sexta = pd.DataFrame(columns=cabecalho_horarios, index=[f'{x}ª' for x in range(1, 30)])

if dias_horarios_selecionados is not None:
        @st.cache_data
        def horarios_segunda_sexta(tabela_inicial, datas, locais):
            horario_seg_sex = tabela_inicial
            if 'SEGUNDA À SEXTA' in datas:
                if "KM-25" in locais:
                    horario_seg_sex["Horário Proj. Maria Tereza KM-25", 'SEGUNDA À SEXTA', 'KM-25', "Veiculo"] = \
                        [
                            "", "1º", "2º", "4º", "8º", "6º", "7º", "3º", "1º", "2º", "8º",
                            "3º", "7º", "4º", "1º", "6º", "2º", "8º", "7º", "6º", "3º",
                        ]
                    horario_seg_sex["Horário Proj. Maria Tereza KM-25", 'SEGUNDA À SEXTA', 'KM-25', "Horário"] = \
                        [
                            "", "05:50", "06:20", "06:45", "07:00", "07:10", "07:30", "08:00", "08:45", "09:30", "10:15",
                            "11:15", "12:00", "12:45", "13:30", "14:30", "15:50", "16:30", "17:00", "17:25", "18:10",
                        ]
                    horario_seg_sex["Horário Proj. Maria Tereza KM-25", 'SEGUNDA À SEXTA', 'KM-25', "Área"] = \
                        [
                            "", "VILA", "VILA", "A-20", "19/22", "R-4", "R-5/21", "VILA", "VILA", "VILA", "VILA",
                            "VILA", "R-4", "VILA", "VILA", "VILA", "VILA", "19/22", "R-5", "R-4", "VILA",
                        ]
                if "Petrolina" in locais:
                    horario_seg_sex["Horário Proj. Maria Tereza KM-25", 'SEGUNDA À SEXTA', 'Petrolina', "Veiculo"] = \
                        [
                            "TODOS", "3º", "1º", "2º", "8º", "3º", "7º", "4º", "1º", "6º", "2º",
                            "8º", "7º", "4º", "6º", "3º", "1º", "2º", "8º", "", "",
                        ]
                    horario_seg_sex["Horário Proj. Maria Tereza KM-25", 'SEGUNDA À SEXTA', 'Petrolina', "Horário"] = \
                        [
                            "05:20", "06:10", "07:10", "08:00", "09:00", "09:45", "10:30", "11:15", "12:00", "12:30",
                            "13:10", "13:50", "14:30", "15:10", "15:50", "16:30", "17:00", "18:15", "22:00", "", "",
                        ]
                    horario_seg_sex["Horário Proj. Maria Tereza KM-25", 'SEGUNDA À SEXTA', 'Petrolina', "Área"] = \
                        [
                            "TODOS", "VILA", "VILA", "VILA", "VILA", "VILA", "R-4", "VILA", "VILA", "R-4/21",
                            "VILA", "19/22", "R-5", "20", "R-4", "VILA", "VILA", "VILA", "ALUNO", "", "",
                        ]
            return horario_seg_sex


        km25_segunda_sexta = horarios_segunda_sexta(
            horario_segunda_sexta,
            dias_horarios_selecionados,
            local_saida
        )
        # TRANSFORMA A TABELA PARA HTML PARA O INDICE FICAR AJUSTADO
        st.subheader(":heavy_plus_sign: :heavy_minus_sign: Ajustar Tamanho da Tabela", anchor="tamanho_tabela")
        tamanho_colunas_horario = st.number_input(
                "",
                min_value=30,
                max_value=100,
                step=10,
                value=30
        )
        st.subheader("", divider="rainbow")
        st.markdown(
            km25_segunda_sexta.to_html(
                col_space=tamanho_colunas_horario,
                na_rep="",
                border=4,
                table_id="km25_horarios"

            ),
            unsafe_allow_html=True
        )

        st.subheader("", divider="rainbow")
with st.sidebar:
    st.markdown("[Selecionar Horário](#dias_horarios)")
    st.markdown("[Selecionar Horário](#dias_horarios)")
st.caption("Feito Por [Jiomarlison D. Souza](https://wa.me/5587981491787)")
