#!/usr/bin/env python3
"""
Análise Estatística da Atividade 01 - Python Puro
Análise ANOVA para experimento com Eucalyptus grandis
"""

import math
import statistics
from collections import defaultdict

def calcular_estatisticas_basicas(valores):
    """Calcula estatísticas básicas para uma lista de valores"""
    n = len(valores)
    media = statistics.mean(valores)
    desvio_padrao = statistics.stdev(valores) if n > 1 else 0
    minimo = min(valores)
    maximo = max(valores)
    cv = (desvio_padrao / media * 100) if media != 0 else 0
    
    return {
        'n': n,
        'media': media,
        'desvio_padrao': desvio_padrao,
        'minimo': minimo,
        'maximo': maximo,
        'cv_porcento': cv
    }

def calcular_anova_dbc(dados_long):
    """Calcula ANOVA para Delineamento em Blocos Casualizados"""
    # Extrair valores únicos
    procedencias = sorted(list(set(d['Procedencia'] for d in dados_long)))
    blocos = sorted(list(set(d['Bloco'] for d in dados_long)))
    
    # Criar matrizes para cálculos
    dados_por_proc = defaultdict(list)
    dados_por_bloco = defaultdict(list)
    todos_valores = []
    
    for dado in dados_long:
        dados_por_proc[dado['Procedencia']].append(dado['Producao'])
        dados_por_bloco[dado['Bloco']].append(dado['Producao'])
        todos_valores.append(dado['Producao'])
    
    # Médias
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
    gl_total = len(todos_valores) - 1
    
    # Quadrados médios
    qm_proc = sq_proc / gl_proc if gl_proc > 0 else 0
    qm_bloco = sq_bloco / gl_bloco if gl_bloco > 0 else 0
    qm_residuo = sq_residuo / gl_residuo if gl_residuo > 0 else 0
    
    # Estatísticas F
    f_proc = qm_proc / qm_residuo if qm_residuo > 0 else 0
    f_bloco = qm_bloco / qm_residuo if qm_residuo > 0 else 0
    
    return {
        'sq_proc': sq_proc, 'gl_proc': gl_proc, 'qm_proc': qm_proc, 'f_proc': f_proc,
        'sq_bloco': sq_bloco, 'gl_bloco': gl_bloco, 'qm_bloco': qm_bloco, 'f_bloco': f_bloco,
        'sq_residuo': sq_residuo, 'gl_residuo': gl_residuo, 'qm_residuo': qm_residuo,
        'sq_total': sq_total, 'gl_total': gl_total,
        'medias_proc': medias_proc, 'medias_bloco': medias_bloco, 'media_geral': media_geral
    }

def gerar_relatorio_html(dados_matriz, dados_long, resultados_anova):
    """Gera relatório HTML completo"""
    
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Análise de Produção de Eucalyptus grandis - Atividade 01</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f8f9fa;
        }}
        
        .header {{
            text-align: center;
            background: linear-gradient(135deg, #2c3e50, #3498db);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
            font-weight: 300;
        }}
        
        .header p {{
            margin: 10px 0 0 0;
            font-size: 1.1em;
            opacity: 0.9;
        }}
        
        .section {{
            background: white;
            margin: 20px 0;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        .section h2 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-top: 0;
        }}
        
        .section h3 {{
            color: #34495e;
            margin-top: 25px;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
            font-size: 0.9em;
        }}
        
        table th, table td {{
            padding: 12px;
            text-align: center;
            border: 1px solid #ddd;
        }}
        
        table th {{
            background-color: #3498db;
            color: white;
            font-weight: 600;
        }}
        
        table tr:nth-child(even) {{
            background-color: #f8f9fa;
        }}
        
        table tr:hover {{
            background-color: #e8f4f8;
        }}
        
        .numero {{
            font-family: 'Courier New', monospace;
            font-weight: bold;
        }}
        
        .destaque {{
            background-color: #fff3cd;
            border: 1px solid #ffeaa7;
            padding: 15px;
            border-radius: 5px;
            margin: 15px 0;
        }}
        
        .conclusao {{
            background-color: #d1ecf1;
            border: 1px solid #74c0fc;
            padding: 15px;
            border-radius: 5px;
            margin: 15px 0;
        }}
        
        .grid-2 {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin: 20px 0;
        }}
        
        .card {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #3498db;
        }}
        
        .estatistica {{
            text-align: center;
            font-size: 1.1em;
        }}
        
        .valor-destaque {{
            color: #e74c3c;
            font-weight: bold;
            font-size: 1.2em;
        }}
    </style>
</head>
<body>

<div class="header">
    <h1>Análise de Produção de Eucalyptus grandis</h1>
    <p>Atividade 01 - Análise de Variância (ANOVA)</p>
    <p>CEN5815 - Análise de Dados Agronômicos e Ambientais</p>
