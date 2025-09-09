# 🌲 Análise de Produção de Eucalyptus grandis

<div align="center">

![Atividade 01](https://img.shields.io/badge/Atividade-01-blue?style=for-the-badge&logo=tree)
![CEN5815](https://img.shields.io/badge/CEN5815-Análise_de_Dados_Agronômicos-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-✅_Completo-success?style=for-the-badge)

**Prof. Dr. Deoclecio Jardim Amorim**  
*29 de agosto de 2025*

</div>

---

## 🎯 **ACESSO DIRETO**

<div align="center">

### 📊 **Relatório Completo (Publicado)**
[![Visualizar Relatório](https://img.shields.io/badge/🌐_Acessar-Relatório_Completo-blue?style=for-the-badge)](https://gabrielteoodoro.github.io/atividade01-eucalyptus)

**✅ Versão profissional com Bootstrap Quarto**
- Sidebar navegável com índice
- Todas as análises estatísticas
- Dados experimentais completos
- Tabelas e gráficos formatados
- **Para visualização e apresentações**

---

### 📚 **Tutorial Didático**
[![Acessar Tutorial](https://img.shields.io/badge/📖_Acessar-Tutorial_Didático-orange?style=for-the-badge)](https://gabrielteoodoro.github.io/atividade01-eucalyptus/tutorial.html)

**✅ Baseado na Atividade01.pdf**
- Requisitos da atividade
- Passo-a-passo de execução
- O que entregar ao professor
- Checklist completo
- **Para instruções e entrega**

</div>

---

## 📋 **REQUISITOS DA ATIVIDADE** *(Conforme Atividade01.pdf)*

| **Item** | **Descrição** | **Status** |
|:--------:|:-------------|:----------:|
| **1. Análise Descritiva** | Média e desvio padrão por tratamento | ✅ |
| **2. ANOVA DIC** | Delineamento Inteiramente Casualizado | ✅ |
| **3. ANOVA DBC** | Delineamento em Blocos Casualizados | ✅ |
| **4. Relatório Quarto** | Usando Quarto conforme modelo | ✅ |
| **5. Entrega** | Máximo 2 arquivos (.html + .zip) | ✅ |

---

## 🚀 **EXECUÇÃO NO RSTUDIO**

### **Passo 1: Instalar Dependências**
```r
source("entrega/instalar_pacotes.R")
```

### **Passo 2: Gerar Relatório**
```r
# Método 1: RStudio (Recomendado)
# 1. Abrir entrega/codigo_fonte.qmd
# 2. Clicar em "Render"

# Método 2: R Console
quarto::quarto_render("entrega/codigo_fonte.qmd")
```

---

## 📤 **ENTREGA AO PROFESSOR**

<div align="center">

### 🚨 **ATENÇÃO: Máximo 2 arquivos**

| **Arquivo** | **Descrição** | **Como Obter** |
|:-----------:|:-------------|:--------------|
| **1️⃣ codigo_fonte.html** | Relatório principal | Renderizar .qmd no RStudio |
| **2️⃣ projeto.zip** | Código fonte | Compactar pasta entrega/ |

</div>

---

## 📊 **DADOS EXPERIMENTAIS**

### **Experimento: 4 Blocos × 7 Procedências**

| **Procedência** | **P1** | **P2** | **P3** | **P4** | **P5** | **P6** | **P7** | **Total** |
|:---------------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:---------:|
| **Bloco I**     | 358    | 284    | 273    | 284    | 258    | 249    | 318    | **2.024** |
| **Bloco II**    | 380    | 249    | 222    | 242    | 263    | 217    | 312    | **1.885** |
| **Bloco III**   | 353    | 259    | 236    | 266    | 242    | 267    | 327    | **1.950** |
| **Bloco IV**    | 360    | 242    | 226    | 252    | 231    | 220    | 319    | **1.850** |
| **Total**       | **1.451** | **1.034** | **957** | **1.044** | **994** | **953** | **1.276** | **7.709** |

---

## 📈 **PRINCIPAIS RESULTADOS**

<div align="center">

| **Métrica** | **Valor** | **Interpretação** |
|:-----------:|:---------:|:-----------------:|
| **F (Procedências)** | `40,05***` | Altamente significativo |
| **F (Blocos)** | `3,75*` | Significativo |
| **CV Experimental** | `5,43%` | Excelente precisão |
| **Melhor Procedência** | **P1** | 362,75 m³.ha⁻¹ |

### 🏆 **Ranking das Procedências**

| Posição | Procedência | Produção | Grupo Tukey |
|:-------:|:-----------:|:--------:|:-----------:|
| **1º** | **P1** | **362,75** | ![A](https://img.shields.io/badge/A-success) |
| **2º** | P7 | 319,00 | ![B](https://img.shields.io/badge/B-primary) |
| 3º-7º | P4,P2,P5,P3,P6 | 238-261 | ![C](https://img.shields.io/badge/C-warning) |

</div>

---

## 🛠️ **ESTRUTURA DO PROJETO**

```
📦 atividade01-eucalyptus/
├── 📊 index.html                         ← Relatório completo (Bootstrap)
├── 📚 tutorial.html                      ← Tutorial didático
├── 📖 README.md                          ← Este arquivo
├── 📂 entrega/                           ← PASTA PARA ENTREGA
│   ├── 📄 codigo_fonte.qmd              ← Código fonte Quarto ⭐
│   ├── 📄 codigo_fonte.html             ← Para entregar ⭐
│   ├── 🔧 instalar_pacotes.R            ← Instalação automática
│   ├── 📊 executar_analise.R            ← Script alternativo
│   └── 📋 INSTRUCOES.txt                ← Instruções
├── 📂 src/                               ← Scripts adicionais
└── 📂 docs/                              ← Documentação
```

---

## ✅ **CHECKLIST DE ENTREGA**

### **Para o Estudante:**

**Antes de submeter:**
- [ ] Executei `source("entrega/instalar_pacotes.R")`
- [ ] Renderizei `codigo_fonte.qmd` sem erros
- [ ] Arquivo `codigo_fonte.html` gerado
- [ ] Compactei pasta `entrega/` em .zip
- [ ] Tenho APENAS 2 arquivos para upload

**Validação de conteúdo:**
- [ ] Análise descritiva completa ✅
- [ ] ANOVA DIC realizada ✅
- [ ] ANOVA DBC realizada ✅
- [ ] Comparação DIC vs DBC ✅
- [ ] Teste Tukey executado ✅
- [ ] Relatório Quarto formatado ✅

---

## 🎓 **INFORMAÇÕES ACADÊMICAS**

<div align="center">

| **Atributo** | **Detalhamento** |
|:------------:|:----------------:|
| **Disciplina** | CEN5815 - Análise de Dados Agronômicos e Ambientais |
| **Professor** | Prof. Dr. Deoclecio Jardim Amorim |
| **Atividade** | 01 - Análise ANOVA de *Eucalyptus grandis* |
| **Data** | 29 de agosto de 2025 |
| **Entrega** | Máximo 2 arquivos (.html + .zip) |

</div>

---

## 💡 **CONCLUSÕES**

### **🏆 Resultados Estatísticos**
1. **Diferenças altamente significativas** entre procedências (F = 40,05; p < 0,001)
2. **P1 é estatisticamente superior** com 362,75 m³.ha⁻¹
3. **DBC mais eficiente que DIC** (CV: 5,43% vs 7,11%)
4. **Excelente precisão experimental** (CV = 5,43%)

### **📋 Recomendações**
- **🌱 Comercial:** Utilizar procedência P1
- **🔬 Experimental:** Adotar DBC
- **📈 Melhoramento:** Investir na P1

---

## 🆘 **SUPORTE**

**Problemas?**
- 📧 [Issues GitHub](https://github.com/gabrielteoodoro/atividade01-eucalyptus/issues)
- 📚 [Tutorial Completo](https://gabrielteoodoro.github.io/atividade01-eucalyptus/tutorial.html)

---

<div align="center">

### **🎯 RESUMO RÁPIDO**

**Execute:** `source("entrega/instalar_pacotes.R")` → Renderize `codigo_fonte.qmd`  
**Entregue:** `codigo_fonte.html` + `projeto.zip` *(máximo 2 arquivos)*

[![Relatório](https://img.shields.io/badge/📊_Ver-Relatório_Completo-blue?style=for-the-badge)](https://gabrielteoodoro.github.io/atividade01-eucalyptus)
[![Tutorial](https://img.shields.io/badge/📚_Ver-Tutorial_Didático-orange?style=for-the-badge)](https://gabrielteoodoro.github.io/atividade01-eucalyptus/tutorial.html)

---

**⭐ Projeto desenvolvido seguindo rigorosamente os requisitos da Atividade01.pdf**

![Stars](https://img.shields.io/github/stars/gabrielteoodoro/atividade01-eucalyptus?style=social)
![Forks](https://img.shields.io/github/forks/gabrielteoodoro/atividade01-eucalyptus?style=social)

*Análise estatística profissional para pesquisa florestal* 🌲

</div>