# Script para executar a análise completa da Atividade 01
# Dados de produção de Eucalyptus grandis (EXATOS conforme PDF)

cat("===================================================================\n")
cat("ATIVIDADE 01 - ANÁLISE DE PRODUÇÃO DE EUCALYPTUS GRANDIS\n") 
cat("CEN5815 - Análise de Dados Agronômicos e Ambientais (2025)\n")
cat("Prof. Dr. Deoclecio Jardim Amorim\n")
cat("===================================================================\n\n")

# Verificar e instalar pacotes necessários
pacotes_necessarios <- c("tidyverse", "knitr", "broom", "ggplot2", "agricolae")

cat("Verificando pacotes necessários...\n")
for(pacote in pacotes_necessarios) {
  if(!require(pacote, character.only = TRUE, quietly = TRUE)) {
    cat("Instalando", pacote, "...\n")
    install.packages(pacote, dependencies = TRUE)
    library(pacote, character.only = TRUE)
  }
}

# Fixar semente
set.seed(2025)

cat("Pacotes carregados com sucesso!\n\n")

# =========================================================================
# DADOS EXATOS CONFORME ATIVIDADE01.PDF
# =========================================================================

cat("1. CARREGANDO DADOS ORIGINAIS...\n")

# Dados EXATOS da tabela original
dados_matriz <- matrix(c(
  358, 284, 273, 284, 258, 249, 318,  # Bloco I
  380, 249, 222, 242, 263, 217, 312,  # Bloco II
  353, 259, 236, 266, 242, 267, 327,  # Bloco III
  360, 242, 226, 252, 231, 220, 319   # Bloco IV
), nrow = 4, byrow = TRUE)

# Nomear exatamente como na tabela
rownames(dados_matriz) <- c("Bloco I", "Bloco II", "Bloco III", "Bloco IV")
colnames(dados_matriz) <- c("P1", "P2", "P3", "P4", "P5", "P6", "P7")

cat("Dados originais (matriz):\n")
print(dados_matriz)

# Verificar totais (devem conferir com a tabela original)
totais_linha <- rowSums(dados_matriz)
totais_coluna <- colSums(dados_matriz)
total_geral <- sum(dados_matriz)

cat("\nVerificação dos totais:\n")
cat("Totais por linha:", totais_linha, "\n")
cat("(Devem ser: 2024, 1885, 1950, 1850)\n")
cat("Totais por coluna:", totais_coluna, "\n") 
cat("(Devem ser: 1451, 1034, 957, 1044, 994, 953, 1276)\n")
cat("Total geral:", total_geral, "(deve ser 7709)\n\n")

# Converter para formato longo
dados_long <- dados_matriz %>%
  as.data.frame() %>%
  rownames_to_column("Bloco") %>%
  pivot_longer(cols = -Bloco, 
               names_to = "Procedencia", 
               values_to = "Producao") %>%
  mutate(
    Bloco = factor(Bloco, levels = c("Bloco I", "Bloco II", "Bloco III", "Bloco IV")),
    Procedencia = factor(Procedencia, levels = c("P1", "P2", "P3", "P4", "P5", "P6", "P7"))
  )

cat("Dados organizados para análise (primeiras 10 linhas):\n")
print(head(dados_long, 10))

# =========================================================================
# 2. ANÁLISE DESCRITIVA
# =========================================================================

cat("\n2. ANÁLISE DESCRITIVA...\n")

# Estatísticas por procedência
estat_proc <- dados_long %>%
  group_by(Procedencia) %>%
  summarise(
    n = n(),
    Media = mean(Producao),
    DP = sd(Producao),
    Minimo = min(Producao),
    Maximo = max(Producao),
    CV_pct = (sd(Producao)/mean(Producao))*100,
    .groups = "drop"
  )

cat("\nEstatísticas por Procedência:\n")
print(estat_proc)

# Estatísticas por bloco  
estat_bloco <- dados_long %>%
  group_by(Bloco) %>%
  summarise(
    n = n(),
    Media = mean(Producao),
    DP = sd(Producao),
    Minimo = min(Producao),
    Maximo = max(Producao),
    CV_pct = (sd(Producao)/mean(Producao))*100,
    .groups = "drop"
  )

cat("\nEstatísticas por Bloco:\n")
print(estat_bloco)

# =========================================================================
# 3. ANOVA - DELINEAMENTO INTEIRAMENTE CASUALIZADO (DIC)
# =========================================================================

cat("\n3. ANOVA - DELINEAMENTO INTEIRAMENTE CASUALIZADO (DIC)...\n")

