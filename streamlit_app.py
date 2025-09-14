import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd

st.set_page_config(page_title="情報モラル", page_icon="📱", layout="wide")

st.title("情報モラル（pp.217-219）")
st.caption("Created by Dit-Lab.(Daiki ITO)")
st.caption("Supported by Tomoaki ATSUMI")

if 'current_step' not in st.session_state:
    st.session_state.current_step = 1

if 'scores' not in st.session_state:
    st.session_state.scores = {
        'scene1': 0,
        'scene2': 0,
        'scene3': 0,
        'total': 0
    }

if 'progress' not in st.session_state:
    st.session_state.progress = 0

progress_bar = st.progress(st.session_state.progress)

def update_progress():
    st.session_state.progress = st.session_state.current_step / 5
    progress_bar.progress(st.session_state.progress)

def next_step():
    if st.session_state.current_step < 5:
        st.session_state.current_step += 1
        update_progress()

def prev_step():
    if st.session_state.current_step > 1:
        st.session_state.current_step -= 1
        update_progress()

def reset_app():
    st.session_state.current_step = 1
    st.session_state.scores = {'scene1': 0, 'scene2': 0, 'scene3': 0, 'total': 0}
    st.session_state.progress = 0

# Navigation buttons
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("← 前へ") and st.session_state.current_step > 1:
        prev_step()
        st.rerun()

with col3:
    if st.button("次へ →") and st.session_state.current_step < 5:
        next_step()
        st.rerun()

# Step 1: はじめに
if st.session_state.current_step == 1:
    st.header("🌟 SNSシミュレーターへようこそ！")
    st.subheader("きみは「デキる」デジタル市民になれるか？")
    
    st.markdown("""
    ### 📱 架空のSNS「TomoNet」へようこそ！
    
    このシミュレーターでは、SNSでよくある場面に次々と遭遇します。
    あなたの判断と行動で、ネット社会を気持ちよく、そして安全に生き抜くスキルを身につけましょう！
    """)
    
    # SNS風の体験プレビュー
    st.info("💡 これから3つのシーンを体験していきます。各シーンであなたの判断力が試されます！")
    
    # プレビューカード
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="border: 3px solid #ff6b6b; border-radius: 10px; padding: 20px; background-color: white; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
        <h4 style="color: #d63031; margin-bottom: 10px;">🔥 Scene 1</h4>
        <p style="color: #2d3436; font-weight: bold; margin-bottom: 8px;">感情的なコメント</p>
        <p style="color: #636e72; font-size: 14px; line-height: 1.4;">友達への辛辣なコメントを見つけた時、どうする？</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="border: 3px solid #4ecdc4; border-radius: 10px; padding: 20px; background-color: white; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
        <h4 style="color: #00b894; margin-bottom: 10px;">📰 Scene 2</h4>
        <p style="color: #2d3436; font-weight: bold; margin-bottom: 8px;">うわさ情報</p>
        <p style="color: #636e72; font-size: 14px; line-height: 1.4;">衝撃的なニュースが拡散されている。信じる？</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="border: 3px solid #45b7d1; border-radius: 10px; padding: 20px; background-color: white; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
        <h4 style="color: #0984e3; margin-bottom: 10px;">🖼️ Scene 3</h4>
        <p style="color: #2d3436; font-weight: bold; margin-bottom: 8px;">著作権・肖像権</p>
        <p style="color: #636e72; font-size: 14px; line-height: 1.4;">プロフィール画像、どれを選ぶのが正解？</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    if st.button("🚀 シミュレーションを開始する！", type="primary"):
        next_step()
        st.rerun()

