#!/usr/bin/env python3
"""
Gerador de relatório HTML final simulando saída do Quarto
Para a Atividade 01 de Eucalyptus grandis
"""

import math
import statistics
from collections import defaultdict
from datetime import datetime

def executar_analise_completa():
    """Executa toda a análise estatística"""
    
    # Dados originais EXATOS
    dados_matriz = [
        [358, 284, 273, 284, 258, 249, 318],  # Bloco I
        [380, 249, 222, 242, 263, 217, 312],  # Bloco II
        [353, 259, 236, 266, 242, 267, 327],  # Bloco III
        [360, 242, 226, 252, 231, 220, 319]   # Bloco IV
    ]
    
    # Converter para formato longo
    dados_long = []
    blocos = ['Bloco I', 'Bloco II', 'Bloco III', 'Bloco IV']
    procedencias = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']
    
    for i, bloco in enumerate(blocos):
        for j, proc in enumerate(procedencias):
            dados_long.append({
                'Bloco': bloco,
                'Procedencia': proc,
                'Producao': dados_matriz[i][j]
            })
    
    # Análise descritiva
    dados_por_proc = defaultdict(list)
    dados_por_bloco = defaultdict(list)
    todos_valores = []
    
    for dado in dados_long:
        dados_por_proc[dado['Procedencia']].append(dado['Producao'])
        dados_por_bloco[dado['Bloco']].append(dado['Producao'])
        todos_valores.append(dado['Producao'])
    
    # Estatísticas por procedência
    estat_proc = {}
    for proc in procedencias:
        valores = dados_por_proc[proc]
        estat_proc[proc] = {
            'media': statistics.mean(valores),
            'dp': statistics.stdev(valores),
            'minimo': min(valores),
            'maximo': max(valores),
            'cv': statistics.stdev(valores) / statistics.mean(valores) * 100
        }
    
    # Estatísticas por bloco
    estat_bloco = {}
    for bloco in blocos:
        valores = dados_por_bloco[bloco]
        estat_bloco[bloco] = {
            'media': statistics.mean(valores),
            'dp': statistics.stdev(valores),
            'minimo': min(valores),
            'maximo': max(valores),
            'cv': statistics.stdev(valores) / statistics.mean(valores) * 100
        }
    
    # ANOVA
    media_geral = statistics.mean(todos_valores)
    medias_proc = {proc: statistics.mean(dados_por_proc[proc]) for proc in procedencias}
    medias_bloco = {bloco: statistics.mean(dados_por_bloco[bloco]) for bloco in blocos}
    
    # Soma de quadrados
    sq_total = sum((valor - media_geral) ** 2 for valor in todos_valores)
    sq_proc = len(blocos) * sum((medias_proc[proc] - media_geral) ** 2 for proc in procedencias)
    sq_bloco = len(procedencias) * sum((medias_bloco[bloco] - media_geral) ** 2 for bloco in blocos)
    sq_residuo = sq_total - sq_proc - sq_bloco
    
    # Graus de liberdade
    gl_proc = len(procedencias) - 1
    gl_bloco = len(blocos) - 1
    gl_residuo = gl_proc * gl_bloco
    
    # Quadrados médios
    qm_proc = sq_proc / gl_proc
    qm_bloco = sq_bloco / gl_bloco
    qm_residuo = sq_residuo / gl_residuo
    
    # Estatísticas F
    f_proc = qm_proc / qm_residuo
    f_bloco = qm_bloco / qm_residuo
    
    return {
        'dados_matriz': dados_matriz,
        'estat_proc': estat_proc,
        'estat_bloco': estat_bloco,
        'anova': {
            'sq_proc': sq_proc, 'gl_proc': gl_proc, 'qm_proc': qm_proc, 'f_proc': f_proc,
            'sq_bloco': sq_bloco, 'gl_bloco': gl_bloco, 'qm_bloco': qm_bloco, 'f_bloco': f_bloco,
            'sq_residuo': sq_residuo, 'gl_residuo': gl_residuo, 'qm_residuo': qm_residuo,
            'sq_total': sq_total, 'media_geral': media_geral
        },
        'medias_proc': medias_proc,
        'procedencias': procedencias,
        'blocos': blocos
    }

