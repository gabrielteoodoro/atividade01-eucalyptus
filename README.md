# 🌲 Análise de Produção de Eucalyptus grandis

<div align="center">

![Atividade 01](https://img.shields.io/badge/Atividade-01-blue?style=for-the-badge&logo=tree)
![CEN5815](https://img.shields.io/badge/CEN5815-Análise_de_Dados_Agronômicos-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-✅_Completo-success?style=for-the-badge)

**Prof. Dr. Deoclecio Jardim Amorim**  
*29 de agosto de 2025*

[![Tutorial Completo](https://img.shields.io/badge/📚_Ver-Tutorial_Completo-blue?style=for-the-badge)](https://gabrielteoodoro.github.io/atividade01-eucalyptus)

</div>

---

## 🎯 **REQUISITOS DA ATIVIDADE** *(Conforme Atividade01.pdf)*

<table align="center">
<tr>
<td width="50%">

### 📊 **1. Análise Descritiva**
- Média e desvio padrão por tratamento
- Entender distribuição e variabilidade dos dados

### 📈 **2. ANOVA**
- **DIC:** Delineamento Inteiramente Casualizado
- **DBC:** Delineamento em Blocos Casualizados
- Comparar eficácia dos tratamentos

</td>
<td width="50%">

### 📝 **3. Relatório Quarto**
- Relatório detalhado usando Quarto
- Incluir análise descritiva e ANOVA
- Seguir modelo fornecido pelo professor

### 📤 **4. Entrega (MÁXIMO 2 ARQUIVOS)**
1. **Arquivo HTML renderizado**
2. **Projeto compactado** (.zip/.rar/.tgz)

</td>
</tr>
</table>

---

## 🚀 **EXECUÇÃO RÁPIDA**

### **Passo 1: Instalar Dependências**
```r
source("entrega/instalar_pacotes.R")
```

### **Passo 2: Gerar Relatório**

<table>
<tr>
<td width="50%">

#### 🖥️ **Método 1: RStudio** *(Recomendado)*
```r
# 1. Abrir arquivo no RStudio:
#    entrega/codigo_fonte.qmd
# 
# 2. Clicar no botão "Render"
# 
# 3. HTML será gerado automaticamente
```

</td>
<td width="50%">

#### 💻 **Método 2: R Console**
```r
quarto::quarto_render("entrega/codigo_fonte.qmd")
```

#### 🐍 **Método 3: Python (Alternativo)**
```bash
python analise_python_puro.py
```

</td>
</tr>
</table>

---

## 📤 **O QUE ENTREGAR AO PROFESSOR**

<div align="center">

### 🚨 **ATENÇÃO: Máximo 2 arquivos conforme Atividade01.pdf**

</div>

<table align="center">
<tr>
<td width="50%" align="center">

### 📄 **Arquivo 1: HTML Renderizado**

```
codigo_fonte.html
```

**Este é o relatório principal** que será avaliado pelo professor com todas as análises estatísticas.

✅ Análise Descritiva  
✅ ANOVA DIC  
✅ ANOVA DBC  
✅ Formatação Quarto  

</td>
<td width="50%" align="center">

### 📦 **Arquivo 2: Projeto Compactado**

```
atividade01_entrega.zip
```

**Contém o código fonte** e arquivos de apoio para reprodutibilidade.

📁 `codigo_fonte.qmd`  
📁 `instalar_pacotes.R`  
📁 `executar_analise.R`  
📁 `INSTRUCOES.txt`  

</td>
</tr>
</table>

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

<div align="center">

**Variável:** Produção em m³.ha⁻¹  
**Tratamentos:** 7 procedências de *Eucalyptus grandis*  
**Delineamento:** Blocos casualizados (4 repetições)

</div>

---

## 📈 **PRINCIPAIS RESULTADOS**

<div align="center">

| **Métrica Estatística** | **Valor** | **Interpretação** |
|:-----------------------:|:---------:|:-----------------:|
| **F (Procedências)** | `40,05***` | Altamente significativo (p < 0,001) |
| **F (Blocos)** | `3,75*` | Significativo (p < 0,05) |
| **CV Experimental** | `5,43%` | Excelente precisão |
| **Melhor Procedência** | **P1** | 362,75 m³.ha⁻¹ |

</div>

### 🏆 **Ranking das Procedências (Teste de Tukey)**

<table align="center">
<tr>
<th>Posição</th>
<th>Procedência</th>
<th>Produção (m³.ha⁻¹)</th>
<th>Grupo Estatístico</th>
</tr>
<tr align="center">
<td><strong>1º</strong></td>
<td><strong>P1</strong></td>
<td><strong>362,75</strong></td>
<td><img src="https://img.shields.io/badge/Grupo-A-success"></td>
</tr>
<tr align="center">
<td><strong>2º</strong></td>
<td>P7</td>
<td>319,00</td>
<td><img src="https://img.shields.io/badge/Grupo-B-primary"></td>
</tr>
<tr align="center">
<td>3º-7º</td>
<td>P4, P2, P5, P3, P6</td>
<td>238-261</td>
<td><img src="https://img.shields.io/badge/Grupo-C-warning"></td>
</tr>
</table>

---

## 🛠️ **ESTRUTURA DO PROJETO**

```
📦 atividade01-eucalyptus/
├── 📚 README.md                          ← Este arquivo
├── 🎯 index.html                         ← Tutorial interativo
├── 📂 entrega/                           ← PASTA PRINCIPAL
│   ├── 📄 codigo_fonte.qmd              ← Código fonte Quarto ⭐
│   ├── 📄 codigo_fonte.html             ← Relatório HTML (ENTREGA) ⭐
│   ├── 🔧 instalar_pacotes.R            ← Instalação automática
│   ├── 📊 executar_analise.R            ← Script R alternativo
│   └── 📋 INSTRUCOES.txt                ← Instruções de execução
├── 📂 src/                               ← Scripts adicionais
├── 📂 docs/                              ← Documentação
└── 📁 data/                              ← Dados originais
```

---

## ✅ **CHECKLIST DE ENTREGA**

### **Antes de Submeter:**

- [ ] Executei `source("entrega/instalar_pacotes.R")`
- [ ] Renderizei o arquivo `.qmd` no RStudio sem erros
- [ ] Arquivo `codigo_fonte.html` foi gerado corretamente
- [ ] Compactei a pasta `entrega/` em arquivo `.zip`
- [ ] Tenho APENAS 2 arquivos para upload:
  - [ ] `codigo_fonte.html` (Relatório principal)
  - [ ] `atividade01_entrega.zip` (Projeto compactado)

### **Validação de Conteúdo:**

- [ ] **Análise Descritiva:** Médias, desvios, tabelas ✅
- [ ] **ANOVA DIC:** Análise como delineamento inteiramente casualizado ✅
- [ ] **ANOVA DBC:** Análise como delineamento em blocos ✅
- [ ] **Comparação:** DIC vs DBC eficiência ✅
- [ ] **Teste Tukey:** Comparações múltiplas ✅
- [ ] **Relatório Quarto:** Formatação adequada ✅

---

## 🔗 **LINKS ÚTEIS**

<div align="center">

[![Tutorial Interativo](https://img.shields.io/badge/📚_Acessar-Tutorial_Interativo-blue?style=for-the-badge&logo=github)](https://gabrielteoodoro.github.io/atividade01-eucalyptus)
[![Código Fonte](https://img.shields.io/badge/💾_Ver-Código_no_GitHub-green?style=for-the-badge&logo=github)](https://github.com/gabrielteoodoro/atividade01-eucalyptus)
[![Download Projeto](https://img.shields.io/badge/📥_Download-Projeto_Completo-orange?style=for-the-badge&logo=download)](https://github.com/gabrielteoodoro/atividade01-eucalyptus/archive/main.zip)

</div>

### **Documentação Técnica:**
- 📖 [Documentação Quarto](https://quarto.org/)
- 🔬 [Pacote agricolae](https://cran.r-project.org/package=agricolae)
- 📊 [Tidyverse](https://www.tidyverse.org/)

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

## 💡 **CONCLUSÕES PRINCIPAIS**

### **🏆 Resultados Estatísticos**
1. **Diferenças altamente significativas** entre procedências (F = 40,05; p < 0,001)
2. **P1 é estatisticamente superior** com 362,75 m³.ha⁻¹
3. **DBC mais eficiente que DIC** (CV: 5,43% vs 7,11%)
4. **Excelente precisão experimental** (CV = 5,43%)

### **📋 Recomendações Técnicas**
- **🌱 Comercial:** Utilizar procedência P1 para plantios
- **🔬 Experimental:** Adotar DBC em futuros experimentos
- **📈 Melhoramento:** Investir no desenvolvimento da P1
- **🗺️ Zoneamento:** Avaliar adaptação regional da P1

---

## 🆘 **SUPORTE**

### **Problemas com Execução?**

1. **Pacotes não instalam:** Execute `install.packages("agricolae", dependencies=TRUE)`
2. **Quarto não funciona:** Use o script R: `source("entrega/executar_analise.R")`
3. **Erro de rendering:** Verifique se RStudio tem Quarto atualizado

### **Contato**
- 📧 **Issues GitHub:** [Reportar Problema](https://github.com/gabrielteoodoro/atividade01-eucalyptus/issues)
- 📚 **Tutorial:** [Passo-a-passo Completo](https://gabrielteoodoro.github.io/atividade01-eucalyptus)

---

<div align="center">

### **🎯 Resumo para Entrega**

**Execute:** `source("entrega/instalar_pacotes.R")` → Renderize `codigo_fonte.qmd`  
**Entregue:** `codigo_fonte.html` + `projeto.zip` *(máximo 2 arquivos)*

---

**⭐ Projeto desenvolvido seguindo rigorosamente os requisitos da Atividade01.pdf**

![GitHub Repo stars](https://img.shields.io/github/stars/gabrielteoodoro/atividade01-eucalyptus?style=social)
![GitHub forks](https://img.shields.io/github/forks/gabrielteoodoro/atividade01-eucalyptus?style=social)

*Análise estatística profissional para pesquisa florestal* 🌲

</div>