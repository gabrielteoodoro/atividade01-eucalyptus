# 🌲 Análise de Produção de Eucalyptus grandis

<div align="center">

![Eucalyptus](https://img.shields.io/badge/Espécie-Eucalyptus_grandis-green?style=for-the-badge)
![Disciplina](https://img.shields.io/badge/CEN5815-Análise_de_Dados-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completo-success?style=for-the-badge)

**Atividade 01 - Delineamento em Blocos Casualizados (DBC)**

*Análise estatística comparativa de 7 procedências em 4 blocos*

</div>

---

## 📊 **RELATÓRIOS DISPONÍVEIS**

### 🎯 **Versão Profissional Interativa**
[![Visualizar Relatório](https://img.shields.io/badge/🌐_Visualizar-Relatório_Profissional-blue?style=for-the-badge)](https://gabrielteoodoro.github.io/atividade01-eucalyptus)

**Características:**
- ✅ **Design Bootstrap 5.3** responsivo
- ✅ **Sidebar navegável** com scroll automático
- ✅ **Gráficos interativos** Chart.js
- ✅ **Cards estatísticos** animados
- ✅ **Tabelas profissionais** com badges
- ✅ **Layout mobile-friendly**

**Uso recomendado:** Apresentações, visualização online, análise interativa

---

### 📋 **Versão Acadêmica Simples**
[![Visualizar Entrega](https://img.shields.io/badge/📄_Visualizar-Versão_Acadêmica-orange?style=for-the-badge)](https://gabrielteoodoro.github.io/atividade01-eucalyptus/relatorio_simples.html)

**Características:**
- ✅ **Formato limpo** modelo do professor
- ✅ **Estrutura acadêmica** padrão
- ✅ **Sem formatações extras**
- ✅ **Compatível RStudio/Quarto**

**Uso recomendado:** Submissão acadêmica, avaliação formal

---

## 🔬 **METODOLOGIA EXPERIMENTAL**

| **Parâmetro** | **Especificação** |
|---------------|-------------------|
| **Delineamento** | Blocos Casualizados (DBC) |
| **Tratamentos** | 7 Procedências (P1 a P7) |
| **Repetições** | 4 Blocos |
| **Unidades Experimentais** | 28 parcelas |
| **Variável Resposta** | Produção (m³.ha⁻¹) |

---

## 📈 **PRINCIPAIS RESULTADOS**

<div align="center">

| **Métrica** | **Valor** | **Interpretação** |
|-------------|-----------|-------------------|
| **F (Procedências)** | `40,05***` | Altamente significativo |
| **F (Blocos)** | `3,75*` | Significativo |
| **CV Experimental** | `5,43%` | Excelente precisão |
| **Melhor Procedência** | `P1 (362,75 m³.ha⁻¹)` | Superior estatisticamente |

</div>

### 🏆 **Ranking das Procedências**

| **Posição** | **Procedência** | **Produção** | **Classificação Tukey** |
|:-----------:|:---------------:|:------------:|:-----------------------:|
| 1º | **P1** | 362,75 m³.ha⁻¹ | ![Grupo A](https://img.shields.io/badge/Grupo-A-success) |
| 2º | **P7** | 319,00 m³.ha⁻¹ | ![Grupo B](https://img.shields.io/badge/Grupo-B-primary) |
| 3º-7º | **P4, P2, P5, P3, P6** | 238-261 m³.ha⁻¹ | ![Grupo C](https://img.shields.io/badge/Grupo-C-warning) |

---

## 🛠️ **EXECUÇÃO LOCAL**

### **Opção 1: RStudio/Quarto** ![R](https://img.shields.io/badge/R-276DC3?style=flat&logo=r&logoColor=white)

```r
# 1. Instalar dependências
source("instalar_pacotes.R")

# 2. Renderizar relatório
quarto::quarto_render("relatorio_atividade01_corrigido.qmd")

# 3. OU executar análise direta
source("executar_analise_corrigido.R")
```

### **Opção 2: Python Alternativo** ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

```bash
# Execução independente (não requer R)
python analise_python_puro.py
```

### **Opção 3: Visualização HTML** ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)

```bash
# Abrir arquivo HTML diretamente no navegador
open relatorio_profissional.html  # macOS/Linux
start relatorio_profissional.html  # Windows
```

---

## 📁 **ESTRUTURA DO PROJETO**

```
📦 atividade01-eucalyptus/
├── 📊 index.html                           # Relatório profissional (GitHub Pages)
├── 📄 relatorio_simples.html              # Versão acadêmica
├── 📋 README.md                           # Este documento
├── 📂 ATIVIDADE01_ENTREGA_FINAL/         # Arquivos para entrega
│   ├── 🗂️ RELATORIO_PRINCIPAL.html
│   └── 📝 codigo_fonte.qmd
├── 📂 docs/                              # Documentação
│   ├── 📖 INSTRUCOES_GITHUB.txt
│   └── 🎯 mod_relatorio.html
└── 📂 scripts/                           # Scripts R e Python
    ├── ⚙️ executar_analise_corrigido.R
    ├── 📦 instalar_pacotes.R
    └── 🐍 analise_python_puro.py
```

---

## 🎯 **PARÂMETROS DE AVALIAÇÃO**

### ✅ **Critérios Atendidos**

| **Requisito** | **Status** | **Localização** |
|---------------|------------|-----------------|
| **Análise Descritiva** | ✅ Completa | Seção 3 dos relatórios |
| **ANOVA DIC** | ✅ Realizada | Seção 4 dos relatórios |
| **ANOVA DBC** | ✅ Realizada | Seção 5 dos relatórios |
| **Teste de Tukey** | ✅ Com agricolae | Seção 6 dos relatórios |
| **Comparação Delineamentos** | ✅ DIC vs DBC | Seção 7 dos relatórios |
| **Relatório Quarto** | ✅ Formato .qmd | `codigo_fonte.qmd` |
| **Dados Corretos** | ✅ Total = 7.709 | Validado em todas as versões |
| **Reprodutibilidade** | ✅ Scripts R/Python | Pasta `scripts/` |

### 📊 **Validação Estatística**

- **✅ Dados originais preservados:** Soma total = 7.709
- **✅ Cálculos estatísticos corretos:** F-test, Tukey, CV
- **✅ Interpretação adequada:** Significância e recomendações
- **✅ Precisão experimental:** CV = 5,43% (excelente)

---

## 🎓 **INFORMAÇÕES ACADÊMICAS**

<div align="center">

| **Atributo** | **Detalhamento** |
|:------------:|:----------------:|
| **Disciplina** | CEN5815 - Análise de Dados Agronômicos e Ambientais |
| **Professor** | Dr. Deoclecio Jardim Amorim |
| **Instituição** | Universidade Federal - Programa de Pós-Graduação |
| **Data** | 29 de agosto de 2025 |
| **Semestre** | 2025.2 |

</div>

---

## 🔍 **CONCLUSÕES PRINCIPAIS**

### 🏆 **Resultados Estatísticos**

1. **Diferenças altamente significativas** entre procedências (F = 40,05; p < 0,001)
2. **P1 é estatisticamente superior** com 362,75 m³.ha⁻¹ de produção
3. **DBC mais eficiente que DIC** (CV: 5,43% vs 7,11%)
4. **Excelente precisão experimental** (CV = 5,43%)

### 💡 **Recomendações Técnicas**

- **🌱 Comercial:** Utilizar procedência P1 para plantios comerciais
- **🔬 Experimental:** Adotar DBC em futuros experimentos florestais
- **📈 Melhoramento:** Investir no desenvolvimento da linhagem P1
- **🗺️ Zoneamento:** Avaliar adaptação de P1 em diferentes regiões

---

## 🚀 **ACESSO RÁPIDO**

<div align="center">

[![Relatório Profissional](https://img.shields.io/badge/🎯_Acesso-Relatório_Profissional-blue?style=for-the-badge&logo=github)](https://gabrielteoodoro.github.io/atividade01-eucalyptus)

[![Versão Acadêmica](https://img.shields.io/badge/📋_Acesso-Versão_Acadêmica-orange?style=for-the-badge&logo=github)](https://gabrielteoodoro.github.io/atividade01-eucalyptus/relatorio_simples.html)

[![Download Código](https://img.shields.io/badge/💾_Download-Código_Fonte-green?style=for-the-badge&logo=download)](https://github.com/gabrielteoodoro/atividade01-eucalyptus/archive/main.zip)

</div>

---

## 📞 **SUPORTE TÉCNICO**

Para dúvidas sobre execução, análises estatísticas ou interpretação dos resultados:

- 📧 **Email:** [Inserir email acadêmico]
- 📱 **GitHub Issues:** [Reportar problemas](https://github.com/gabrielteoodoro/atividade01-eucalyptus/issues)
- 📚 **Documentação:** Pasta `docs/` do repositório

---

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela no repositório!**

![GitHub Repo stars](https://img.shields.io/github/stars/gabrielteoodoro/atividade01-eucalyptus?style=social)
![GitHub forks](https://img.shields.io/github/forks/gabrielteoodoro/atividade01-eucalyptus?style=social)

---

*Desenvolvido com 💚 para análise florestal*

![Eucalyptus](https://img.shields.io/badge/🌲-Sustentabilidade_Florestal-green?style=flat)
![R](https://img.shields.io/badge/R-276DC3?style=flat&logo=r&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=flat&logo=bootstrap&logoColor=white)

</div>