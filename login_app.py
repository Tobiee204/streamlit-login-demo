import streamlit as st

# CSS nội bộ
st.markdown("""
<style>
body {
    background-color: #1e1e2f;
    color: white;
}
h1 {
    text-align: center;
    color: #f39c12;
}
.login-box {
    background-color: #2c3e50;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 0 15px rgba(0,0,0,0.5);
    width: 350px;
    margin: auto;
}
input[type="text"], input[type="password"] {
    width: 100%;
    padding: 12px;
    margin: 8px 0;
    border-radius: 5px;
    border: none;
}
button {
    background-color: #f39c12;
    color: white;
    padding: 12px;
    width: 100%;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
button:hover {
    background-color: #e67e22;
}
</style>
""", unsafe_allow_html=True)

# Layout HTML
st.markdown("""
<div class="login-box">
    <h1>Login Page</h1>
    <form action="" method="post">
        <input type="text" id="username" placeholder="Username" name="username">
        <input type="password" id="password" placeholder="Password" name="password">
        <button type="submit">Login</button>
    </form>
</div>
""", unsafe_allow_html=True)

# Streamlit thực sự
st.write("### Hoặc đăng nhập tại đây:")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "123456":
        st.success("Đăng nhập thành công!")
    else:
        st.error("Sai tài khoản hoặc mật khẩu!")