# Step 2: シーン1
elif st.session_state.current_step == 2:
    st.header("🔥 Case 1：友達の投稿と、トゲのあるコメント")
    
    # SNS投稿風のボックス
    st.markdown("""
    <div style="border: 2px solid #ddd; border-radius: 10px; padding: 20px; background-color: white; margin: 20px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
    <div style="display: flex; align-items: center; margin-bottom: 15px;">
        <div style="width: 40px; height: 40px; background-color: #4CAF50; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; margin-right: 15px;">A</div>
        <strong style="color: #2d3436; font-size: 16px;">友達Aさん</strong>
    </div>
    <p style="font-size: 16px; line-height: 1.5; color: #2d3436; margin-bottom: 20px;">新発売のゲーム、操作が難しすぎて全然楽しめない…😞</p>
    <div style="border-top: 2px solid #eee; padding-top: 15px; margin-top: 15px;">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <div style="width: 30px; height: 30px; background-color: #f44336; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; margin-right: 15px;">X</div>
            <strong style="color: #2d3436; font-size: 14px;">知らない人</strong>
        </div>
        <p style="color: #636e72; font-size: 14px; line-height: 1.4;">え、そんなのもクリアできないの？才能ないんじゃない？笑</p>
    </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🤔 あなたなら、この知らない人にどう反応する？")
    
    choice1 = st.radio(
        "選択肢を選んでください：",
        [
            "①「友達に失礼だろ！そっちこそ才能ないんじゃない？」と反論する。",
            "② 反応せず無視する。または、友達を「大丈夫？」と気遣う。",
            "③「確かに難しいですよね〜」と、知らない人に同調するフリをしてみる。"
        ],
        key="scene1_choice"
    )
    
    if st.button("回答を確認する", key="scene1_submit"):
        if choice1 == "② 反応せず無視する。または、友達を「大丈夫？」と気遣う。":
            st.session_state.scores['scene1'] = 100
            st.success("🎉 **正解です！**")
            st.markdown("""
            **解説：**  
            ネットの向こう側にいるのも、感情を持った人間です。売り言葉に買い言葉で返すと、ただの言い争い（炎上）に発展してしまいます。
            
            **重要なポイント：**
            - 相手の気持ちを想像し、冷静に対応することが責任ある態度
            - 友達をサポートすることが大切
            - 感情的な反応は状況を悪化させるだけ
            """)
        else:
            st.session_state.scores['scene1'] = 30
            st.warning("💭 **もう一度考えてみましょう**")
            st.markdown("""
            **正解は②です。**  
            ネットの向こう側にいるのも、感情を持った人間です。売り言葉に買い言葉で返すと、ただの言い争い（炎上）に発展してしまいます。
            相手の気持ちを想像し、冷静に対応することが、責任ある態度です。
            """)
        
        # スコア可視化
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = st.session_state.scores['scene1'],
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Scene 1 スコア"},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': "darkgreen"},
                'steps': [
                    {'range': [0, 50], 'color': "lightgray"},
                    {'range': [50, 100], 'color': "lightgreen"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90
                }
            }
        ))
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)

# Step 3: シーン2
elif st.session_state.current_step == 3:
    st.header("📰 Case 2：タイムラインに流れてきた、気になるウワサ")
    
    # バイラルな投稿風のボックス
    st.markdown("""
    <div style="border: 3px solid #ff4444; border-radius: 10px; padding: 25px; background-color: white; margin: 20px 0; box-shadow: 0 4px 12px rgba(255,68,68,0.2);">
    <div style="display: flex; align-items: center; margin-bottom: 20px;">
        <div style="width: 45px; height: 45px; background: linear-gradient(135deg, #ff6b6b, #ee5a5a); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; margin-right: 15px; font-size: 18px;">⚡</div>
        <strong style="color: #d63031; font-size: 18px;">Breaking News Today</strong>
    </div>
    <h3 style="color: #d63031; margin-bottom: 20px; font-size: 20px;">【超速報！】</h3>
    <p style="font-size: 16px; line-height: 1.6; font-weight: bold; color: #2d3436; margin-bottom: 20px;">人気ドリンク「クールサイダー」に、健康に害のある成分が含まれていることが判明！メーカーは隠蔽か？</p>
    <div style="margin-top: 15px; padding: 15px; background-color: #fff5f5; border-radius: 8px; border-left: 4px solid #ff6b6b;">
        <span style="color: #d63031; font-weight: bold; font-size: 16px;">#拡散希望</span>
    </div>
    <div style="margin-top: 20px; display: flex; gap: 30px;">
        <span style="color: #636e72; font-weight: bold;">❤️ いいね：5.2万件</span>
        <span style="color: #636e72; font-weight: bold;">🔄 リポスト：3.8万件</span>
    </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🤔 あなたならどうする？")
    
    choice2 = st.selectbox(
        "行動を選択してください：",
        [
            "選択してください",
            "大変だ！みんなに知らせなきゃ！急いでリポストする。",
            "本当かな？まずは情報の出どころを調べてみる。",
            "とりあえず「いいね」だけしておく。"
        ],
        key="scene2_choice"
    )
    
    if choice2 != "選択してください" and st.button("回答を確認する", key="scene2_submit"):
        if choice2 == "本当かな？まずは情報の出どころを調べてみる。":
            st.session_state.scores['scene2'] = 100
            st.success("🎉 **正解です！**")
            st.markdown("""
            **解説：**  
            「いいね」やリポストの数が多いからといって、その情報が正しいとは限りません。
            
            **メディアリテラシーのポイント：**
            - 衝撃的な情報ほど、まずは公式サイトや複数の大手ニュースサイトなど、信頼できる情報源で同じ内容が報じられているかを確認
            - これを「クロスチェック」と呼びます
            - 情報を正しく見極める力（メディアリテラシー）が重要
            """)
        else:
            st.session_state.scores['scene2'] = 20
            st.warning("💭 **もう一度考えてみましょう**")
            st.markdown("""
            **正解は「調べてみる」です。**  
            「いいね」やリポストの数が多いからといって、その情報が正しいとは限りません。
            衝撃的な情報ほど、まずは公式サイトや複数の大手ニュースサイトなど、信頼できる情報源で同じ内容が報じられているかを確認（クロスチェック）しましょう。
            これが情報を正しく見極める力（メディアリテラシー）です。
            """)
        
        # 情報確認のフローチャート
        fig = go.Figure()
        
        # フローチャートのノード
        fig.add_shape(
            type="rect", x0=0, y0=3, x1=2, y1=4,
            line=dict(color="#0984e3", width=3), fillcolor="white"
        )
        fig.add_annotation(x=1, y=3.5, text="<b>衝撃的な情報発見</b>", showarrow=False, 
                          font=dict(size=14, color="#2d3436"))
        
        fig.add_shape(
            type="rect", x0=0, y0=2, x1=2, y1=3,
            line=dict(color="#00b894", width=3), fillcolor="white"
        )
        fig.add_annotation(x=1, y=2.5, text="<b>情報源を確認</b>", showarrow=False, 
                          font=dict(size=14, color="#2d3436"))
        
        fig.add_shape(
            type="rect", x0=0, y0=1, x1=2, y1=2,
            line=dict(color="#fdcb6e", width=3), fillcolor="white"
        )
        fig.add_annotation(x=1, y=1.5, text="<b>複数のソースで<br>クロスチェック</b>", showarrow=False, 
                          font=dict(size=13, color="#2d3436"))
        
        fig.add_shape(
            type="rect", x0=0, y0=0, x1=2, y1=1,
            line=dict(color="#6c5ce7", width=3), fillcolor="white"
        )
        fig.add_annotation(x=1, y=0.5, text="<b>信頼できる場合のみ<br>シェア</b>", showarrow=False, 
                          font=dict(size=13, color="#2d3436"))
        
        # 矢印（より見やすく）
        fig.add_annotation(x=1, y=2.85, text="<b>↓</b>", showarrow=False, 
                          font=dict(size=24, color="#74b9ff"))
        fig.add_annotation(x=1, y=1.85, text="<b>↓</b>", showarrow=False, 
                          font=dict(size=24, color="#74b9ff"))
        fig.add_annotation(x=1, y=0.85, text="<b>↓</b>", showarrow=False, 
                          font=dict(size=24, color="#74b9ff"))
        
        fig.update_layout(
            title=dict(text="<b>情報確認のフローチャート</b>", font=dict(size=18, color="#2d3436")),
            xaxis=dict(range=[-0.5, 2.5], showgrid=False, showticklabels=False),
            yaxis=dict(range=[-0.5, 4.5], showgrid=False, showticklabels=False),
            height=400,
            plot_bgcolor='white',
            paper_bgcolor='white'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # スコア表示
        fig_score = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = st.session_state.scores['scene2'],
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Scene 2 スコア"},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, 50], 'color': "lightgray"},
                    {'range': [50, 100], 'color': "lightblue"}
                ],
            }
        ))
        fig_score.update_layout(height=300)
        st.plotly_chart(fig_score, use_container_width=True)