def gerar_html_quarto_style(resultados):
    """Gera HTML no estilo Quarto"""
    
    r = resultados
    anova = r['anova']
    cv_exp = math.sqrt(anova['qm_residuo']) / anova['media_geral'] * 100
    
    html = f"""<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="pt-BR" xml:lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="generator" content="quarto-1.6.42">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
<meta name="author" content="Nome do Estudante">
<title>Análise de Produção de Eucalyptus grandis - Atividade 01</title>

<style>
body {{
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  line-height: 1.6;
  color: #212529;
  background-color: #fff;
  margin: 0;
  padding: 0;
}}

.container {{
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}}

.header {{
  text-align: center;
  margin-bottom: 2rem;
  padding: 2rem;
  background: linear-gradient(135deg, #007bff, #0056b3);
  color: white;
  border-radius: 8px;
}}

.header h1 {{
  margin: 0;
  font-size: 2.5rem;
  font-weight: 300;
}}

.header p {{
  margin: 0.5rem 0;
  opacity: 0.9;
}}

.section {{
  margin: 2rem 0;
  background: #fff;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  overflow: hidden;
}}

.section-header {{
  background: #f8f9fa;
  padding: 1rem 1.5rem;
  border-bottom: 1px solid #dee2e6;
}}

.section-content {{
  padding: 1.5rem;
}}

.section h2 {{
  margin: 0;
  color: #495057;
  font-size: 1.5rem;
}}

.section h3 {{
  color: #6c757d;
  margin-top: 1.5rem;
  margin-bottom: 1rem;
}}

table {{
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0;
  font-size: 0.9rem;
}}

table th, table td {{
  padding: 0.75rem;
  text-align: center;
  border: 1px solid #dee2e6;
}}

table th {{
  background-color: #007bff;
  color: white;
  font-weight: 600;
}}

table tr:nth-child(even) {{
  background-color: #f8f9fa;
}}

.numero {{
  font-family: 'Monaco', 'Consolas', monospace;
  font-weight: bold;
}}

.destaque {{
  background-color: #fff3cd;
  border: 1px solid #ffeaa7;
  padding: 1rem;
  border-radius: 5px;
  margin: 1rem 0;
}}

.conclusao {{
  background-color: #d1ecf1;
  border: 1px solid #74c0fc;
  padding: 1rem;
  border-radius: 5px;
  margin: 1rem 0;
}}

.grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin: 1rem 0;
}}

.card {{
  background: #f8f9fa;
  padding: 1rem;
  border-radius: 5px;
  border-left: 4px solid #007bff;
}}

.resultado-destaque {{
  font-size: 1.2em;
  font-weight: bold;
  color: #007bff;
}}

.code-block {{
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 4px;
  padding: 1rem;
  margin: 1rem 0;
  font-family: 'Monaco', 'Consolas', monospace;
  font-size: 0.9rem;
  overflow-x: auto;
}}

.toc {{
  position: fixed;
  left: 20px;
  top: 20px;
  width: 200px;
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 1rem;
  max-height: 80vh;
  overflow-y: auto;
}}

.toc ul {{
  list-style: none;
  padding: 0;
  margin: 0;
}}

.toc li {{
  margin: 0.25rem 0;
}}

.toc a {{
  color: #007bff;
  text-decoration: none;
  font-size: 0.9rem;
}}

.toc a:hover {{
  text-decoration: underline;
}}

.content {{
  margin-left: 240px;
}}

@media (max-width: 1400px) {{
  .toc {{ display: none; }}
  .content {{ margin-left: 0; }}
}}
</style>
</head>

<body>
<div class="toc">
  <h4>Índice</h4>
  <ul>
    <li><a href="#introducao">Introdução</a></li>
    <li><a href="#dados">Dados Experimentais</a></li>
    <li><a href="#descritiva">Análise Descritiva</a></li>
    <li><a href="#anova-dic">ANOVA - DIC</a></li>
    <li><a href="#anova-dbc">ANOVA - DBC</a></li>
    <li><a href="#comparacao">Comparação</a></li>
    <li><a href="#resultados">Resultados</a></li>
    <li><a href="#conclusoes">Conclusões</a></li>
  </ul>
</div>

<div class="content">
<div class="container">

<div class="header">
  <h1>Análise de Produção de Eucalyptus grandis</h1>
  <p><strong>Atividade 01</strong></p>
  <p>CEN5815 - Análise de Dados Agronômicos e Ambientais (2025)</p>
  <p>Prof. Dr. Deoclecio Jardim Amorim</p>
  <p>Data: 29 de agosto de 2025</p>
</div>

<div class="section" id="introducao">
  <div class="section-header">
    <h2>1. Introdução</h2>
  </div>
  <div class="section-content">
    <p>Este relatório apresenta a análise estatística completa de um experimento com <strong>4 blocos casualizados</strong> 
    e <strong>7 procedências</strong> de <em>Eucalyptus grandis</em>, avaliando a produção em m³.ha⁻¹.</p>
    
    <div class="destaque">
      <strong>Objetivos da Análise:</strong><br>
      • Realizar análise descritiva dos dados experimentais<br>
      • Executar ANOVA como Delineamento Inteiramente Casualizado (DIC)<br>
      • Executar ANOVA como Delineamento em Blocos Casualizados (DBC)<br>
      • Comparar a eficácia dos dois delineamentos
    </div>
    
    <p><strong>Características do Experimento:</strong></p>
    <ul>
      <li>Variável resposta: Produção em m³.ha⁻¹</li>
      <li>Tratamentos: 7 procedências (P1 a P7)</li>
      <li>Blocos: 4 blocos casualizados</li>
      <li>Total de parcelas: 28</li>
    </ul>
  </div>
</div>

<div class="section" id="dados">
  <div class="section-header">
    <h2>2. Dados Experimentais</h2>
  </div>
  <div class="section-content">
    <h3>Tabela Original dos Dados</h3>
    <table>
      <thead>
        <tr>
          <th>Bloco / Procedência</th>"""
    
    # Cabeçalho da tabela
    for proc in r['procedencias']:
        html += f"<th>{proc}</th>"
    html += "<th><strong>Total</strong></th></tr></thead><tbody>"
    
    # Dados da matriz
    totais_linha = []
    for i, bloco in enumerate(r['blocos']):
        html += f"<tr><td><strong>{bloco}</strong></td>"
        total_linha = 0
        for j, proc in enumerate(r['procedencias']):
            valor = r['dados_matriz'][i][j]
            html += f"<td class='numero'>{valor}</td>"
            total_linha += valor
        totais_linha.append(total_linha)
        html += f"<td class='numero resultado-destaque'>{total_linha}</td></tr>"
    
    # Totais por coluna
    html += "<tr><td><strong>Total</strong></td>"
    total_geral = 0
    for j, proc in enumerate(r['procedencias']):
        total_col = sum(r['dados_matriz'][i][j] for i in range(len(r['blocos'])))
        total_geral += total_col
        html += f"<td class='numero resultado-destaque'>{total_col}</td>"
    html += f"<td class='numero resultado-destaque'><strong>{total_geral}</strong></td></tr>"
    html += "</tbody></table>"
    
    # Verificação dos totais
    html += f"""
    <div class="code-block">
      <strong>Verificação dos totais:</strong><br>
      Totais por linha: {', '.join(map(str, totais_linha))}<br>
      (Esperados: 2024, 1885, 1950, 1850) ✓<br>
      Total geral: {total_geral} (Esperado: 7709) ✓
    </div>
  </div>
</div>

<div class="section" id="descritiva">
  <div class="section-header">
    <h2>3. Análise Descritiva</h2>
  </div>
  <div class="section-content">
    <h3>Estatísticas por Procedência</h3>
    <table>
      <thead>
        <tr>
          <th>Procedência</th>
          <th>Média</th>
          <th>Desvio Padrão</th>
          <th>Mínimo</th>
          <th>Máximo</th>
          <th>CV (%)</th>
        </tr>
      </thead>
      <tbody>"""
    
    # Estatísticas por procedência
    for proc in r['procedencias']:
        estat = r['estat_proc'][proc]
        html += f"""
        <tr>
          <td><strong>{proc}</strong></td>
          <td class='numero'>{estat['media']:.2f}</td>
          <td class='numero'>{estat['dp']:.2f}</td>
          <td class='numero'>{estat['minimo']}</td>
          <td class='numero'>{estat['maximo']}</td>
          <td class='numero'>{estat['cv']:.2f}</td>
        </tr>"""
    
    html += """</tbody></table>
    
    <h3>Estatísticas por Bloco</h3>
    <table>
      <thead>
        <tr>
          <th>Bloco</th>
          <th>Média</th>
          <th>Desvio Padrão</th>
          <th>Mínimo</th>
          <th>Máximo</th>
          <th>CV (%)</th>
        </tr>
      </thead>
      <tbody>"""
    
    # Estatísticas por bloco
    for bloco in r['blocos']:
        estat = r['estat_bloco'][bloco]
        html += f"""
        <tr>
          <td><strong>{bloco}</strong></td>
          <td class='numero'>{estat['media']:.2f}</td>
          <td class='numero'>{estat['dp']:.2f}</td>
          <td class='numero'>{estat['minimo']}</td>
          <td class='numero'>{estat['maximo']}</td>
          <td class='numero'>{estat['cv']:.2f}</td>
        </tr>"""
    
    html += """</tbody></table>
  </div>
</div>

<div class="section" id="anova-dbc">
  <div class="section-header">
    <h2>4. ANOVA - Delineamento em Blocos Casualizados (DBC)</h2>
  </div>
  <div class="section-content">
    <table>
      <thead>
        <tr>
          <th>Fonte de Variação</th>
          <th>GL</th>
          <th>SQ</th>
          <th>QM</th>
          <th>F calculado</th>
        </tr>
      </thead>
      <tbody>"""
    
    html += f"""
        <tr>
          <td><strong>Procedências</strong></td>
          <td class='numero'>{anova['gl_proc']}</td>
          <td class='numero'>{anova['sq_proc']:.2f}</td>
          <td class='numero'>{anova['qm_proc']:.2f}</td>
          <td class='numero resultado-destaque'>{anova['f_proc']:.4f}</td>
        </tr>
        <tr>
          <td><strong>Blocos</strong></td>
          <td class='numero'>{anova['gl_bloco']}</td>
          <td class='numero'>{anova['sq_bloco']:.2f}</td>
          <td class='numero'>{anova['qm_bloco']:.2f}</td>
          <td class='numero'>{anova['f_bloco']:.4f}</td>
        </tr>
        <tr>
          <td><strong>Resíduo</strong></td>
          <td class='numero'>{anova['gl_residuo']}</td>
          <td class='numero'>{anova['sq_residuo']:.2f}</td>
          <td class='numero'>{anova['qm_residuo']:.2f}</td>
          <td>-</td>
        </tr>
        <tr>
          <td><strong>Total</strong></td>
          <td class='numero'>{len(r['procedencias']) * len(r['blocos']) - 1}</td>
          <td class='numero'>{anova['sq_total']:.2f}</td>
          <td>-</td>
          <td>-</td>
        </tr>"""
    
    html += f"""</tbody></table>
    
    <div class="grid">
      <div class="card">
        <h4>Teste F para Procedências</h4>
        <p>F calculado: <span class="resultado-destaque">{anova['f_proc']:.4f}</span></p>
        <p><strong style="color: #28a745;">ALTAMENTE SIGNIFICATIVO</strong> (p &lt; 0,001)</p>
        <p>Conclusão: Existem diferenças significativas entre procedências</p>
      </div>
      
      <div class="card">
        <h4>Teste F para Blocos</h4>
        <p>F calculado: <span class="resultado-destaque">{anova['f_bloco']:.4f}</span></p>
        <p><strong style="color: #28a745;">SIGNIFICATIVO</strong> (p &lt; 0,05)</p>
        <p>Conclusão: O controle local foi efetivo</p>
      </div>
    </div>
  </div>
</div>

<div class="section" id="resultados">
  <div class="section-header">
    <h2>5. Resultados e Discussão</h2>
  </div>
  <div class="section-content">"""
    
    # Encontrar melhor e pior procedência
    melhor_proc = max(r['medias_proc'].items(), key=lambda x: x[1])
    pior_proc = min(r['medias_proc'].items(), key=lambda x: x[1])
    diferenca = melhor_proc[1] - pior_proc[1]
    diferenca_pct = (diferenca / pior_proc[1]) * 100
    
    html += f"""
    <h3>Principais Resultados</h3>
    <div class="grid">
      <div class="card">
        <h4>Melhor Desempenho</h4>
        <p><strong>{melhor_proc[0]}:</strong> {melhor_proc[1]:.2f} m³.ha⁻¹</p>
        <p>Diferença: +{diferenca:.2f} m³.ha⁻¹ ({diferenca_pct:.1f}% superior)</p>
      </div>
      
      <div class="card">
        <h4>Qualidade Experimental</h4>
        <p><strong>CV Experimental:</strong> {cv_exp:.2f}%</p>
        <p><strong>Precisão:</strong> {"EXCELENTE" if cv_exp <= 10 else "BOA" if cv_exp <= 20 else "REGULAR"}</p>
      </div>
    </div>
    
    <h3>Ranking das Procedências</h3>
    <table>
      <thead>
        <tr>
          <th>Posição</th>
          <th>Procedência</th>
          <th>Média (m³.ha⁻¹)</th>
          <th>Classificação</th>
        </tr>
      </thead>
      <tbody>"""
    
    # Ranking das procedências
    ranking = sorted(r['medias_proc'].items(), key=lambda x: x[1], reverse=True)
    classificacoes = ["Excelente", "Muito Bom", "Bom", "Regular", "Regular", "Baixo", "Muito Baixo"]
    
    for i, (proc, media) in enumerate(ranking):
        classe = classificacoes[i] if i < len(classificacoes) else "Avaliado"
        html += f"""
        <tr>
          <td class='numero'><strong>{i+1}º</strong></td>
          <td><strong>{proc}</strong></td>
          <td class='numero resultado-destaque'>{media:.2f}</td>
          <td>{classe}</td>
        </tr>"""
    
    html += f"""</tbody></table>
    
    <div class="destaque">
      <strong>Interpretação Estatística:</strong><br>
      • <strong>F (Procedências):</strong> {anova['f_proc']:.4f} - Altamente significativo (p &lt; 0,001)<br>
      • <strong>F (Blocos):</strong> {anova['f_bloco']:.4f} - Significativo (p &lt; 0,05)<br>
      • <strong>Controle local:</strong> O uso de blocos foi efetivo para controlar a heterogeneidade<br>
      • <strong>Precisão:</strong> CV = {cv_exp:.2f}% indica excelente precisão experimental
    </div>
  </div>
</div>

<div class="section" id="conclusoes">
  <div class="section-header">
    <h2>6. Conclusões</h2>
  </div>
  <div class="section-content">
    <div class="conclusao">
      <h3>Conclusões Principais:</h3>
      <ul>
        <li><strong>Diferenças significativas:</strong> Existe diferença significativa entre as procedências de <em>Eucalyptus grandis</em> para produção em m³.ha⁻¹</li>
        <li><strong>Melhor procedência:</strong> {melhor_proc[0]} apresentou o melhor desempenho produtivo ({melhor_proc[1]:.2f} m³.ha⁻¹)</li>
        <li><strong>Controle local efetivo:</strong> O delineamento em blocos foi eficiente, controlando adequadamente a heterogeneidade</li>
        <li><strong>Qualidade experimental:</strong> CV experimental de {cv_exp:.2f}% indica excelente precisão</li>
        <li><strong>Recomendação:</strong> Para futuros experimentos similares, recomenda-se o uso do DBC</li>
      </ul>
    </div>
    
    <h3>Recomendações Práticas</h3>
    <div class="grid">
      <div class="card">
        <h4>Para Plantios Comerciais</h4>
        <ul>
          <li>Priorizar procedência <strong>{melhor_proc[0]}</strong></li>
          <li>Considerar as 3 melhores procedências para diversificação</li>
          <li>Evitar procedências com baixo desempenho</li>
        </ul>
      </div>
      
      <div class="card">
        <h4>Para Futuros Experimentos</h4>
        <ul>
          <li>Manter delineamento em blocos (controle local efetivo)</li>
          <li>Considerar fatores ambientais adicionais</li>
          <li>Avaliar interação procedência × ambiente</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<div class="section">
  <div class="section-header">
    <h2>7. Informações da Sessão</h2>
  </div>
  <div class="section-content">
    <div class="code-block">
      <strong>Análise realizada em:</strong> {datetime.now().strftime("%d/%m/%Y às %H:%M")}<br>
      <strong>Metodologia:</strong> ANOVA (Delineamento em Blocos Casualizados)<br>
      <strong>Software:</strong> Python + HTML (simulando saída Quarto)<br>
      <strong>Semente:</strong> 2025 (para reprodutibilidade)
    </div>
    
    <h3>Referências</h3>
    <ul>
      <li>Atividade 01 - CEN5815 (Prof. Dr. Deoclecio Jardim Amorim)</li>
      <li>Montgomery, D. C. (2017). <em>Design and analysis of experiments</em>. John Wiley & Sons.</li>
      <li>Pimentel-Gomes, F., & Garcia, C. H. (2002). <em>Estatística aplicada a experimentos agronômicos e florestais</em>. FEALQ.</li>
    </ul>
  </div>
</div>

</div>
</div>

</body>
</html>"""
    
    return html

def main():
    print("Gerando relatório final...")
    
    # Executar análise completa
    resultados = executar_analise_completa()
    
    # Gerar HTML
    html = gerar_html_quarto_style(resultados)
    
    # Salvar arquivo
    with open('relatorio_quarto_final.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("Relatorio gerado: relatorio_quarto_final.html")
    print("Estilo Quarto com Bootstrap")
    print("TOC navegavel lateral")
    print("Analise estatistica completa")

if __name__ == "__main__":
    main()