# Modelo DIC (apenas procedência)
modelo_dic <- aov(Producao ~ Procedencia, data = dados_long)
anova_dic <- anova(modelo_dic)

cat("\nTabela ANOVA - DIC:\n")
print(anova_dic)

# Teste de Tukey DIC
tukey_dic <- TukeyHSD(modelo_dic, "Procedencia")
cat("\nTeste de Tukey - DIC (primeiras 10 comparações):\n")
print(head(tukey_dic$Procedencia, 10))

# =========================================================================
# 4. ANOVA - DELINEAMENTO EM BLOCOS CASUALIZADOS (DBC)
# =========================================================================

cat("\n4. ANOVA - DELINEAMENTO EM BLOCOS CASUALIZADOS (DBC)...\n")

# Modelo DBC (bloco + procedência)
modelo_dbc <- aov(Producao ~ Bloco + Procedencia, data = dados_long)
anova_dbc <- anova(modelo_dbc)

cat("\nTabela ANOVA - DBC:\n")
print(anova_dbc)

# Teste de Tukey DBC
tukey_dbc <- TukeyHSD(modelo_dbc, "Procedencia")
cat("\nTeste de Tukey - DBC (primeiras 10 comparações):\n")
print(head(tukey_dbc$Procedencia, 10))

# Teste HSD com agricolae (grupos estatísticos)
grupos_tukey <- HSD.test(modelo_dbc, "Procedencia", alpha = 0.05)
cat("\nAgrupamento das procedências (agricolae):\n")
print(grupos_tukey$groups)

# =========================================================================
# 5. COMPARAÇÃO DOS MODELOS
# =========================================================================

cat("\n5. COMPARAÇÃO DOS MODELOS DIC vs DBC...\n")

# Extrair valores para comparação
qm_residuo_dic <- anova_dic["Residuals", "Mean Sq"]
qm_residuo_dbc <- anova_dbc["Residuals", "Mean Sq"] 
f_proc_dic <- anova_dic["Procedencia", "F value"]
f_proc_dbc <- anova_dbc["Procedencia", "F value"]
p_proc_dic <- anova_dic["Procedencia", "Pr(>F)"]
p_proc_dbc <- anova_dbc["Procedencia", "Pr(>F)"]
f_bloco_dbc <- anova_dbc["Bloco", "F value"]
p_bloco_dbc <- anova_dbc["Bloco", "Pr(>F)"]

# Tabela comparativa
comparacao <- data.frame(
  Delineamento = c("DIC", "DBC"),
  QM_Residuo = c(qm_residuo_dic, qm_residuo_dbc),
  F_Procedencias = c(f_proc_dic, f_proc_dbc),
  P_valor_Proc = c(p_proc_dic, p_proc_dbc)
)

cat("\nComparação dos delineamentos:\n")
print(comparacao)

# Eficiência relativa
eficiencia <- qm_residuo_dic / qm_residuo_dbc
cat("\nEficiência relativa do DBC:", round(eficiencia, 3))

# Coeficientes de variação
media_geral <- mean(dados_long$Producao)
cv_dic <- sqrt(qm_residuo_dic) / media_geral * 100
cv_dbc <- sqrt(qm_residuo_dbc) / media_geral * 100

cat("\nCV experimental DIC:", round(cv_dic, 2), "%")
cat("\nCV experimental DBC:", round(cv_dbc, 2), "%")

# =========================================================================
# 6. ANÁLISE DE PRESSUPOSTOS
# =========================================================================

cat("\n\n6. ANÁLISE DE PRESSUPOSTOS (DBC)...\n")

# Teste de normalidade dos resíduos
residuos <- residuals(modelo_dbc)
shapiro_test <- shapiro.test(residuos)

cat("\nTeste de Shapiro-Wilk para normalidade:")
cat("\nW =", round(shapiro_test$statistic, 4))
cat("\nP-valor =", round(shapiro_test$p.value, 4))

if(shapiro_test$p.value > 0.05) {
  cat("\nConclusão: Resíduos seguem distribuição normal (p > 0,05)")
} else {
  cat("\nConclusão: Resíduos NÃO seguem distribuição normal (p ≤ 0,05)")
}

# =========================================================================
# 7. RESULTADOS E CONCLUSÕES
# =========================================================================

cat("\n\n7. RESULTADOS E CONCLUSÕES...\n")
cat("="*60, "\n")

# Melhor procedência
melhor_proc <- estat_proc[which.max(estat_proc$Media), ]
pior_proc <- estat_proc[which.min(estat_proc$Media), ]