# Step 4: シーン3
elif st.session_state.current_step == 4:
    st.header("🖼️ Case 3：自分のプロフィール画像、どれにする？")
    
    st.markdown("### あなたのアカウントの「顔」となるプロフィール画像。法的に問題がないのはどちらでしょう？")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; border: 3px solid #ff6b6b; border-radius: 10px; padding: 25px; background-color: white; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #d63031; margin-bottom: 20px;">選択肢 A</h3>
        <div style="width: 150px; height: 150px; background: linear-gradient(45deg, #ff6b6b, #4ecdc4); border-radius: 50%; margin: 20px auto; display: flex; align-items: center; justify-content: center; color: white; font-size: 20px; font-weight: bold; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
        アニメ<br>キャラ
        </div>
        <p style="color: #2d3436; font-size: 16px;"><strong>大好きなアニメのキャラクター</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; border: 3px solid #0984e3; border-radius: 10px; padding: 25px; background-color: white; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #0984e3; margin-bottom: 20px;">選択肢 B</h3>
        <div style="width: 150px; height: 150px; background: linear-gradient(135deg, #667eea, #764ba2); border-radius: 50%; margin: 20px auto; display: flex; align-items: center; justify-content: center; color: white; font-size: 20px; font-weight: bold; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
        風景<br>写真
        </div>
        <p style="color: #2d3436; font-size: 16px;"><strong>自分で撮影した風景写真</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    choice3 = st.radio(
        "プロフィール画像として適切なのは？",
        ["A: 大好きなアニメのキャラクター", "B: 自分で撮影した風景写真"],
        key="scene3_choice"
    )
    
    if st.button("回答を確認する", key="scene3_submit"):
        if choice3 == "B: 自分で撮影した風景写真":
            st.session_state.scores['scene3'] = 100
            st.success("🎉 **正解です！**")
            st.markdown("""
            **解説：**  
            アニメのキャラクターには**著作権**が、有名人の写真には**肖像権**があります。
            
            **知的財産権のポイント：**
            - これらを作者や本人の許可なく利用すると、権利侵害にあたります
            - 自分で作成したものや、利用が許可されたフリー素材を使うのがルール
            - 「みんなやってるから大丈夫」は通用しません
            """)
        else:
            st.session_state.scores['scene3'] = 25
            st.warning("💭 **もう一度考えてみましょう**")
            st.markdown("""
            **正解はBです。**  
            アニメのキャラクターには著作権が、有名人の写真には肖像権があります。
            これらを作者や本人の許可なく利用すると、権利侵害にあたります。
            自分で作成したものや、利用が許可されたフリー素材を使うのがルールです。
            """)
        
        
        # スコア表示
        fig_score = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = st.session_state.scores['scene3'],
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Scene 3 スコア"},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': "darkred"},
                'steps': [
                    {'range': [0, 50], 'color': "lightgray"},
                    {'range': [50, 100], 'color': "lightcoral"}
                ],
            }
        ))
        fig_score.update_layout(height=300)
        st.plotly_chart(fig_score, use_container_width=True)

