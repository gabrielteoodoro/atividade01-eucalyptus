# Análise de Produção de Eucalyptus grandis - Atividade 01

**Disciplina:** CEN5815 - Análise de Dados Agronômicos e Ambientais  
**Professor:** Prof. Dr. Deoclecio Jardim Amorim  
**Data:** 29 de agosto de 2025

## 📊 Relatório Final Online

**🔗 [Ver Relatório Completo](https://gabrielteoodoro.github.io/atividade01-eucalyptus)**

O relatório completo está publicado no GitHub Pages com análise estatística completa de um experimento com 4 blocos casualizados e 7 procedências de *Eucalyptus grandis*.

## 📁 Arquivos para Entrega

### **Pasta: `ATIVIDADE01_ENTREGA_FINAL/`**

**Arquivos principais para submissão:**

1. **`RELATORIO_PRINCIPAL.html`** - Relatório final renderizado (49KB)
2. **`codigo_fonte.qmd`** - Código fonte Quarto (16KB) 
3. **`executar_analise.R`** - Script R completo (11KB)
4. **`INSTRUCOES.txt`** - Instruções de execução

**Para entregar ao professor:**
- Enviar o arquivo `RELATORIO_PRINCIPAL.html` 
- Compactar a pasta completa como ZIP/RAR (conforme solicitado)

## 🔬 Análises Realizadas

### ✅ **Requisitos Atendidos:**

1. **Análise Descritiva** - Estatísticas por procedência e bloco
2. **ANOVA DIC** - Delineamento Inteiramente Casualizado  
3. **ANOVA DBC** - Delineamento em Blocos Casualizados
4. **Teste de Tukey** - Comparações múltiplas
5. **Comparação entre Delineamentos** - Eficiência DIC vs DBC
6. **Relatório Quarto** - Formato HTML profissional

### 📈 **Principais Resultados:**

- **F (Procedências):** 40.05 (p < 0.001) - Diferenças altamente significativas
- **F (Blocos):** 3.75 (p < 0.05) - Efeito de bloco significativo  
- **CV Experimental:** 5.43% (excelente precisão)
- **Melhor Procedência:** P1 com 362.75 m³.ha⁻¹
- **DBC superior ao DIC** - Maior eficiência experimental

## 🛠️ Como Executar

### **Opção 1: RStudio/Quarto**
```r
# Instalar dependências
source("ATIVIDADE01_ENTREGA_FINAL/instalar_pacotes.R")

# Renderizar relatório
quarto::quarto_render("ATIVIDADE01_ENTREGA_FINAL/codigo_fonte.qmd")
```

### **Opção 2: R Console**
```r
# Executar análise completa
source("ATIVIDADE01_ENTREGA_FINAL/executar_analise.R")
```

## 📊 Estrutura dos Dados

**Experimento:** 4 blocos × 7 procedências = 28 parcelas  
**Variável:** Produção em m³.ha⁻¹  

| Bloco/Proc | P1  | P2  | P3  | P4  | P5  | P6  | P7  | Total |
|------------|-----|-----|-----|-----|-----|-----|-----|-------|
| Bloco I    | 358 | 284 | 273 | 284 | 258 | 249 | 318 | 2.024 |
| Bloco II   | 380 | 249 | 222 | 242 | 263 | 217 | 312 | 1.885 |
| Bloco III  | 353 | 259 | 236 | 266 | 242 | 267 | 327 | 1.950 |
| Bloco IV   | 360 | 242 | 226 | 252 | 231 | 220 | 319 | 1.850 |
| **Total**  |**1.451**|**1.034**|**957**|**1.044**|**994**|**953**|**1.276**|**7.709**|

## 🎯 Repositório GitHub

**🔗 [https://github.com/gabrielteoodoro/atividade01-eucalyptus](https://github.com/gabrielteoodoro/atividade01-eucalyptus)**

---

*Análise completa conforme requisitos da Atividade01.pdf*