import streamlit as st



paginas = ['Home', 'Histograma', 'Sobre']

st.sidebar.subheader('Navegue por aqui')
pagina = st.sidebar.selectbox('Menu', paginas)

if pagina == 'Home':
	st.title('Meu primeiro Web-App da Vida')
	st.markdown('---')
	st.write('Meu webapp com diversas funcionalidades bacanas. Só navegue!')

if pagina == 'Histograma':

	import matplotlib.pyplot as plt
	import numpy as np

	n = st.slider('Número:', 50, 500, 100, 10)
	cor = st.color_picker('Escolha uma cor')
	cor2 = st.color_picker('Escolha outra cor')

	x = np.random.normal(0, 1, size = n)

	fig, ax = plt.subplots()
	ax.hist(x, color = cor, edgecolor = cor2)

	st.pyplot(fig)

if pagina == 'Sobre':
	st.write('WebApp versão 0.0.-1. Em desenvolvimento.')
 
