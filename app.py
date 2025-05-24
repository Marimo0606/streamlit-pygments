import streamlit as st
import streamlit.components.v1 as components
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
lang_names_set = {lexer[1][0] for lexer in all_lexers if lexer[1] and lexer[1][0] != "python"}
lang_names = ["python", "(自動判定)"] + sorted(lang_names_set - {"python"})
lang = st.selectbox("🗂 言語を選択：", lang_names, index=0)

# スタイル指定
style = st.selectbox("🎨 ハイライトスタイルを選択：", list(get_all_styles()))

if code_input:
    # Lexerとフォーマッタの取得
    from pygments.lexers import guess_lexer, ClassNotFound
    try:
        if lang == "(自動判定)":
            lexer = guess_lexer(code_input)
        else:
            lexer = get_lexer_by_name(lang)
    except ClassNotFound:
        lexer = get_lexer_by_name("text")
    html_formatter = HtmlFormatter(style=style, noclasses=True, nowrap=True)
    bbcode_formatter = get_formatter_by_name("bbcode", style=style)

    # HTML形式でハイライト（色 + インデント保持 + インラインスタイル）
    raw_html = highlight(code_input, lexer, html_formatter)
    highlighted_html = f"""
    <div style="background-color:#f5f5f5; padding: 1em; overflow-x:auto; white-space:pre-wrap; font-family:monospace; margin-bottom:0;">{raw_html}</div>
    """

    # BBCode形式でハイライト出力
    highlighted_bbcode = highlight(code_input, lexer, bbcode_formatter)

    st.subheader("🖥 プレビュー：")
    line_count = code_input.count('\n') + 1
    height_px = min(800, max(100, line_count * 24))
    components.html(highlighted_html, height=height_px, scrolling=True)

    st.subheader("📦 BBCode：")
    st.code(highlighted_bbcode, language="text")
