import './App.css';
import {useNavigate} from "react-router-dom"

function App() {
    const navigate = useNavigate();
    const handleLogin = () => {
        navigate('/login')
    }
    const handleRegister = () => {
        navigate('/register')
    }
  return (// !localStorage.getItem('token') || !localStorage.getItem('id') ?
      <body>
          <div className="e3_64">
              <div className="e3_65"></div>
              <span className="e3_66">Ставки</span>
              <button className="e3_67"><span className="e3_68" onClick={handleRegister}>Регистрация</span></button>
              <button className="e3_69"><span className="e3_70" onClick={handleLogin}>Вход</span></button><span className="e3_71">Данное приложение является программным
      проектом студентки третьего курса образовательной программы “Прикладная математика и информатика” НИУ ВШЭ
      Богачевой Анны Андреевны</span>
          </div>
          </body>
  );
}

export default App;
