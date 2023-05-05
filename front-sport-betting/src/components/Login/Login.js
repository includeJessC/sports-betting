import './styles.css';
import {useNavigate} from "react-router-dom"
import React, {useState} from "react";
import {loginUser} from '../../network/requests.ts';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();
    const handleLogin = () => {
      localStorage.setItem('username', username);
      let response = loginUser(username, password);
      localStorage.setItem('token', response.token)
      navigate('/');
    }
  return (
      <body>
      <div className="e1_39">
          <div className="e1_40"></div>
          <span className="e1_41">Ставки</span>
          <div className="e1_42"><span className="e1_43">Регистрация</span></div>
          <div className="e1_44"><span className="e1_45">Вход</span></div>
          <span className="e1_46">Данное приложение является программным
      проектом студентки третьего курса образовательной программы “Прикладная математика и информатика” НИУ ВШЭ
      Богачевой Анны Андреевны</span>
          <div className="e1_47"></div>
          <div className="e1_48">
              <div className="e1_49"></div>
              <div className="e1_50"></div>
              <span className="e1_51">Нет аккаунта? Зарегистрироваться</span><span
              className="e1_52">Авторизация</span>
              <div className="e1_53"><span className="e1_54">Телеграм</span>
                  <input className="e1_55" type="text" id="name" name="name" required minLength="4" maxLength="8"
                         size="12" value={username} onChange={(e) => setUsername(e.target.value)}></input>
              </div>
              <div className="e1_56"><span className="e1_57">Пароль</span>
                  <input className="e1_58" type="text" id="name" name="name" required minLength="4" maxLength="8"
                         size="12" value={password} onChange={(e) => setPassword(e.target.value)}></input>

              </div>
              <div className="e1_59">
                  <div className="e1_60">
                      <div className="e1_61"></div>
                  </div>
              </div>
              <button onClick={handleLogin} className="e1_62"><span className="e1_63">Вход</span></button>
          </div>
      </div>
      </body>
  );
}

export default Login;