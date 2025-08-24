# 🎨 Análise Cromática da Obra *O Grito* (Edvard Munch)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Este projeto aplica **clusterização K-Means** para identificar e quantificar as cores dominantes da famosa obra *O Grito*, de **Edvard Munch**.  
O script baixa a imagem diretamente do **Wikimedia Commons**, realiza o pré-processamento, aplica o algoritmo de agrupamento e apresenta os resultados em forma de **paleta cromática** e **gráfico de pizza** com nomes e percentuais de cada cor.

Repositório: 👉 [vitor-souza-ime/ogrito](https://github.com/vitor-souza-ime/ogrito)

---

## 📌 Funcionalidades

- 📥 Download automático da imagem com **User-Agent customizado**.  
- 🖼 Conversão e pré-processamento com **OpenCV**.  
- 🎯 Identificação das **5 cores dominantes** via **K-Means (scikit-learn)**.  
- 🏷 Associação das cores aos nomes padronizados **CSS4**.  
- 📊 Visualizações:
  - Gráfico de pizza com nomes e percentuais.  
  - Paleta linear com cores, nomes e proporções.  

---

## 🚀 Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/vitor-souza-ime/ogrito.git
cd ogrito
````

### 2. Crie o ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o script principal

```bash
python main.py
```

---

## 📦 Dependências

* [opencv-python](https://pypi.org/project/opencv-python/)
* [numpy](https://numpy.org/)
* [matplotlib](https://matplotlib.org/)
* [scikit-learn](https://scikit-learn.org/stable/)
* [requests](https://requests.readthedocs.io/en/latest/)

> Instale todas de uma vez com:

```bash
pip install opencv-python numpy matplotlib scikit-learn requests
```

---

## 📊 Exemplos de Saída

### 🔹 Gráfico de Pizza

Mostra a proporção relativa das cores dominantes extraídas da obra.

### 🔹 Paleta Extraída

Uma faixa de cores representando as cores mais importantes, acompanhadas de nomes e percentuais.

---

## 📚 Referências

* BRADSKI, G. *The OpenCV Library*. Dr. Dobb’s Journal of Software Tools, 2000.
* PEDREGOSA, F. et al. *Scikit-learn: Machine Learning in Python*. Journal of Machine Learning Research, 2011.
* CELEBI, M. E. et al. *A comparative study of efficient initialization methods for the k-means clustering algorithm*. Expert Systems with Applications, 2013.
* BEREZHNOY, I. J. et al. *Automatic color palette creation from paintings*. Computer Graphics Forum, 2005.
* INTERNATIONAL TELECOMMUNICATION UNION. *Recommendation ITU-R BT.709-6: Parameter values for the HDTV standards for production and international programme exchange*, 2015.

