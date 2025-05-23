import streamlit as st
from pygments import highlight
from pygments.lexers import get_lexer_by_name, get_all_lexers
from pygments.formatters import HtmlFormatter
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
    formatter = HtmlFormatter(style=style, noclasses=True, wrapcode=True)
    highlighted_html = f"<pre>{highlight(code_input, lexer, formatter)}</pre>"

    # BBCode形式（タグ付き）で出力（簡易的にタグ置換）
    bbcode = f"[code={lang}]\n{code_input}\n[/code]"

    st.subheader("🖥 プレビュー：")
    st.markdown(highlighted_html, unsafe_allow_html=True)

    st.subheader("📦 BBCode：")
    st.code(bbcode, language="text")

    st.caption("※ BBCodeはフォーラムなどで使用できるプレーンテキスト形式です。")
