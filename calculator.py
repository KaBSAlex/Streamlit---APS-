#python -m streamlit run calculator.py
import streamlit as st

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

def calculator():
    st.title("Calculator")
    st.markdown("---")

    operacao = st.selectbox("Operação", ("Soma", "Subtração", "Multiplicação", "Divisão"))

    num1 = st.number_input("Number_1:", step=1)
    num2 = st.number_input("Number_2")

    resultado = 0

    if operacao == "Soma":
        resultado = soma(num1, num2)
    if operacao == "Subtração":
        resultado = subtracao(num1, num2)
    if operacao == "Multiplicação":
        resultado = multiplicacao(num1, num2)
    if operacao == "Divisão":
        resultado = divisao(num1, num2)

    st.write("Result:", resultado)

if __name__ == "__main__":
    calculator()