# Step 5: アルゴリズムの罠
elif st.session_state.current_step == 5:
    st.header("🧠 知っておこう - SNSにひそむアルゴリズムの罠")
    
    st.markdown("""
    ### あなたに見えている世界は、あなた専用に作られている
    
    SNSや動画サイトは、賢いプログラム（**アルゴリズム**）が、あなたの好みを学習して
    「あなたが見たいであろう情報」を優先的に表示します。
    
    これは便利ですが、時としてあなたの視野を狭めてしまう危険性もはらんでいます。
    """)
    
    tab1, tab2 = st.tabs(["🫧 フィルターバブル", "🔊 エコーチェンバー"])
    
    with tab1:
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # フィルターバブルの視覚化
            fig = go.Figure()
            
            # 外側の世界（多様な情報）
            theta = [i * 360 / 20 for i in range(20)]
            r = [3] * 20
            fig.add_trace(go.Scatterpolar(
                r=r,
                theta=theta,
                mode='markers',
                marker=dict(size=8, color=['red', 'blue', 'green', 'yellow', 'purple'] * 4),
                name='多様な情報',
                showlegend=True
            ))
            
            # バブル（フィルター）
            theta_bubble = [i for i in range(0, 361, 1)]
            r_bubble = [2] * len(theta_bubble)
            fig.add_trace(go.Scatterpolar(
                r=r_bubble,
                theta=theta_bubble,
                mode='lines',
                line=dict(color='rgba(255,0,0,0.5)', width=3),
                name='フィルターバブル',
                showlegend=True
            ))
            
            # 中心（あなた）
            fig.add_trace(go.Scatterpolar(
                r=[0],
                theta=[0],
                mode='markers',
                marker=dict(size=15, color='orange'),
                name='あなた',
                showlegend=True
            ))
            
            # 好みの情報のみ
            theta_filtered = [45, 90, 135, 180, 225]
            r_filtered = [1.5] * 5
            fig.add_trace(go.Scatterpolar(
                r=r_filtered,
                theta=theta_filtered,
                mode='markers',
                marker=dict(size=10, color='orange'),
                name='あなたの好みの情報',
                showlegend=True
            ))
            
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(visible=False, range=[0, 4]),
                    angularaxis=dict(visible=False)
                ),
                title="フィルターバブル現象"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("""
            ### 🫧 フィルターバブル とは
            
            **定義：**
            自分が見たい情報、心地よい情報にだけ囲まれてしまい、
            まるで「泡（バブル）」の中にいるように、異なる意見が見えなくなってしまう現象。
            
            **問題点：**
            - 世界観が偏る
            - 多様な価値観に触れる機会が減る
            - 判断力が低下する
            - 社会の分断が進む
            
            **実例：**
            - 政治的な投稿ばかり表示される
            - 同じ趣味の人の投稿ばかり見る
            - 反対意見を見る機会がなくなる
            """)
    
    with tab2:
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # エコーチェンバーの視覚化
            fig = go.Figure()
            
            # 部屋の壁
            fig.add_shape(
                type="rect",
                x0=0, y0=0, x1=4, y1=3,
                line=dict(color="brown", width=3),
                fillcolor="rgba(139,69,19,0.1)"
            )
            
            # 人（あなた）
            fig.add_trace(go.Scatter(
                x=[2], y=[1.5],
                mode='markers',
                marker=dict(size=20, color='blue'),
                name='あなた'
            ))
            
            # 声（意見）の波
            for i in range(3):
                fig.add_shape(
                    type="circle",
                    x0=2-0.3*(i+1), y0=1.5-0.3*(i+1), 
                    x1=2+0.3*(i+1), y1=1.5+0.3*(i+1),
                    line=dict(color=f"rgba(0,0,255,{0.5-i*0.1})", width=2),
                )
            
            # エコー（反響）
            echo_x = [0.5, 3.5, 0.5, 3.5, 2]
            echo_y = [0.5, 0.5, 2.5, 2.5, 1.5]
            fig.add_trace(go.Scatter(
                x=echo_x,
                y=echo_y,
                mode='markers',
                marker=dict(size=8, color='lightblue'),
                showlegend=False,
                name='エコー'
            ))
            
            fig.update_layout(
                xaxis=dict(range=[0, 4], showgrid=False, showticklabels=False),
                yaxis=dict(range=[0, 3], showgrid=False, showticklabels=False),
                title="エコーチェンバー現象",
                height=300
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("""
            ### 🔊 エコーチェンバー とは
            
            **定義：**
            閉じたコミュニティの中で、自分と同じ意見ばかりが返ってくる（エコーする）ため、
            その意見が「世の中の常識だ」と勘違いしてしまう現象。
            
            **問題点：**
            - 自分の意見が絶対正しいと思い込む
            - 批判的思考力が低下する
            - 異なる意見への理解が失われる
            - 極端な考えに走りやすくなる
            
            **実例：**
            - 同じ意見の人だけをフォロー
            - 反対意見は「間違い」だと決めつける
            - グループ内で意見が強化され続ける
            """)
    
    st.markdown("---")
    
    st.markdown("""
    ### 💡 対策：意識的に「泡」や「部屋」の外に出よう
    
    時には、興味のない分野のニュースを読んだり、自分とは違う意見を探したりして、
    意識的に多様な情報に触れることが大切です。
    """)
    
    # 対策のための行動チェックリスト
    st.markdown("### ✅ 多様性チェックリスト")
    
    checks = [
        "異なる政治的立場のニュースサイトを読む",
        "普段興味のない分野の記事をチェックする",
        "反対意見の人の投稿も見てみる",
        "海外のメディアも参照する",
        "オフラインでも情報収集する"
    ]
    
    checked_items = 0
    for i, check in enumerate(checks):
        if st.checkbox(check, key=f"check_{i}"):
            checked_items += 1
    
    if checked_items > 0:
        diversity_score = (checked_items / len(checks)) * 100
        
        fig = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = diversity_score,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "情報多様性スコア"},
            delta = {'reference': 60},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': "darkgreen"},
                'steps': [
                    {'range': [0, 40], 'color': "lightgray"},
                    {'range': [40, 80], 'color': "yellow"},
                    {'range': [80, 100], 'color': "lightgreen"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 60
                }
            }
        ))
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    # 総合スコア計算と表示
    st.markdown("---")
    st.header("🏆 あなたの総合情報モラルスコア")
    
    total_score = (st.session_state.scores['scene1'] + 
                   st.session_state.scores['scene2'] + 
                   st.session_state.scores['scene3']) / 3
    
    st.session_state.scores['total'] = total_score
    
    # 総合スコアの表示
    col1, col2 = st.columns([1, 1])
    
    with col1:
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = total_score,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "総合スコア"},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': "gold"},
                'steps': [
                    {'range': [0, 30], 'color': "red"},
                    {'range': [30, 60], 'color': "yellow"},
                    {'range': [60, 85], 'color': "lightgreen"},
                    {'range': [85, 100], 'color': "darkgreen"}
                ],
            }
        ))
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # 各シーンのスコア比較
        scores_df = pd.DataFrame({
            'シーン': ['感情的コメント', 'うわさ情報', 'プロフィール画像'],
            'スコア': [st.session_state.scores['scene1'], 
                     st.session_state.scores['scene2'], 
                     st.session_state.scores['scene3']]
        })
        
        fig = px.bar(scores_df, x='シーン', y='スコア', 
                    title="各シーンでのパフォーマンス",
                    color='スコア',
                    color_continuous_scale='Viridis')
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # 評価とメッセージ
    if total_score >= 85:
        st.success("🏆 **素晴らしい！あなたは優秀なデジタル市民です！**")
        st.balloons()
        st.markdown("情報モラルをしっかり理解し、責任ある行動ができています。この調子でネット社会をより良いものにしていきましょう！")
    elif total_score >= 60:
        st.info("👍 **良い判断力を持っています！**")
        st.markdown("基本的な情報モラルは身についています。さらに意識を高めて、より良いデジタル市民を目指しましょう！")
    else:
        st.warning("📚 **まだまだ学習の余地があります**")
        st.markdown("情報モラルについて、もう一度学び直してみましょう。正しい知識と判断力で、安全なネットライフを送りましょう！")
    
    # 学習した内容のまとめ
    st.markdown("""
    ### 🎓 今日学んだこと
    
    1. **感情的な反応は控えめに** - 冷静な対応が炎上を防ぐ
    2. **情報は必ず確認** - メディアリテラシーで偽情報を見抜く
    3. **権利を尊重する** - 著作権・肖像権を理解し遵守する
    4. **多様な視点を持つ** - フィルターバブルとエコーチェンバーに注意
    
    ### 🌟 これからも心がけること
    - 相手の気持ちを考える
    - 情報の出どころを確認する
    - 法的ルールを守る
    - 幅広い情報に触れる
    """)
    
    if st.button("🔄 もう一度挑戦する", type="secondary"):
        reset_app()
        st.rerun()

update_progress()
