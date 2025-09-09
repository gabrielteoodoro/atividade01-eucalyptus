# 📊 Análise de Produção de Eucalyptus grandis

**Disciplina:** CEN5815 - Análise de Dados Agronômicos e Ambientais  
**Professor:** Prof. Dr. Deoclecio Jardim Amorim  
**Data:** 29 de agosto de 2025

---

## 🔥 **VISUALIZAR RELATÓRIO COMPLETO**

### 📋 **[🚀 RELATÓRIO INTERATIVO ONLINE](https://gabrielteoodoro.github.io/atividade01-eucalyptus)**

**O relatório completo e interativo está publicado no GitHub Pages!**

- ✅ **Análise estatística completa** - DIC, DBC, Tukey
- ✅ **Gráficos e tabelas interativas** - Visualização profissional  
- ✅ **Resultados detalhados** - F(40.05), CV(5.43%), P1 melhor procedência
- ✅ **Design responsivo** - Funciona em qualquer dispositivo
- ✅ **Índice navegável** - Acesso rápido às seções

---

## 📁 **ABAS DO PROJETO**

### 🎓 **[ARQUIVOS DE ENTREGA](./entrega/)**
**Para submissão acadêmica:**
- `RELATORIO_PRINCIPAL.html` - Relatório final (50KB)
- `codigo_fonte.qmd` - Código Quarto v2 corrigido
- `executar_analise.R` - Script R completo
- `INSTRUCOES.txt` - Como executar

### 📚 **[DOCUMENTAÇÃO](./docs/)**
**Materiais de referência:**
- `Atividade01.pdf` - Enunciado original
- `mod_relatorio.html` - Modelo fornecido pelo professor

### 💻 **[CÓDIGO FONTE](./src/)**
**Scripts desenvolvidos:**
- `executar_analise.R` - Análise estatística completa
- `instalar_pacotes.R` - Instalação automática de dependências

---

## 🔬 **ANÁLISES REALIZADAS**

### 📊 **Experimento: 4 Blocos × 7 Procedências**

| **Análise** | **Resultado** | **Interpretação** |
|-------------|---------------|-------------------|
| **ANOVA DIC** | F = 23.89 (p < 0.001) | Diferenças significativas |
| **ANOVA DBC** | F = 40.05 (p < 0.001) | **DBC mais eficiente** |
| **Efeito Blocos** | F = 3.75 (p < 0.05) | Bloqueamento justificado |
| **CV Experimental** | 5.43% | **Excelente precisão** |
| **Melhor Procedência** | P1 = 362.75 m³.ha⁻¹ | **Maior produtividade** |

### 🏆 **Ranking de Procedências:**
1. **P1:** 362.75 m³.ha⁻¹ ⭐ (melhor)
2. **P7:** 319.00 m³.ha⁻¹  
3. **P4:** 261.00 m³.ha⁻¹
4. **P2:** 258.50 m³.ha⁻¹
5. **P5:** 248.50 m³.ha⁻¹
6. **P3:** 239.25 m³.ha⁻¹
7. **P6:** 238.25 m³.ha⁻¹ (menor)

---

## 🛠️ **COMO EXECUTAR**

### **Opção 1: Visualizar Online (Recomendado)**
```
🌐 https://gabrielteoodoro.github.io/atividade01-eucalyptus
```

### **Opção 2: RStudio/Quarto**
```r
# Instalar dependências
source("src/instalar_pacotes.R")

# Renderizar relatório
quarto::quarto_render("entrega/codigo_fonte.qmd")
```

### **Opção 3: R Console**
```r
# Executar análise completa
source("src/executar_analise.R")
```

---

## 📊 **DADOS DO EXPERIMENTO**

**Produção em m³.ha⁻¹ por Bloco e Procedência:**

| **Bloco** | **P1** | **P2** | **P3** | **P4** | **P5** | **P6** | **P7** | **Total** |
|-----------|--------|--------|--------|--------|--------|--------|--------|-----------|
| **I**     | 358    | 284    | 273    | 284    | 258    | 249    | 318    | 2.024     |
| **II**    | 380    | 249    | 222    | 242    | 263    | 217    | 312    | 1.885     |
| **III**   | 353    | 259    | 236    | 266    | 242    | 267    | 327    | 1.950     |
| **IV**    | 360    | 242    | 226    | 252    | 231    | 220    | 319    | 1.850     |
| **Total** | **1.451** | **1.034** | **957** | **1.044** | **994** | **953** | **1.276** | **7.709** |

---

## 📈 **PRINCIPAIS CONCLUSÕES**

1. **🎯 Diferenças altamente significativas** entre procedências (p < 0.001)
2. **🏆 P1 é a melhor procedência** com 362.75 m³.ha⁻¹  
3. **📊 DBC superior ao DIC** - Controla heterogeneidade ambiental
4. **⚡ Precisão excelente** - CV = 5.43%
5. **✅ Bloqueamento eficaz** - Efeito significativo entre blocos

**Recomendação:** Utilizar P1 em plantios comerciais e DBC em futuros experimentos.

---

## 🔗 **LINKS ÚTEIS**

- **📊 [Relatório Completo Online](https://gabrielteoodoro.github.io/atividade01-eucalyptus)**
- **📁 [Arquivos de Entrega](./entrega/)**
- **💻 [Código Fonte](./src/)**
- **📚 [Documentação](./docs/)**

---

**✨ Análise estatística completa de experimento florestal com Eucalyptus grandis**