</div>

<div class="section">
    <h2>1. Introdução</h2>
    <p>Este relatório apresenta a análise estatística de um experimento com <strong>4 blocos casualizados</strong> 
    e <strong>7 procedências</strong> de <em>Eucalyptus grandis</em>, avaliando a produção em m³.ha⁻¹.</p>
    
    <p><strong>Objetivos:</strong></p>
    <ul>
        <li>Realizar análise descritiva dos dados experimentais</li>
        <li>Executar ANOVA como Delineamento Inteiramente Casualizado (DIC)</li>
        <li>Executar ANOVA como Delineamento em Blocos Casualizados (DBC)</li>
        <li>Comparar a eficácia dos dois delineamentos</li>
    </ul>
</div>

<div class="section">
    <h2>2. Dados Experimentais</h2>
    <h3>2.1 Matriz Original dos Dados</h3>
    <table>
        <thead>
            <tr>
                <th>Bloco / Procedência</th>"""
    
    # Cabeçalho da tabela com procedências
    procedencias = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']
    for proc in procedencias:
        html += f"<th>{proc}</th>"
    html += "<th><strong>Total</strong></th></tr></thead><tbody>"
    
    # Dados da matriz
    blocos = ['Bloco I', 'Bloco II', 'Bloco III', 'Bloco IV']
    totais_linha = []
    for i, bloco in enumerate(blocos):
        html += f"<tr><td><strong>{bloco}</strong></td>"
        total_linha = 0
        for j in range(len(procedencias)):
            valor = dados_matriz[i][j]
            html += f"<td class='numero'>{valor}</td>"
            total_linha += valor
        totais_linha.append(total_linha)
        html += f"<td class='numero valor-destaque'>{total_linha}</td></tr>"
    
    # Totais por coluna
    html += "<tr><td><strong>Total</strong></td>"
    totais_coluna = []
    total_geral = 0
    for j in range(len(procedencias)):
        total_col = sum(dados_matriz[i][j] for i in range(len(blocos)))
        totais_coluna.append(total_col)
        total_geral += total_col
        html += f"<td class='numero valor-destaque'>{total_col}</td>"
    html += f"<td class='numero valor-destaque'><strong>{total_geral}</strong></td></tr>"
    html += "</tbody></table>"
    
    html += f"""
    <div class="destaque">
        <strong>Características do Experimento:</strong><br>
        • <strong>Delineamento:</strong> Blocos casualizados<br>
        • <strong>Tratamentos:</strong> 7 procedências (P1 a P7)<br>
        • <strong>Repetições:</strong> 4 blocos<br>
        • <strong>Total de parcelas:</strong> 28<br>
        • <strong>Variável resposta:</strong> Produção em m³.ha⁻¹
    </div>
</div>

<div class="section">
    <h2>3. Análise Descritiva</h2>
    
    <h3>3.1 Estatísticas por Procedência</h3>
    <table>
        <thead>
            <tr>
                <th>Procedência</th>
                <th>n</th>
                <th>Média</th>
                <th>Desvio Padrão</th>
                <th>Mínimo</th>
                <th>Máximo</th>
                <th>CV (%)</th>
            </tr>
        </thead>
        <tbody>"""
    
    # Calcular estatísticas por procedência
    dados_por_proc = defaultdict(list)
    for dado in dados_long:
        dados_por_proc[dado['Procedencia']].append(dado['Producao'])
    
    for proc in sorted(dados_por_proc.keys()):
        estats = calcular_estatisticas_basicas(dados_por_proc[proc])
        html += f"""
            <tr>
                <td><strong>{proc}</strong></td>
                <td class='numero'>{estats['n']}</td>
                <td class='numero'>{estats['media']:.2f}</td>
                <td class='numero'>{estats['desvio_padrao']:.2f}</td>
                <td class='numero'>{estats['minimo']:.0f}</td>
                <td class='numero'>{estats['maximo']:.0f}</td>
                <td class='numero'>{estats['cv_porcento']:.2f}</td>
            </tr>"""
    
    html += """</tbody></table>
    
    <h3>3.2 Estatísticas por Bloco</h3>
    <table>
        <thead>
            <tr>
                <th>Bloco</th>
                <th>n</th>
                <th>Média</th>
                <th>Desvio Padrão</th>
                <th>Mínimo</th>
                <th>Máximo</th>
                <th>CV (%)</th>
            </tr>
        </thead>
        <tbody>"""
    
    # Calcular estatísticas por bloco
    dados_por_bloco = defaultdict(list)
    for dado in dados_long:
        dados_por_bloco[dado['Bloco']].append(dado['Producao'])
    
    for bloco in sorted(dados_por_bloco.keys()):
        estats = calcular_estatisticas_basicas(dados_por_bloco[bloco])
        html += f"""
            <tr>
                <td><strong>{bloco}</strong></td>
                <td class='numero'>{estats['n']}</td>
                <td class='numero'>{estats['media']:.2f}</td>
                <td class='numero'>{estats['desvio_padrao']:.2f}</td>
                <td class='numero'>{estats['minimo']:.0f}</td>
                <td class='numero'>{estats['maximo']:.0f}</td>
                <td class='numero'>{estats['cv_porcento']:.2f}</td>
            </tr>"""
    
    html += """</tbody></table>
