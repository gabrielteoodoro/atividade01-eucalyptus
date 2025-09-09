# 🌲 Análise de Produção de Eucalyptus grandis

<div align="center">

![Atividade 01](https://img.shields.io/badge/Atividade-01-blue?style=for-the-badge&logo=tree)
![CEN5815](https://img.shields.io/badge/CEN5815-Análise_de_Dados_Agronômicos-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-✅_Completo-success?style=for-the-badge)

**Prof. Dr. Deoclecio Jardim Amorim • 29 de agosto de 2025**

</div>

---

## 🎯 **ACESSO DIRETO**

<div align="center">

### 📊 **RELATÓRIO COMPLETO** *(Bootstrap + Funcionalidades)*

**https://gabrielteoodoro.github.io/atividade01-eucalyptus**

✅ Navbar fixa + Sidebar moderna + Gráficos interativos + Animações

---

### 📋 **RELATÓRIO ENTREGA** *(Formato Professor)*

**https://gabrielteoodoro.github.io/atividade01-eucalyptus/relatorio_entrega.html**

✅ Formato simples para submissão acadêmica

---

### 📚 **TUTORIAL DIDÁTICO** *(Instruções Completas)*

**https://gabrielteoodoro.github.io/atividade01-eucalyptus/tutorial.html**

✅ Baseado na Atividade01.pdf + Checklist entrega

</div>

---

## 🚀 **EXECUÇÃO NO RSTUDIO**

```r
# Passo 1: Instalar dependências
source("entrega/instalar_pacotes.R")

# Passo 2: Renderizar relatório
# Abrir entrega/codigo_fonte.qmd no RStudio → Clicar "Render"
# OU: quarto::quarto_render("entrega/codigo_fonte.qmd")
```

---

## 📤 **ENTREGA AO PROFESSOR**

### 🚨 **MÁXIMO 2 ARQUIVOS** *(Conforme Atividade01.pdf)*

| **Arquivo** | **Descrição** |
|:-----------:|:-------------|
| **1️⃣ codigo_fonte.html** | Relatório renderizado no RStudio |
| **2️⃣ projeto.zip** | Pasta `entrega/` compactada |

---

## 📊 **DADOS EXPERIMENTAIS**

| **Procedência** | **P1** | **P2** | **P3** | **P4** | **P5** | **P6** | **P7** | **Total** |
|:---------------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:---------:|
| **Bloco I**     | 358    | 284    | 273    | 284    | 258    | 249    | 318    | **2.024** |
| **Bloco II**    | 380    | 249    | 222    | 242    | 263    | 217    | 312    | **1.885** |
| **Bloco III**   | 353    | 259    | 236    | 266    | 242    | 267    | 327    | **1.950** |
| **Bloco IV**    | 360    | 242    | 226    | 252    | 231    | 220    | 319    | **1.850** |
| **Total**       | **1.451** | **1.034** | **957** | **1.044** | **994** | **953** | **1.276** | **7.709** |

---

## 📈 **PRINCIPAIS RESULTADOS**

| **Métrica** | **Valor** | **Interpretação** |
|:-----------:|:---------:|:-----------------:|
| **F (Procedências)** | `40,05***` | Altamente significativo |
| **F (Blocos)** | `3,75*` | Significativo |
| **CV Experimental** | `5,43%` | Excelente precisão |
| **Melhor Procedência** | **P1** | 362,75 m³.ha⁻¹ |

### 🏆 **Ranking das Procedências**

| Pos | Procedência | Produção | Grupo |
|:---:|:-----------:|:--------:|:-----:|
| **1º** | **P1** | **362,75** | **A** |
| **2º** | P7 | 319,00 | **B** |
| 3º-7º | P4,P2,P5,P3,P6 | 238-261 | **C** |

---

## ✅ **CHECKLIST DE ENTREGA**

**Antes de submeter:**
- [ ] ✅ Executei `source("entrega/instalar_pacotes.R")`
- [ ] ✅ Renderizei `codigo_fonte.qmd` no RStudio
- [ ] ✅ Arquivo `codigo_fonte.html` gerado
- [ ] ✅ Compactei pasta `entrega/` em .zip
- [ ] ✅ Tenho APENAS 2 arquivos para upload

**Conteúdo validado:**
- [ ] ✅ Análise descritiva completa
- [ ] ✅ ANOVA DIC realizada
- [ ] ✅ ANOVA DBC realizada  
- [ ] ✅ Teste Tukey executado
- [ ] ✅ Comparação DIC vs DBC
- [ ] ✅ Formatação Quarto adequada

---

## 💡 **CONCLUSÕES**

1. **Diferenças altamente significativas** entre procedências (F = 40,05; p < 0,001)
2. **P1 é estatisticamente superior** com 362,75 m³.ha⁻¹
3. **DBC mais eficiente que DIC** (CV: 5,43% vs 7,11%)
4. **Excelente precisão experimental** (CV = 5,43%)

### 📋 **Recomendações**
- **🌱 Comercial:** Utilizar procedência P1 para plantios
- **🔬 Experimental:** Adotar DBC em futuros experimentos
- **📈 Melhoramento:** Investir no desenvolvimento da P1

---

<div align="center">

## 🌐 **LINKS RÁPIDOS**

**📊 Relatório:** https://gabrielteoodoro.github.io/atividade01-eucalyptus  
**📋 Entrega:** https://gabrielteoodoro.github.io/atividade01-eucalyptus/relatorio_entrega.html  
**📚 Tutorial:** https://gabrielteoodoro.github.io/atividade01-eucalyptus/tutorial.html  

**⭐ Projeto desenvolvido seguindo rigorosamente os requisitos da Atividade01.pdf**

*Análise estatística profissional para pesquisa florestal* 🌲

</div>