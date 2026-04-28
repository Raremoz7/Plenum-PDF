import re

with open('CRM.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ─── CSS NOVO ────────────────────────────────────────────────
new_css = """
  /* === STAT CARDS === */
  #stats { padding: 60px 0 80px; background: var(--bg); }
  .stats-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    border: 1px solid var(--border);
    border-radius: 16px;
    overflow: hidden;
  }
  .stat-card {
    padding: 40px 28px;
    text-align: center;
    border-right: 1px solid var(--border);
    background: var(--card);
    position: relative;
  }
  .stat-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--purple-dk), var(--purple-mid));
  }
  .stat-card:last-child { border-right: none; }
  .stat-number {
    font-family: var(--font-head);
    font-size: 54px;
    font-weight: 800;
    letter-spacing: -0.04em;
    background: linear-gradient(135deg, var(--purple-mid), var(--purple-lt));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1;
    margin-bottom: 10px;
  }
  .stat-label { font-size: 13px; color: var(--mid); font-weight: 500; }

  /* === SUMARIO VISUAL === */
  #summary {
    padding: 80px 0;
    background: linear-gradient(180deg, transparent, rgba(124,63,228,0.04) 50%, transparent);
  }
  .summary-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 12px;
    margin-top: 40px;
  }
  .summary-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 28px 16px 24px;
    text-align: center;
  }
  .summary-icon {
    width: 52px; height: 52px;
    background: var(--purple-dim);
    border: 1px solid rgba(124,63,228,0.25);
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 14px;
  }
  .summary-icon svg { width: 26px; height: 26px; }
  .summary-num {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.14em;
    color: var(--purple);
    text-transform: uppercase;
    margin-bottom: 6px;
  }
  .summary-name {
    font-family: var(--font-head);
    font-size: 12px;
    font-weight: 700;
    color: var(--white);
    line-height: 1.35;
    margin-bottom: 12px;
  }
  .summary-mods {
    font-size: 11px;
    color: var(--purple-mid);
    font-weight: 600;
    background: var(--purple-dim);
    border-radius: 100px;
    padding: 3px 10px;
    display: inline-block;
  }

  /* === FUNIL COMERCIAL === */
  .funnel-wrap { margin: 60px 0 0; }
  .funnel-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--purple);
    margin-bottom: 28px;
    text-align: center;
  }
  .funnel-stages { display: flex; flex-direction: column; align-items: center; gap: 6px; }
  .funnel-stage {
    display: flex;
    align-items: center;
    border-radius: 10px;
    padding: 14px 24px;
    justify-content: space-between;
    gap: 16px;
  }
  .funnel-stage-left { display: flex; align-items: center; gap: 14px; }
  .funnel-dot { width: 10px; height: 10px; border-radius: 50%; background: var(--purple-mid); flex-shrink: 0; }
  .funnel-stage-name { font-family: var(--font-head); font-size: 14px; font-weight: 700; color: var(--white); }
  .funnel-stage-desc { font-size: 12px; color: var(--mid); }
  .funnel-badge {
    font-size: 11px; font-weight: 600; color: var(--purple-mid);
    background: var(--purple-dim); border-radius: 100px; padding: 3px 12px; white-space: nowrap;
  }

  /* === ICONES DE MODULO === */
  .module-icon {
    width: 42px; height: 42px;
    background: var(--purple-dim);
    border: 1px solid rgba(124,63,228,0.2);
    border-radius: 11px;
    display: flex; align-items: center; justify-content: center;
    margin-bottom: 14px;
  }
  .module-icon svg { width: 22px; height: 22px; }
"""

content = content.replace('</style>', new_css + '\n</style>')

# ─── SEÇÃO STAT CARDS ────────────────────────────────────────
stats_html = """
<!-- STAT CARDS -->
<section id="stats">
  <div class="container">
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-number">17</div>
        <div class="stat-label">Módulos integrados</div>
      </div>
      <div class="stat-card">
        <div class="stat-number">5</div>
        <div class="stat-label">Grupos funcionais</div>
      </div>
      <div class="stat-card">
        <div class="stat-number">360°</div>
        <div class="stat-label">Visão do cliente</div>
      </div>
      <div class="stat-card">
        <div class="stat-number">1</div>
        <div class="stat-label">Plataforma, todas as frentes</div>
      </div>
    </div>
  </div>
</section>

"""

# ─── SEÇÃO SUMÁRIO VISUAL ────────────────────────────────────
icon_users = '<svg viewBox="0 0 24 24" fill="none" stroke="#9a5ef5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>'
icon_calendar = '<svg viewBox="0 0 24 24" fill="none" stroke="#9a5ef5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>'
icon_bolt = '<svg viewBox="0 0 24 24" fill="none" stroke="#9a5ef5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>'
icon_chart = '<svg viewBox="0 0 24 24" fill="none" stroke="#9a5ef5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>'
icon_shield = '<svg viewBox="0 0 24 24" fill="none" stroke="#9a5ef5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'

summary_html = f"""
<!-- SUMARIO VISUAL -->
<section id="summary">
  <div class="container">
    <div class="reveal">
      <p class="section-label">Estrutura da plataforma</p>
      <h2 class="section-title">5 Grupos · 17 Módulos</h2>
      <p class="section-sub">Cada grupo cobre uma frente estratégica — do relacionamento à governança.</p>
    </div>
    <div class="summary-grid">
      <div class="summary-card">
        <div class="summary-icon">{icon_users}</div>
        <div class="summary-num">Grupo 01</div>
        <div class="summary-name">Relacionamento &amp; Comercial</div>
        <span class="summary-mods">3 módulos</span>
      </div>
      <div class="summary-card">
        <div class="summary-icon">{icon_calendar}</div>
        <div class="summary-num">Grupo 02</div>
        <div class="summary-name">Execução &amp; Rotina</div>
        <span class="summary-mods">3 módulos</span>
      </div>
      <div class="summary-card">
        <div class="summary-icon">{icon_bolt}</div>
        <div class="summary-num">Grupo 03</div>
        <div class="summary-name">Escala &amp; Automação</div>
        <span class="summary-mods">3 módulos</span>
      </div>
      <div class="summary-card">
        <div class="summary-icon">{icon_chart}</div>
        <div class="summary-num">Grupo 04</div>
        <div class="summary-name">Inteligência &amp; Resultado</div>
        <span class="summary-mods">4 módulos</span>
      </div>
      <div class="summary-card">
        <div class="summary-icon">{icon_shield}</div>
        <div class="summary-num">Grupo 05</div>
        <div class="summary-name">Governança &amp; Infraestrutura</div>
        <span class="summary-mods">4 módulos</span>
      </div>
    </div>
  </div>
</section>

"""

# Inserir stats e sumário antes do overview
marker = '<!-- ═══════════════════════════════════════════\n     VISÃO GERAL'
content = content.replace(marker, stats_html + summary_html + marker)

# ─── FUNIL (substitui journey-wrap) ──────────────────────────
funnel_html = """    <!-- Funil Comercial -->
    <div class="funnel-wrap reveal">
      <p class="funnel-label">Funil Comercial — Da Entrada ao Resultado</p>
      <div class="funnel-stages">
        <div class="funnel-stage" style="width:100%;background:rgba(124,63,228,0.18);">
          <div class="funnel-stage-left"><div class="funnel-dot"></div><div><div class="funnel-stage-name">Captação</div><div class="funnel-stage-desc">Formulários, canais digitais e indicações</div></div></div>
          <span class="funnel-badge">Entrada de leads</span>
        </div>
        <div class="funnel-stage" style="width:88%;background:rgba(124,63,228,0.15);">
          <div class="funnel-stage-left"><div class="funnel-dot"></div><div><div class="funnel-stage-name">Qualificação</div><div class="funnel-stage-desc">Pontuação, segmentação e distribuição automática</div></div></div>
          <span class="funnel-badge">Leads qualificados</span>
        </div>
        <div class="funnel-stage" style="width:74%;background:rgba(124,63,228,0.12);">
          <div class="funnel-stage-left"><div class="funnel-dot"></div><div><div class="funnel-stage-name">Negociação</div><div class="funnel-stage-desc">Funil visual, follow-ups e registro de interações</div></div></div>
          <span class="funnel-badge">Oportunidades ativas</span>
        </div>
        <div class="funnel-stage" style="width:60%;background:rgba(124,63,228,0.10);">
          <div class="funnel-stage-left"><div class="funnel-dot"></div><div><div class="funnel-stage-name">Proposta</div><div class="funnel-stage-desc">Apresentação, produtos e condições comerciais</div></div></div>
          <span class="funnel-badge">Em proposta</span>
        </div>
        <div class="funnel-stage" style="width:46%;background:rgba(124,63,228,0.14);border:1px solid rgba(124,63,228,0.3);">
          <div class="funnel-stage-left"><div class="funnel-dot" style="background:#b891f8;"></div><div><div class="funnel-stage-name">Fechamento</div><div class="funnel-stage-desc">Contrato, pagamento e onboarding</div></div></div>
          <span class="funnel-badge" style="background:rgba(124,63,228,0.3);color:#b891f8;">Conversão</span>
        </div>
      </div>
    </div>
"""

content = re.sub(
    r'    <!-- Journey -->.*?</div>\s*\n\s*</div>',
    funnel_html + '\n    </div>',
    content,
    flags=re.DOTALL
)

# ─── ICONES NOS MÓDULOS ──────────────────────────────────────
icons = {
    'Leads e Funil de Vendas': '<svg viewBox="0 0 24 24" fill="none" stroke="#9a5ef5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>',
    'Contatos e Empresas': '<svg viewBox="0 0 24 24" fill="none" stroke="#9a5ef5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
    'Comunicação Omnichannel': '<svg viewBox="0 0 24 24" fill="none" stroke="#9a5ef5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
    'Tarefas e Atividades': '<svg viewBox="0 0 24 24" fill="none" stroke="#9a5ef5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>',
    'Link de Agendamento': '<svg viewBox="0 0 24 24" fill="none" stroke="#9a5ef5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>',
    'Produtos': '<svg viewBox="0 0 24 24" fill="none" stroke="#9a5ef5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>',
    'Automações e Workflows': '<svg viewBox="0 0 24 24" fill="none" stroke="#9a5ef5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
    'Formulários de Captura': '<svg viewBox="0 0 24 24" fill="none" stroke="#9a5ef5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>',
    'IA e Assistentes': '<svg viewBox="0 0 24 24" fill="none" stroke="#9a5ef5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 1 1 7.072 0l-.548.547A3.374 3.374 0 0 0 14 18.469V19a2 2 0 1 1-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/></svg>',
    'Dashboard': '<svg viewBox="0 0 24 24" fill="none" stroke="#9a5ef5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>',
    'Marketing e Campanhas': '<svg viewBox="0 0 24 24" fill="none" stroke="#9a5ef5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>',
    'ROI e Performance': '<svg viewBox="0 0 24 24" fill="none" stroke="#9a5ef5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>',
    'Pagamentos': '<svg viewBox="0 0 24 24" fill="none" stroke="#9a5ef5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"/><line x1="1" y1="10" x2="23" y2="10"/></svg>',
    'Configurações': '<svg viewBox="0 0 24 24" fill="none" stroke="#9a5ef5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>',
    'Usuários e Permissões': '<svg viewBox="0 0 24 24" fill="none" stroke="#9a5ef5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    'Integrações': '<svg viewBox="0 0 24 24" fill="none" stroke="#9a5ef5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>',
    'Multiempresa': '<svg viewBox="0 0 24 24" fill="none" stroke="#9a5ef5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="9" height="14" rx="1"/><rect x="13" y="3" width="9" height="18" rx="1"/></svg>',
}

for title, svg in icons.items():
    icon_html = f'<div class="module-icon">{svg}</div>\n          '
    content = content.replace(
        f'<h3 class="module-card-title">{title}</h3>',
        f'{icon_html}<h3 class="module-card-title">{title}</h3>'
    )

with open('CRM.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")