</div>

<div class="section">
    <h2>4. Análise de Variância (ANOVA)</h2>
    
    <h3>4.1 Delineamento em Blocos Casualizados (DBC)</h3>
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
    
    anova = resultados_anova
    
    html += f"""
            <tr>
                <td><strong>Procedências</strong></td>
                <td class='numero'>{anova['gl_proc']}</td>
                <td class='numero'>{anova['sq_proc']:.2f}</td>
                <td class='numero'>{anova['qm_proc']:.2f}</td>
                <td class='numero valor-destaque'>{anova['f_proc']:.4f}</td>
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
                <td class='numero'>{anova['gl_total']}</td>
                <td class='numero'>{anova['sq_total']:.2f}</td>
                <td>-</td>
                <td>-</td>
            </tr>"""
    
    html += """</tbody></table>
    
    <div class="grid-2">
        <div class="card">
            <h4>Teste F para Procedências</h4>
            <div class="estatistica">
                <p>F calculado: <span class="valor-destaque">"""
    
    html += f"{anova['f_proc']:.4f}</span></p>"
    
    # Interpretação do F
    f_critico_aprox = 2.85  # Aproximado para α=0.05, gl1=6, gl2=18
    if anova['f_proc'] > f_critico_aprox:
        html += f"<p><strong style='color: #27ae60;'>Significativo</strong> (F > {f_critico_aprox})</p>"
        conclusao_proc = "Existem diferenças significativas entre as procedências"
    else:
        html += f"<p><strong style='color: #e74c3c;'>Não significativo</strong> (F ≤ {f_critico_aprox})</p>"
        conclusao_proc = "Não há diferenças significativas entre as procedências"
    
    html += """</div>
        </div>
        
        <div class="card">
            <h4>Teste F para Blocos</h4>
            <div class="estatistica">
                <p>F calculado: <span class="valor-destaque">"""
    
    html += f"{anova['f_bloco']:.4f}</span></p>"
    
    # Interpretação do F para blocos
    f_critico_bloco_aprox = 3.16  # Aproximado para α=0.05, gl1=3, gl2=18
    if anova['f_bloco'] > f_critico_bloco_aprox:
        html += f"<p><strong style='color: #27ae60;'>Significativo</strong> (F > {f_critico_bloco_aprox})</p>"
        conclusao_bloco = "O efeito de blocos é significativo"
    else:
        html += f"<p><strong style='color: #e74c3c;'>Não significativo</strong> (F ≤ {f_critico_bloco_aprox})</p>"
        conclusao_bloco = "O efeito de blocos não é significativo"
    
    html += """</div>
        </div>
    </div>
</div>

<div class="section">
    <h2>5. Ranking das Procedências</h2>
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
    medias_ordenadas = sorted(anova['medias_proc'].items(), key=lambda x: x[1], reverse=True)
    classificacoes = ['🥇 Excelente', '🥈 Muito Bom', '🥉 Bom', '👍 Regular', '👌 Regular', '⚠️ Baixo', '❌ Muito Baixo']
    
    for i, (proc, media) in enumerate(medias_ordenadas):
        classe = classificacoes[i] if i < len(classificacoes) else '📊 Avaliado'
        html += f"""
            <tr>
                <td class='numero'><strong>{i+1}º</strong></td>
                <td><strong>{proc}</strong></td>
                <td class='numero valor-destaque'>{media:.2f}</td>
                <td>{classe}</td>
            </tr>"""
    
    html += """</tbody></table>
</div>

