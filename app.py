
import streamlit as st
import joblib
import html

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Sentiment AI | Review Analyzer",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM DESIGN ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background: linear-gradient(135deg, #0b1020 0%, #15112d 55%, #101a32 100%);
    color: #f4f5ff;
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu, footer {
    visibility: hidden;
}

.hero {
    text-align: center;
    padding: 25px 15px 28px;
}

.ai-badge {
    display: inline-block;
    padding: 8px 15px;
    border: 1px solid #6355a8;
    border-radius: 30px;
    background: rgba(111, 82, 220, 0.15);
    color: #c8bcff;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
}

.hero h1 {
    font-size: clamp(36px, 5vw, 54px);
    font-weight: 800;
    letter-spacing: -2px;
    margin: 20px 0 10px;
    color: #ffffff;
}

.gradient-text {
    background: linear-gradient(90deg, #a99aff, #64d9ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    color: #a7aec9;
    font-size: 16px;
    line-height: 1.8;
    max-width: 680px;
    margin: auto;
}

.panel {
    background: rgba(25, 31, 57, 0.88);
    border: 1px solid #343b60;
    border-radius: 20px;
    padding: 25px;
    margin: 10px 0 18px;
}

.panel-title {
    font-size: 20px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 5px;
}

.panel-subtitle {
    color: #a7aec9;
    font-size: 13px;
    margin-bottom: 18px;
}

div[data-testid="stTextArea"] textarea {
    background: #11172b !important;
    color: #f5f6ff !important;
    border: 1px solid #41496f !important;
    border-radius: 13px !important;
    padding: 15px !important;
    font-size: 15px !important;
}

div[data-testid="stTextArea"] textarea:focus {
    border-color: #a394ff !important;
    box-shadow: 0 0 0 2px rgba(163, 148, 255, 0.12) !important;
}

.stButton > button {
    border-radius: 12px;
    min-height: 45px;
    font-weight: 700;
    border: 1px solid #4e4b86;
    background: #222344;
    color: white;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    border-color: #a394ff;
    color: #ffffff;
    background: #34305d;
}

div.stButton > button[kind="primary"] {
    background: linear-gradient(90deg, #7664e8, #596fe6);
    border: none;
    color: white;
}

div.stButton > button[kind="primary"]:hover {
    background: linear-gradient(90deg, #8a79f5, #6d82f5);
    box-shadow: 0 5px 20px rgba(113, 99, 232, 0.25);
}

.result-card {
    border-radius: 18px;
    padding: 24px;
    margin: 15px 0;
    background: #171d35;
    border: 1px solid #3b456b;
}

.result-label {
    color: #a7aec9;
    font-size: 12px;
    letter-spacing: 1.5px;
    font-weight: 700;
}

.result-value {
    font-size: 30px;
    font-weight: 800;
    margin: 12px 0 6px;
}

.result-description {
    color: #bdc4df;
    font-size: 14px;
}

.positive {
    color: #65e6b0;
}

.negative {
    color: #ff899d;
}

.info-card {
    background: rgba(25, 31, 57, 0.8);
    border: 1px solid #343b60;
    border-radius: 15px;
    padding: 18px;
    min-height: 110px;
}

.info-card h4 {
    margin: 0 0 8px;
    color: #ded9ff;
    font-size: 14px;
}

.info-card p {
    color: #a7aec9;
    font-size: 13px;
    line-height: 1.6;
    margin: 0;
}

.footer {
    text-align: center;
    padding: 25px 5px 5px;
    color: #7f89ac;
    font-size: 12px;
    line-height: 1.8;
}

hr {
    border-color: #303653;
}
</style>
""", unsafe_allow_html=True)


# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    return joblib.load("sentiment_model.joblib")


try:
    model = load_model()
except Exception as e:
    st.error("Unable to load the trained model. Check that sentiment_model.joblib is in the project folder.")
    st.stop()


# ---------------- SAMPLE REVIEWS ----------------
def choose_review(review):
    st.session_state.review_text = review


if "review_text" not in st.session_state:
    st.session_state.review_text = ""


# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
    <span class="ai-badge">✦ POWERED BY MACHINE LEARNING</span>
    <h1>Understand the <span class="gradient-text">Feeling.</span></h1>
    <p>
        Turn written reviews into meaningful insights.
        Discover whether a review expresses a positive or negative sentiment
        with your trained machine-learning model.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------- MAIN INPUT PANEL ----------------
left, right = st.columns([1.45, 1], gap="large")

with left:
    st.markdown("""
    <div class="panel">
        <div class="panel-title">✍️ Analyse a review</div>
        <div class="panel-subtitle">
            Enter a product or movie review to get started.
        </div>
    </div>
    """, unsafe_allow_html=True)

    review = st.text_area(
        "Your review",
        key="review_text",
        height=175,
        placeholder="For example: The quality is amazing and the product works perfectly...",
        label_visibility="collapsed"
    )

    st.caption(f"📝 Characters entered: {len(review)}")

    analyze = st.button(
        "✦  Analyse Sentiment",
        type="primary",
        use_container_width=True
    )

    st.markdown("**Try a sample review**")

    sample1, sample2 = st.columns(2)

    with sample1:
        st.button(
            "😊 Positive sample",
            use_container_width=True,
            on_click=choose_review,
            args=("The product is excellent, useful, and works perfectly!",)
        )

    with sample2:
        st.button(
            "☹️ Negative sample",
            use_container_width=True,
            on_click=choose_review,
            args=("The product is disappointing, poor quality, and not worth buying.",)
        )


with right:
    st.markdown("""
    <div class="panel">
        <div class="panel-title">⚡ How it works</div>
        <div class="panel-subtitle">
            A simple machine-learning workflow
        </div>
        <div class="info-card">
            <h4>01 · Input</h4>
            <p>Your written review is supplied to the trained model.</p>
        </div>
        <br>
        <div class="info-card">
            <h4>02 · Prediction</h4>
            <p>The model analyses text patterns learned from labelled reviews.</p>
        </div>
        <br>
        <div class="info-card">
            <h4>03 · Result</h4>
            <p>The app displays the predicted sentiment and, when supported, the model's confidence.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ---------------- PREDICTION ----------------
if analyze:
    if not review.strip():
        st.warning("Please enter a review before analysing it.")
    else:
        try:
            prediction = model.predict([review])[0]
            sentiment = str(prediction).strip().lower()

            if sentiment == "positive":
                emoji = "😊"
                result_class = "positive"
                result_title = "Positive Sentiment"
                description = "The model classified this review as positive."
            elif sentiment == "negative":
                emoji = "☹️"
                result_class = "negative"
                result_title = "Negative Sentiment"
                description = "The model classified this review as negative."
            else:
                emoji = "🔎"
                result_class = ""
                result_title = html.escape(str(prediction).title())
                description = "This is the sentiment label returned by the model."

            st.markdown("---")
            st.markdown("### ✨ Analysis Result")

            st.markdown(f"""
            <div class="result-card">
                <div class="result-label">PREDICTED SENTIMENT</div>
                <div class="result-value {result_class}">
                    {emoji} {result_title}
                </div>
                <div class="result-description">{description}</div>
            </div>
            """, unsafe_allow_html=True)

            if hasattr(model, "predict_proba"):
                probabilities = model.predict_proba([review])[0]
                confidence = float(max(probabilities)) * 100

                st.markdown("**Model confidence estimate**")
                st.progress(min(confidence / 100, 1.0))
                st.markdown(f"### {confidence:.1f}%")
                st.caption(
                    "This is the model's estimated probability, not a guarantee "
                    "that the prediction is correct."
                )
            else:
                st.info("This model does not provide probability estimates.")

            with st.expander("View the review you analysed"):
                st.write(review)

        except Exception as e:
            st.error(f"Prediction failed: {e}")


# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    <hr>
    <strong>Sentiment AI</strong> · Review Classification System<br>
    Semester Machine Learning Project · Built with Python and Streamlit
</div>
""", unsafe_allow_html=True)
