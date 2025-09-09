# Script para instalar todos os pacotes necessários para a Atividade 01
# Execute este script ANTES de renderizar o relatório Quarto

cat("===================================================================\n")
cat("INSTALAÇÃO DE PACOTES - ATIVIDADE 01\n")
cat("CEN5815 - Análise de Dados Agronômicos e Ambientais\n")
cat("===================================================================\n\n")

# Lista completa de pacotes necessários
pacotes_necessarios <- c(
  "tidyverse",    # Manipulação de dados (dplyr, ggplot2, etc.)
  "knitr",        # Tabelas e relatórios
  "broom",        # Resultados estatísticos organizados
  "ggplot2",      # Gráficos (já incluído no tidyverse)
  "agricolae",    # Testes estatísticos agrícolas (Tukey)
  "here",         # Caminhos de arquivos
  "quarto"        # Sistema de relatórios
)

# Lista de pacotes opcionais (úteis mas não obrigatórios)
pacotes_opcionais <- c(
  "rmarkdown",    # Alternativa ao Quarto
  "readxl",       # Leitura de arquivos Excel
  "writexl",      # Escrita de arquivos Excel
  "car",          # Análises estatísticas adicionais
  "multcomp"      # Comparações múltiplas
)

cat("Verificando e instalando pacotes necessários...\n\n")

# Função para verificar e instalar pacotes
instalar_se_necessario <- function(pacotes, tipo = "necessários") {
  cat("---", toupper(tipo), "---\n")
  
  for(pacote in pacotes) {
    cat("Verificando", pacote, "... ")
    
    if(!require(pacote, character.only = TRUE, quietly = TRUE)) {
      cat("INSTALANDO\n")
      
      tryCatch({
        install.packages(pacote, dependencies = TRUE, repos = "http://cran.r-project.org")
        
        # Verificar se foi instalado com sucesso
        if(require(pacote, character.only = TRUE, quietly = TRUE)) {
          cat("  ✓", pacote, "instalado com sucesso\n")
        } else {
          cat("  ✗ ERRO ao instalar", pacote, "\n")
        }
      }, error = function(e) {
        cat("  ✗ ERRO:", e$message, "\n")
      })
      
    } else {
      cat("OK (já instalado)\n")
    }
  }
  cat("\n")
}

# Instalar pacotes necessários
instalar_se_necessario(pacotes_necessarios, "necessários")

# Perguntar sobre pacotes opcionais
cat("Deseja instalar pacotes opcionais? (recomendado)\n")
cat("Os pacotes opcionais incluem funcionalidades extras como:\n")
cat("- Leitura/escrita de arquivos Excel\n")
cat("- Análises estatísticas adicionais\n")
cat("- Comparações múltiplas avançadas\n\n")

# Para automatizar, vou instalar todos os opcionais
cat("Instalando pacotes opcionais automaticamente...\n")
instalar_se_necessario(pacotes_opcionais, "opcionais")

# Verificar instalações
cat("===================================================================\n")
cat("VERIFICAÇÃO FINAL\n")
cat("===================================================================\n\n")

todos_pacotes <- c(pacotes_necessarios, pacotes_opcionais)
instalados <- character()
nao_instalados <- character()

for(pacote in todos_pacotes) {
  if(require(pacote, character.only = TRUE, quietly = TRUE)) {
    instalados <- c(instalados, pacote)
  } else {
    nao_instalados <- c(nao_instalados, pacote)
  }
}

cat("PACOTES INSTALADOS COM SUCESSO (", length(instalados), "):\n")
for(p in instalados) {
  cat("  ✓", p, "\n")
}

if(length(nao_instalados) > 0) {
  cat("\nPACOTES COM PROBLEMAS (", length(nao_instalados), "):\n")
  for(p in nao_instalados) {
    cat("  ✗", p, "\n")
  }
  cat("\nTente instalar manualmente os pacotes com problema:\n")
  cat("install.packages(c(\"", paste(nao_instalados, collapse = "\", \""), "\"))\n")
} else {
  cat("\n🎉 TODOS OS PACOTES FORAM INSTALADOS COM SUCESSO!\n")
}

cat("\n===================================================================\n")
cat("PRÓXIMOS PASSOS:\n")
cat("===================================================================\n")
cat("1. Abra o arquivo 'relatorio_atividade01_corrigido.qmd' no RStudio\n")
cat("2. Clique em 'Render' para gerar o relatório HTML\n")
cat("3. Ou execute: quarto::quarto_render('relatorio_atividade01_corrigido.qmd')\n")
cat("\nAlternativamente, use o script R direto:\n")
cat("4. Execute: source('executar_analise.R')\n")
cat("\n===================================================================\n")

# Testar carregamento dos pacotes essenciais
cat("TESTE DE CARREGAMENTO DOS PACOTES ESSENCIAIS:\n")
essenciais <- c("tidyverse", "agricolae", "knitr")

for(pacote in essenciais) {
  tryCatch({
    library(pacote, character.only = TRUE)
    cat("✓", pacote, "carregado com sucesso\n")
  }, error = function(e) {
    cat("✗", pacote, "ERRO ao carregar:", e$message, "\n")
  })
}

cat("\n🔧 Script de instalação concluído!\n")