import streamlit as st
from pygments import highlight
from pygments.lexers import get_lexer_by_name, get_all_lexers
from pygments.formatters.html import HtmlFormatter
from pygments.formatters import get_formatter_by_name
from pygments.styles import get_all_styles

# タイトル
st.title("🔍 Pygments ハイライトツール")

# 入力欄
code_input = st.text_area("💬 ハイライトしたいコードを入力してください：", height=200)

# 言語指定
all_lexers = sorted(get_all_lexers(), key=lambda x: x[0].lower())
lang_names = [lexer[1][0] for lexer in all_lexers if lexer[1]]
lang = st.selectbox("🗂 言語を選択：", lang_names, index=lang_names.index("python") if "python" in lang_names else 0)

# スタイル指定
style = st.selectbox("🎨 ハイライトスタイルを選択：", list(get_all_styles()))

if code_input:
    # Lexerとフォーマッタの取得
    lexer = get_lexer_by_name(lang)
    html_formatter = HtmlFormatter(style=style, noclasses=False)
    bbcode_formatter = get_formatter_by_name("bbcode")

    # スタイル用CSS生成
    style_defs = html_formatter.get_style_defs('.highlight')

    # HTML形式でハイライト（改行・空白保持）
    highlighted_html = f"""
    <style>{style_defs}</style>
    <div class="highlight">{highlight(code_input, lexer, html_formatter)}</div>
    """

    # BBCode形式でハイライト出力
    highlighted_bbcode = highlight(code_input, lexer, bbcode_formatter)

    st.subheader("🖥 プレビュー：")
    st.markdown(highlighted_html, unsafe_allow_html=True)

    st.subheader("📦 BBCode：")
    st.code(highlighted_bbcode, language="text")

    st.caption("※ BBCodeはフォーラムなどで使用できるプレーンテキスト形式です。")