<div class="section">
    <h2>6. Resultados e Discussão</h2>
    
    <div class="conclusao">
        <h3>Principais Conclusões:</h3>
        <ul>"""
    
    html += f"<li><strong>Procedências:</strong> {conclusao_proc}</li>"
    html += f"<li><strong>Blocos:</strong> {conclusao_bloco}</li>"
    
    melhor_proc = medias_ordenadas[0]
    pior_proc = medias_ordenadas[-1]
    diferenca = melhor_proc[1] - pior_proc[1]
    
    html += f"""
            <li><strong>Melhor procedência:</strong> {melhor_proc[0]} ({melhor_proc[1]:.2f} m³.ha⁻¹)</li>
            <li><strong>Menor produção:</strong> {pior_proc[0]} ({pior_proc[1]:.2f} m³.ha⁻¹)</li>
            <li><strong>Diferença máxima:</strong> {diferenca:.2f} m³.ha⁻¹ ({(diferenca/pior_proc[1]*100):.1f}% superior)</li>
        </ul>
    </div>
    
    <h3>6.1 Interpretação Estatística</h3>
    <p><strong>Coeficiente de Variação Experimental:</strong> 
    {(math.sqrt(anova['qm_residuo'])/anova['media_geral']*100):.2f}%</p>
    
    <div class="destaque">
        <strong>Qualidade do Experimento:</strong><br>"""
    
    cv_exp = math.sqrt(anova['qm_residuo'])/anova['media_geral']*100
    if cv_exp <= 10:
        html += "• <strong style='color: #27ae60;'>Excelente precisão experimental</strong> (CV ≤ 10%)"
    elif cv_exp <= 20:
        html += "• <strong style='color: #f39c12;'>Boa precisão experimental</strong> (10% < CV ≤ 20%)"
    else:
        html += "• <strong style='color: #e74c3c;'>Precisão experimental regular</strong> (CV > 20%)"
    
    html += f"""
    </div>
    
    <h3>6.2 Recomendações Práticas</h3>
    <div class="grid-2">
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
            <ul>"""
    
    if anova['f_bloco'] > f_critico_bloco_aprox:
        html += "<li>Manter delineamento em blocos (controle local efetivo)</li>"
    else:
        html += "<li>Avaliar necessidade de bloqueiamento</li>"
    
    html += f"""
                <li>Considerar fatores ambientais adicionais</li>
                <li>Avaliar interação procedência × ambiente</li>
            </ul>
        </div>
    </div>
</div>

<div class="section">
    <h2>7. Informações Técnicas</h2>
    <div class="grid-2">
        <div class="card">
            <h4>Metodologia</h4>
            <ul>
                <li><strong>Análise:</strong> ANOVA (Delineamento em Blocos Casualizados)</li>
                <li><strong>Software:</strong> Python (cálculos estatísticos puros)</li>
                <li><strong>Critério de significância:</strong> α = 0.05</li>
                <li><strong>Modelo:</strong> Y<sub>ij</sub> = μ + B<sub>i</sub> + P<sub>j</sub> + ε<sub>ij</sub></li>
            </ul>
        </div>
        
        <div class="card">
            <h4>Dados do Experimento</h4>
            <ul>
                <li><strong>Variável resposta:</strong> Produção (m³.ha⁻¹)</li>
                <li><strong>Média geral:</strong> {anova['media_geral']:.2f} m³.ha⁻¹</li>
                <li><strong>Erro experimental:</strong> {math.sqrt(anova['qm_residuo']):.2f} m³.ha⁻¹</li>
                <li><strong>Precisão:</strong> CV = {cv_exp:.2f}%</li>
            </ul>
        </div>
    </div>
</div>

<div class="header" style="margin-top: 30px;">
    <h2>Relatório Gerado Automaticamente</h2>
    <p>Análise estatística completa usando Python puro e HTML limpo</p>
    <p style="font-size: 0.9em; opacity: 0.8;">
        CEN5815 - Análise de Dados Agronômicos e Ambientais (2025)
    </p>
</div>

</body>
</html>"""
    
    return html

def main():
    """Função principal da análise"""
    print("Iniciando análise estatística...")
    
    # Dados originais do experimento
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
    
    # Calcular ANOVA
    resultados_anova = calcular_anova_dbc(dados_long)
    
    # Gerar relatório HTML
    html_relatorio = gerar_relatorio_html(dados_matriz, dados_long, resultados_anova)
    
    # Salvar arquivo HTML
    with open('relatorio_final.html', 'w', encoding='utf-8') as f:
        f.write(html_relatorio)
    
    print("Analise concluida!")
    print("Relatorio HTML gerado: relatorio_final.html")
    
    # Resumo no console
    print("\n" + "="*60)
    print("RESUMO DA ANALISE")
    print("="*60)
    print(f"F (Procedencias): {resultados_anova['f_proc']:.4f}")
    print(f"F (Blocos): {resultados_anova['f_bloco']:.4f}")
    print(f"QM Residuo: {resultados_anova['qm_residuo']:.2f}")
    print(f"CV Experimental: {(math.sqrt(resultados_anova['qm_residuo'])/resultados_anova['media_geral']*100):.2f}%")
    
    # Ranking das procedencias
    ranking = sorted(resultados_anova['medias_proc'].items(), key=lambda x: x[1], reverse=True)
    print(f"\nRanking das Procedencias:")
    for i, (proc, media) in enumerate(ranking, 1):
        print(f"{i}o {proc}: {media:.2f} m3.ha-1")

if __name__ == "__main__":
    main()