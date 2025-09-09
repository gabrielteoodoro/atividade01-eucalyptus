# 🌲 Atividade 01 - Análise de Produção de Eucalyptus grandis

**Disciplina:** CEN5815 - Análise de Dados Agronômicos e Ambientais (2025)  
**Professor:** Prof. Dr. Deoclecio Jardim Amorim  
**Data:** 29 de agosto de 2025

## 📊 Visualizar Relatório

**🔗 [CLIQUE AQUI PARA VER O RELATÓRIO COMPLETO](https://gabrielteoodoro.github.io/atividade01-eucalyptus)**

## 📋 Sobre o Experimento

Análise estatística completa de experimento com **4 blocos casualizados** e **7 procedências** de *Eucalyptus grandis*, avaliando a produção em m³.ha⁻¹.

### 🎯 Resultados Principais:
- **F (Procedências):** 40.05 (p < 0.001) - ALTAMENTE SIGNIFICATIVO
- **F (Blocos):** 3.75 (p < 0.05) - SIGNIFICATIVO  
- **CV Experimental:** 5.43% - EXCELENTE PRECISÃO
- **Melhor procedência:** P1 (362.75 m³.ha⁻¹)

## 📁 Estrutura do Projeto

### 🏆 Principal:
- **[Relatório HTML](https://gabrielteoodoro.github.io/atividade01-eucalyptus)** - Visualização online
- `src/relatorio_atividade01_corrigido.qmd` - Código Quarto fonte
- `src/executar_analise_corrigido.R` - Script R completo
- `src/instalar_pacotes.R` - Instalação automática de pacotes

### 🐍 Alternativa Python:
- `src/analise_python_puro.py` - Análise completa em Python
- `src/gerar_relatorio_final.py` - Gerador de relatório HTML

### 📦 Entrega:
- `entrega/` - Arquivos organizados para submissão
- `reports/` - Relatórios HTML gerados
- `data/` - Dados originais do experimento

## 🚀 Como Usar

### Opção 1: Visualizar Online
[**Clique aqui para ver o relatório**](https://gabrielteoodoro.github.io/atividade01-eucalyptus)

### Opção 2: Executar no RStudio
```r
# 1. Instalar pacotes
source("src/instalar_pacotes.R")

# 2. Renderizar relatório  
quarto::quarto_render("src/relatorio_atividade01_corrigido.qmd")
```

### Opção 3: Executar Python
```bash
python src/analise_python_puro.py
```

## ✅ Análises Incluídas

- [x] Análise descritiva completa
- [x] ANOVA DIC (Delineamento Inteiramente Casualizado)
- [x] ANOVA DBC (Delineamento em Blocos Casualizados)  
- [x] Comparação entre delineamentos
- [x] Teste de Tukey para comparações múltiplas
- [x] Gráficos e visualizações
- [x] Análise de pressupostos
- [x] Ranking das procedências
- [x] Conclusões e recomendações

## 🏅 Ranking das Procedências

1. **P1** - 362.75 m³.ha⁻¹ (Excelente)
2. **P7** - 319.00 m³.ha⁻¹ (Muito Bom)  
3. **P4** - 261.00 m³.ha⁻¹ (Bom)
4. **P2** - 258.50 m³.ha⁻¹ (Regular)
5. **P5** - 248.50 m³.ha⁻¹ (Regular)
6. **P3** - 239.25 m³.ha⁻¹ (Baixo)
7. **P6** - 238.25 m³.ha⁻¹ (Muito Baixo)

## 📈 Dados Experimentais Verificados

| Procedência | P1  | P2  | P3  | P4  | P5  | P6  | P7  | Total |
|-------------|-----|-----|-----|-----|-----|-----|-----|-------|
| Bloco I     | 358 | 284 | 273 | 284 | 258 | 249 | 318 | 2.024 |
| Bloco II    | 380 | 249 | 222 | 242 | 263 | 217 | 312 | 1.885 |
| Bloco III   | 353 | 259 | 236 | 266 | 242 | 267 | 327 | 1.950 |
| Bloco IV    | 360 | 242 | 226 | 252 | 231 | 220 | 319 | 1.850 |
| **Total**   |1.451|1.034| 957 |1.044| 994 | 953 |1.276| **7.709** |

✅ Todos os totais conferem com a tabela original!

## 🎓 Informações Acadêmicas

**Curso:** Análise de Dados Agronômicos e Ambientais  
**Código:** CEN5815  
**Ano:** 2025  
**Método:** ANOVA - Delineamento em Blocos Casualizados  
**Software:** R + Quarto, Python (alternativo)  

---

**📊 [VER RELATÓRIO COMPLETO](https://gabrielteoodoro.github.io/atividade01-eucalyptus)**
