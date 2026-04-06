SIDEBAR_HIDE_CSS = (
    "<style>"
    "[data-testid='stSidebar'],[data-testid='stSidebarCollapsedControl']"
    "{display:none !important}"
    "</style>"
)

SIDEBAR_LOGO = """
<div class="logo-area">
    <div class="logo-text">
        <span class="logo-pick">Pick</span><span class="logo-card">Card</span><span class="logo-u">U</span>
    </div>
    <div class="logo-version">v. 1.0.0</div>
</div>
"""

SPLASH = (
    '<div class="splash-overlay">'
    '  <div class="splash-logo-text">'
    '    <span class="splash-pick">Pick</span>'
    '    <span class="splash-card">Card</span>'
    '    <span class="splash-u">U</span>'
    '  </div>'
    '  <p class="splash-tagline">당신을 위한 개인 맞춤형 신용카드 큐레이션 시스템</p>'
    '</div>'
)

BOT_LOADING = (
    '<div class="msg-bot-row">'
    '<div class="avatar">🤖</div>'
    '<div class="msg-bot-bubble">⏳ 카드 혜택을 검색하고 있습니다...</div>'
    '</div>'
)


def profile_card(user_name: str, mbti_label: str) -> str:
    return (
        '<p class="mypage-section-header">PROFILE</p>'
        '<div class="mypage-profile-card">'
        '  <div class="mypage-avatar">🪪</div>'
        '  <div class="mypage-profile-info">'
        f'    <p class="mypage-info-line"><b>NAME</b> : {user_name}</p>'
        f'    <p class="mypage-info-line"><b>MBTI</b> : {mbti_label}</p>'
        '  </div>'
        '</div>'
    )


def card_tile(card_name: str) -> str:
    return (
        f'<div class="mypage-card-tile">'
        f'  <p class="tile-name">{card_name}</p>'
        f'</div>'
    )


def user_bubble(content: str) -> str:
    return (
        '<div class="msg-user-row">'
        f'<div class="msg-user-bubble">{content}</div>'
        '<div class="avatar">👤</div>'
        '</div>'
    )


def bot_bubble(content: str) -> str:
    return (
        '<div class="msg-bot-row">'
        '<div class="avatar">🤖</div>'
        f'<div class="msg-bot-bubble">{content}</div>'
        '</div>'
    )
