# 🌲 Análise de Produção de Eucalyptus grandis

<div align="center">

![Atividade 01](https://img.shields.io/badge/Atividade-01-blue?style=for-the-badge&logo=tree)
![CEN5815](https://img.shields.io/badge/CEN5815-Análise_de_Dados_Agronômicos-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-✅_Completo-success?style=for-the-badge)

**Prof. Dr. Deoclecio Jardim Amorim**  
*29 de agosto de 2025*

</div>

---

## 🎯 **ACESSO DIRETO - DUAS VERSÕES**

<table align="center">
<tr>
<td width="50%" align="center">

### 📊 **RELATÓRIO PUBLICADO**
**(Completo e Funcional)**

[![Ver Relatório](https://img.shields.io/badge/🌐_Acessar-Relatório_Completo-blue?style=for-the-badge)](https://gabrielteoodoro.github.io/atividade01-eucalyptus)

✅ **Bootstrap Quarto oficial**  
✅ **Sidebar TOC navegável**  
✅ **Todas as análises estatísticas**  
✅ **Gráficos e tabelas formatados**  
✅ **50KB com dados completos**  

**Para:** Visualização e apresentações

</td>
<td width="50%" align="center">

### 📋 **RELATÓRIO DE ENTREGA**
**(Formato do Professor)**

[![Ver Entrega](https://img.shields.io/badge/📄_Acessar-Formato_Professor-orange?style=for-the-badge)](https://gabrielteoodoro.github.io/atividade01-eucalyptus/relatorio_entrega.html)

✅ **Formato simples e limpo**  
✅ **Igual ao modelo do professor**  
✅ **Sem formatações extras**  
✅ **Pronto para submissão**  

**Para:** Entrega acadêmica

</td>
</tr>
</table>

<div align="center">

### 📚 **TUTORIAL DIDÁTICO**
[![Acessar Tutorial](https://img.shields.io/badge/📖_Acessar-Tutorial_Completo-success?style=for-the-badge)](https://gabrielteoodoro.github.io/atividade01-eucalyptus/tutorial.html)

**✅ Baseado na Atividade01.pdf** • **✅ Passo-a-passo execução** • **✅ Checklist entrega**

</div>

---

## 📋 **REQUISITOS ATENDIDOS** *(Conforme Atividade01.pdf)*

| **Requisito** | **Descrição** | **Localização** | **Status** |
|:-------------:|:-------------|:----------------|:----------:|
| **1. Análise Descritiva** | Média e desvio padrão por tratamento | Seção 3 dos relatórios | ✅ |
| **2. ANOVA DIC** | Delineamento Inteiramente Casualizado | Seção 4 dos relatórios | ✅ |
| **3. ANOVA DBC** | Delineamento em Blocos Casualizados | Seção 5 dos relatórios | ✅ |
| **4. Relatório Quarto** | Usando Quarto conforme modelo | `codigo_fonte.qmd` | ✅ |
| **5. Entrega** | **Máximo 2 arquivos** (.html + .zip) | Pasta `entrega/` | ✅ |

---

## 🚀 **COMO EXECUTAR NO RSTUDIO**

### **📦 Passo 1: Instalar Dependências**
```r
source("entrega/instalar_pacotes.R")
```

### **🎯 Passo 2: Gerar Relatório**

<table>
<tr>
<td width="50%">

#### 🖥️ **Método 1: RStudio** *(Recomendado)*
```r
# 1. Abrir arquivo:
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

#### 🐍 **Método 3: Python** *(Alternativo)*
```bash
python analise_python_puro.py
```

</td>
</tr>
</table>

---

## 📤 **ENTREGA AO PROFESSOR**

<div align="center">

### 🚨 **IMPORTANTE: Máximo 2 arquivos** *(Conforme Atividade01.pdf)*

</div>

<table align="center">
<tr>
<td width="50%" align="center">

### 📄 **Arquivo 1**
**`codigo_fonte.html`**

Relatório principal renderizado no RStudio

**Como obter:**
1. Executar `instalar_pacotes.R`
2. Abrir `codigo_fonte.qmd` no RStudio
3. Clicar em "Render"

**✅ Este é o arquivo que o professor vai avaliar**

</td>
<td width="50%" align="center">

### 📦 **Arquivo 2**
**`atividade01_entrega.zip`**

Projeto compactado com código fonte

**Como criar:**
1. Selecionar pasta `entrega/`
2. Compactar em .zip ou .rar
3. Nomear como `atividade01_entrega.zip`

**✅ Contém todo o código para reprodutibilidade**

</td>
</tr>
</table>

---

## 📊 **DADOS EXPERIMENTAIS**

### **Experimento: 4 Blocos Casualizados × 7 Procedências**

| **Procedência** | **P1** | **P2** | **P3** | **P4** | **P5** | **P6** | **P7** | **Total** |
|:---------------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:---------:|
| **Bloco I**     | 358    | 284    | 273    | 284    | 258    | 249    | 318    | **2.024** |
| **Bloco II**    | 380    | 249    | 222    | 242    | 263    | 217    | 312    | **1.885** |
| **Bloco III**   | 353    | 259    | 236    | 266    | 242    | 267    | 327    | **1.950** |
| **Bloco IV**    | 360    | 242    | 226    | 252    | 231    | 220    | 319    | **1.850** |
| **Total**       | **1.451** | **1.034** | **957** | **1.044** | **994** | **953** | **1.276** | **7.709** |

<div align="center">

**Variável:** Produção em m³.ha⁻¹ • **Tratamentos:** 7 procedências de *Eucalyptus grandis* • **Repetições:** 4 blocos

</div>

---

## 📈 **PRINCIPAIS RESULTADOS**

<div align="center">

### 🏆 **Estatísticas Principais**

| **Métrica** | **Valor** | **Interpretação** |
|:-----------:|:---------:|:-----------------:|
| **F (Procedências)** | `40,05***` | Altamente significativo (p < 0,001) |
| **F (Blocos)** | `3,75*` | Significativo (p < 0,05) |
| **CV Experimental** | `5,43%` | Excelente precisão |
| **Melhor Procedência** | **P1** | 362,75 m³.ha⁻¹ |
| **Eficiência DBC/DIC** | `130,8%` | DBC superior ao DIC |

### 🥇 **Ranking das Procedências (Teste de Tukey)**

| Posição | Procedência | Produção (m³.ha⁻¹) | Grupo Estatístico |
|:-------:|:-----------:|:------------------:|:-----------------:|
| **1º** | **P1** | **362,75** | ![A](https://img.shields.io/badge/A-success) |
| **2º** | P7 | 319,00 | ![B](https://img.shields.io/badge/B-primary) |
| 3º | P4 | 261,00 | ![C](https://img.shields.io/badge/C-warning) |
| 4º | P2 | 258,50 | ![C](https://img.shields.io/badge/C-warning) |
| 5º | P5 | 248,50 | ![C](https://img.shields.io/badge/C-warning) |
| 6º | P3 | 239,25 | ![C](https://img.shields.io/badge/C-warning) |
| **7º** | P6 | 238,25 | ![C](https://img.shields.io/badge/C-warning) |

</div>

---

## 🛠️ **ESTRUTURA DO PROJETO**

```
📦 atividade01-eucalyptus/
├── 📊 index.html                         ← Relatório PUBLICADO (Bootstrap Quarto)
├── 📋 relatorio_entrega.html             ← Relatório ENTREGA (formato professor)
├── 📚 tutorial.html                      ← Tutorial didático
├── 📖 README.md                          ← Este arquivo
├── 📂 entrega/                           ← PASTA PRINCIPAL PARA ENTREGA
│   ├── 📄 codigo_fonte.qmd              ← Código fonte Quarto ⭐
│   ├── 📄 codigo_fonte.html             ← Renderizado para entregar ⭐
│   ├── 🔧 instalar_pacotes.R            ← Instalação automática
│   ├── 📊 executar_analise.R            ← Script R alternativo
│   └── 📋 INSTRUCOES.txt                ← Instruções de execução
├── 📂 src/                               ← Scripts de apoio
├── 📂 docs/                              ← Documentação
└── 📂 data/                              ← Dados experimentais
```

---

## ✅ **CHECKLIST DE ENTREGA**

### **📝 Para o Estudante:**

**Executar antes de submeter:**
- [ ] ✅ Executei `source("entrega/instalar_pacotes.R")`
- [ ] ✅ Renderizei `entrega/codigo_fonte.qmd` no RStudio
- [ ] ✅ Arquivo `codigo_fonte.html` foi gerado sem erros
- [ ] ✅ Compactei pasta `entrega/` em arquivo `.zip`
- [ ] ✅ Tenho APENAS 2 arquivos para upload:
  - [ ] `codigo_fonte.html` (Relatório principal)
  - [ ] `atividade01_entrega.zip` (Projeto compactado)

**Validar conteúdo dos relatórios:**
- [ ] ✅ **Análise Descritiva** completa com médias e desvios
- [ ] ✅ **ANOVA DIC** com tabela e teste F
- [ ] ✅ **ANOVA DBC** com efeito de blocos
- [ ] ✅ **Comparação DIC vs DBC** com eficiência relativa
- [ ] ✅ **Teste de Tukey** com comparações múltiplas
- [ ] ✅ **Formatação Quarto** conforme solicitado

---

## 🎓 **INFORMAÇÕES ACADÊMICAS**

<div align="center">

| **Atributo** | **Detalhamento** |
|:------------:|:----------------:|
| **Disciplina** | CEN5815 - Análise de Dados Agronômicos e Ambientais |
| **Professor** | Prof. Dr. Deoclecio Jardim Amorim |
| **Atividade** | 01 - Análise ANOVA de *Eucalyptus grandis* |
| **Data de Entrega** | 29 de agosto de 2025 |
| **Formato de Entrega** | Máximo 2 arquivos (.html + .zip) |
| **Sistema** | Aceita no máximo dois arquivos para upload |

</div>

---

## 💡 **CONCLUSÕES E RECOMENDAÇÕES**

### **🏆 Principais Conclusões**
1. **Diferenças altamente significativas** entre procedências (F = 40,05; p < 0,001)
2. **P1 é estatisticamente superior** com 362,75 m³.ha⁻¹ de produção
3. **DBC mais eficiente que DIC** (CV: 5,43% vs 7,11%; Eficiência: 130,8%)
4. **Excelente precisão experimental** (CV = 5,43%) indica controle adequado

### **📋 Recomendações Técnicas**
- **🌱 Silvicultura:** Utilizar procedência P1 para plantios comerciais
- **🔬 Pesquisa:** Adotar DBC em futuros experimentos florestais
- **📈 Melhoramento:** Investir no desenvolvimento genético da P1
- **🗺️ Zoneamento:** Avaliar adaptação da P1 em diferentes regiões

---

## 🆘 **SUPORTE TÉCNICO**

### **❓ Problemas Comuns**

**Pacotes não instalam:**
```r
install.packages("agricolae", dependencies=TRUE)
install.packages(c("tidyverse", "knitr", "quarto"))
```

**Quarto não renderiza:**
- Verificar se RStudio tem Quarto atualizado
- Usar script alternativo: `source("entrega/executar_analise.R")`

**Erro de encoding:**
- Usar alternativa Python: `python analise_python_puro.py`

### **📞 Contato**
- 📧 **GitHub Issues:** [Reportar Problema](https://github.com/gabrielteoodoro/atividade01-eucalyptus/issues)
- 📚 **Tutorial Completo:** [Passo-a-passo](https://gabrielteoodoro.github.io/atividade01-eucalyptus/tutorial.html)
- 💾 **Download Projeto:** [ZIP Completo](https://github.com/gabrielteoodoro/atividade01-eucalyptus/archive/main.zip)

---

<div align="center">

## 🎯 **RESUMO PARA ENTREGA**

**🔧 Execute:** `source("entrega/instalar_pacotes.R")` → Renderize `codigo_fonte.qmd`  
**📤 Entregue:** `codigo_fonte.html` + `projeto.zip` *(máximo 2 arquivos)*

---

### **🌐 LINKS RÁPIDOS**

[![Relatório Publicado](https://img.shields.io/badge/📊_Ver-Relatório_Publicado-blue?style=for-the-badge)](https://gabrielteoodoro.github.io/atividade01-eucalyptus)
[![Relatório Entrega](https://img.shields.io/badge/📋_Ver-Relatório_Entrega-orange?style=for-the-badge)](https://gabrielteoodoro.github.io/atividade01-eucalyptus/relatorio_entrega.html)
[![Tutorial](https://img.shields.io/badge/📚_Ver-Tutorial_Didático-success?style=for-the-badge)](https://gabrielteoodoro.github.io/atividade01-eucalyptus/tutorial.html)

---

**⭐ Projeto desenvolvido seguindo rigorosamente os requisitos da Atividade01.pdf**

![GitHub Repo stars](https://img.shields.io/github/stars/gabrielteoodoro/atividade01-eucalyptus?style=social)
![GitHub forks](https://img.shields.io/github/forks/gabrielteoodoro/atividade01-eucalyptus?style=social)

*Análise estatística profissional para pesquisa florestal* 🌲

</div>