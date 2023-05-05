import './styles.css';
import {useNavigate} from "react-router-dom"
import React, {useState} from "react";
import {loginUser} from '../../network/requests.ts';

function RegisterApprove() {
    const navigate = useNavigate();
    const [code, setCode] = useState('');
    const handleRegister = () => {
      navigate('/register');
    }
  return (
      <body>
      <div className="e3_72">
          <div className="e3_73"></div>
          <span className="e3_74">Ставки</span>
          <div className="e3_75"><span className="e3_76">Регистрация</span></div>
          <div className="e3_77"><span className="e3_78">Вход</span></div>
          <span className="e3_79">Данное приложение является программным
      проектом студентки третьего курса образовательной программы “Прикладная математика и информатика” НИУ ВШЭ
      Богачевой Анны Андреевны</span>
          <div className="e3_80"></div>
          <div className="e3_81">
              <div className="e3_82"></div>
              <span className="e3_83">Введите код подтверждения из @sportingbettingbot</span>
              <a href="" className="e3_84"><span className="e3_85">Готово</span></a>
              <div className="e3_86">
                  <input className="e3_87" type="text" id="name" name="name" required minLength="4" maxLength="8"
                         size="12" value={code} onChange={(e) => setCode(e.target.value)}></input>
              </div>
              <button onClick={handleRegister} className="e3_88"><span className="e3_89">Назад</span></button>
          </div>
      </div>
      </body>
  );
}

export default RegisterApprove;