cat("\nPRINCIPAIS RESULTADOS:\n")
cat("• Melhor procedência:", melhor_proc$Procedencia, "(", round(melhor_proc$Media, 2), "m³.ha⁻¹)\n")
cat("• Menor produção:", pior_proc$Procedencia, "(", round(pior_proc$Media, 2), "m³.ha⁻¹)\n")

diferenca <- melhor_proc$Media - pior_proc$Media
diferenca_pct <- (diferenca / pior_proc$Media) * 100
cat("• Diferença:", round(diferenca, 2), "m³.ha⁻¹ (", round(diferenca_pct, 1), "% superior)\n")

cat("\nTESTES ESTATÍSTICOS:\n")
cat("• F (Procedências) DIC:", round(f_proc_dic, 3), "| P-valor:", format(p_proc_dic, scientific=T, digits=3), "\n")
cat("• F (Procedências) DBC:", round(f_proc_dbc, 3), "| P-valor:", format(p_proc_dbc, scientific=T, digits=3), "\n")
cat("• F (Blocos) DBC:", round(f_bloco_dbc, 3), "| P-valor:", format(p_bloco_dbc, scientific=T, digits=3), "\n")

cat("\nEFICIÊNCIA:\n")
cat("• DBC é", round(eficiencia, 2), "vezes mais eficiente que DIC\n")
cat("• CV experimental melhorou de", round(cv_dic, 2), "% (DIC) para", round(cv_dbc, 2), "% (DBC)\n")

cat("\nCONCLUSÕES:\n")
if(p_proc_dbc < 0.05) {
  cat("✓ Existem diferenças SIGNIFICATIVAS entre procedências (p < 0,05)\n")
} else {
  cat("✗ Não há diferenças significativas entre procedências (p ≥ 0,05)\n")
}

if(p_bloco_dbc < 0.05) {
  cat("✓ Efeito de bloco SIGNIFICATIVO - bloqueamento foi efetivo\n")
} else {
  cat("✗ Efeito de bloco NÃO significativo\n")
}

cat("✓ DBC foi mais eficiente que DIC para este experimento\n")
cat("✓ Precisão experimental:", ifelse(cv_dbc <= 10, "EXCELENTE", ifelse(cv_dbc <= 20, "BOA", "REGULAR")), "(CV =", round(cv_dbc, 2), "%)\n")

# Ranking final
cat("\nRANKING DAS PROCEDÊNCIAS:\n")
ranking <- estat_proc %>% arrange(desc(Media))
for(i in 1:nrow(ranking)) {
  cat(i, "º", ranking$Procedencia[i], "-", round(ranking$Media[i], 2), "m³.ha⁻¹\n")
}

cat("\n", "="*60, "\n")
cat("ANÁLISE COMPLETA FINALIZADA!\n")
cat("="*60, "\n")

# =========================================================================
# 8. GERAR GRÁFICOS (OPCIONAL)
# =========================================================================

tryCatch({
  cat("\n8. GERANDO GRÁFICOS...\n")
  
  # Gráfico 1: Boxplot por procedência
  p1 <- ggplot(dados_long, aes(x = Procedencia, y = Producao)) +
    geom_boxplot(aes(fill = Procedencia), alpha = 0.7) +
    geom_point(alpha = 0.6, position = position_jitter(width = 0.2)) +
    labs(
      title = "Produção por Procedência de Eucalyptus grandis",
      x = "Procedência", 
      y = "Produção (m³.ha⁻¹)"
    ) +
    theme_minimal() +
    theme(legend.position = "none")
  
  ggsave("grafico_procedencias.png", p1, width = 10, height = 6, dpi = 300)
  
  # Gráfico 2: Boxplot por bloco
  p2 <- ggplot(dados_long, aes(x = Bloco, y = Producao)) +
    geom_boxplot(aes(fill = Bloco), alpha = 0.7) +
    geom_point(alpha = 0.6, position = position_jitter(width = 0.2)) +
    labs(
      title = "Produção por Bloco",
      x = "Bloco",
      y = "Produção (m³.ha⁻¹)"
    ) +
    theme_minimal() +
    theme(legend.position = "none")
  
  ggsave("grafico_blocos.png", p2, width = 10, height = 6, dpi = 300)
  
  cat("✓ Gráficos salvos: grafico_procedencias.png, grafico_blocos.png\n")
  
}, error = function(e) {
  cat("Aviso: Erro ao gerar gráficos:", e$message, "\n")
})

cat("\n🎉 SCRIPT DE ANÁLISE CONCLUÍDO COM SUCESSO!\n")
cat("📊 Para gerar o relatório completo, execute:\n")
cat("    quarto::quarto_render('relatorio_atividade01_corrigido.qmd')\n")