import './styles.css';
import {useNavigate} from "react-router-dom"
import React, {useState} from "react";
import axios from "../../network/axios.config";

function Register() {
    const [username, setUserName] = useState('');
    const [name, setName] = useState('');
    const [surname, setSurname] = useState('');
    const [password, setPassword] = useState('');
    const [repeat_password, setRepeatPassword] = useState('');
    const navigate = useNavigate();
    const handleBack = () => {
      navigate('/');
    }
    const handleApprove = () => {
        sessionStorage.setItem('username', username)
        if (password !== repeat_password) {
            alert("Пароли не сходятся")
            return
        }
        axios.post('/user_register', {'id': username, 'user_meta': {'name': name, 'surname': surname, 'password': password}
     }).then((resp) => {if (resp.status !== 200) {alert(resp.data.text); return;} navigate('/approve');}).catch(function (error) {
    if (error.response) alert(error.data.text) })
    }
  return (
      <body>
      <div className="e3_2">
          <div className="e3_3"></div>
          <span className="e3_4">Ставки</span>
          <div className="e3_5"><span className="e3_6">Регистрация</span></div>
          <div className="e3_7"><span className="e3_8">Вход</span></div>
          <span className="e3_9">Данное приложение является программным
      проектом студентки третьего курса образовательной программы “Прикладная математика и информатика” НИУ ВШЭ
      Богачевой Анны Андреевны</span>
          <div className="e3_10"></div>
          <div className="e3_11">
              <div className="e3_12"></div>
              <span className="e3_13">Регистрация</span>
              <div className="e3_14"><span className="e3_15">Телеграм</span>
                  <input className="e3_16" type="text" id="name" name="name" required minLength="4" maxLength="8"
                         size="12" value={username} onChange={(e) => setUserName(e.target.value)}></input>
              </div>
              <div className="e3_17"><span className="e3_18">Пароль</span>

                  <input className="e3_19" type="password" id="name" name="name" required minLength="4" maxLength="8"
                         size="12" value={password} onChange={(e) => setPassword(e.target.value)}></input>
              </div>
              <div className="e3_20">
                  <div className="e3_21">
                      <div className="e3_22"></div>
                  </div>
              </div>
              <button className="e3_23" onClick={handleApprove}><span className="e3_24">Продолжить</span></button>
              <div className="e3_25"><span className="e3_26">Фамилия</span>
                  <input className="e3_27" type="text2" id="name2" name="name2" required minLength="4" maxLength="8"
                         size="12" value={surname} onChange={(e) => setSurname(e.target.value)}></input>
              </div>
              <div className="e3_28"><span className="e3_29">Имя</span>
                  <input className="e3_30" type="text2" id="name2" name="name2" required minLength="4" maxLength="8"
                         size="12" value={name} onChange={(e) => setName(e.target.value)}></input>
              </div>
              <div className="e3_31"><span className="e3_32">Повторите пароль</span>
                  <input className="e3_33" type="password" id="name2" name="name2" required minLength="4" maxLength="12"
                         size="12" value={repeat_password} onChange={(e) => setRepeatPassword(e.target.value)}></input>
              </div>
              <button onClick={handleBack} className="e3_34"><span className="e3_35">Назад</span></button>
          </div>
      </div>
      </body>
  );
}

export default Register;