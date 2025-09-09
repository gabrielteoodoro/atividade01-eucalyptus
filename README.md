# 📊 Análise de Produção de Eucalyptus grandis

**Disciplina:** CEN5815 - Análise de Dados Agronômicos e Ambientais  
**Professor:** Prof. Dr. Deoclecio Jardim Amorim  
**Data:** 29 de agosto de 2025

---

## 📋 **RELATÓRIOS DISPONÍVEIS**

### 🚀 **[RELATÓRIO COMPLETO PUBLICADO](https://gabrielteoodoro.github.io/atividade01-eucalyptus)**
**Versão completa e interativa no GitHub Pages**
- ✅ **Análise estatística completa** - DIC, DBC, Tukey
- ✅ **Design responsivo** - Índice navegável lateral
- ✅ **Código R com syntax highlighting** - Blocos interativos
- ✅ **Resultados detalhados** - F(40.05), CV(5.43%), sessionInfo()
- ✅ **50KB de conteúdo** - Versão mais elaborada

### 📋 **[RELATÓRIO DE ENTREGA](./entrega/RELATORIO_PRINCIPAL.html)**
**Versão para submissão acadêmica**
- ✅ **Formato do professor** - Segue mod_relatorio.html exatamente
- ✅ **Análise completa** - Todos os requisitos atendidos  
- ✅ **Código limpo** - Sem elementos adicionais
- ✅ **Pronto para entregar** - Formato acadêmico padrão
- ✅ **49KB otimizado** - Para download e submissão

---

## 📁 **ESTRUTURA DO PROJETO**

### 🎓 **[ARQUIVOS DE ENTREGA](./entrega/)**
**Para submissão acadêmica:**
- `RELATORIO_PRINCIPAL.html` - **Relatório de entrega (49KB)**
- `codigo_fonte.qmd` - Código Quarto v2 corrigido
- `executar_analise.R` - Script R completo
- `instalar_pacotes.R` - Instalação automática
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

### **Opção 1: Visualizar Relatório Publicado (Recomendado)**
```
🌐 https://gabrielteoodoro.github.io/atividade01-eucalyptus
```

### **Opção 2: Baixar Relatório de Entrega**
```
📁 Clicar no link: ./entrega/RELATORIO_PRINCIPAL.html
```

### **Opção 3: RStudio/Quarto**
```r
# Instalar dependências
source("src/instalar_pacotes.R")

# Renderizar relatório
quarto::quarto_render("entrega/codigo_fonte.qmd")
```

### **Opção 4: R Console**
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

## 🎯 **QUAL RELATÓRIO USAR?**

### 🚀 **Para visualização e apresentação:**
- **Use o [Relatório Publicado](https://gabrielteoodoro.github.io/atividade01-eucalyptus)**
- Interface moderna e responsiva
- Ideal para demonstrações e consultas

### 📋 **Para entrega acadêmica:**
- **Use o [Relatório de Entrega](./entrega/RELATORIO_PRINCIPAL.html)**  
- Formato exatamente como o professor solicitou
- Para download, impressão ou submissão

---

## 📈 **PRINCIPAIS CONCLUSÕES**

1. **🎯 Diferenças altamente significativas** entre procedências (p < 0.001)
2. **🏆 P1 é a melhor procedência** com 362.75 m³.ha⁻¹  
3. **📊 DBC superior ao DIC** - Controla heterogeneidade ambiental
4. **⚡ Precisão excelente** - CV = 5.43%
5. **✅ Bloqueamento eficaz** - Efeito significativo entre blocos

**Recomendação:** Utilizar P1 em plantios comerciais e DBC em futuros experimentos.

---

## 🔗 **LINKS DIRETOS**

### **📊 VISUALIZAÇÃO:**
- **[Relatório Completo Online](https://gabrielteoodoro.github.io/atividade01-eucalyptus)** - Versão interativa
- **[Relatório de Entrega](./entrega/RELATORIO_PRINCIPAL.html)** - Para download

### **📁 NAVEGAÇÃO:**
- **[Arquivos de Entrega](./entrega/)** - Pasta completa para submissão
- **[Código Fonte](./src/)** - Scripts R desenvolvidos
- **[Documentação](./docs/)** - Materiais de referência

---

**✨ Projeto completo com duas versões de relatório: uma para visualização online e outra para entrega acadêmica**