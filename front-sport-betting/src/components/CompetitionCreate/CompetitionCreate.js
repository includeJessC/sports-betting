import './styles.css';
import {Link, useLoaderData, useNavigate} from "react-router-dom"
import React, {useState} from "react";
import axios from "../../network/axios.config";
import Vector from "../../static/Vector.png"
import Vector1 from "../../static/Vector1.png"

export async function loader()  {
    console.log(localStorage.getItem('token'))
    console.log(sessionStorage.getItem('username'))
    let toke = localStorage.getItem('token');
    while (toke === null) {
        toke = localStorage.getItem('token');
    }
    console.log(localStorage.getItem('token'))
    let id = sessionStorage.getItem('username');
    let data_ans = await axios.get('/competitions', {params: {id}, headers: {"X-Token": toke, "X-Username": id}});
    if (data_ans.status !== 200) {
        alert(data_ans.data.text)
    }
    console.log(data_ans.data.competitions);
    return (await data_ans.data.competitions);
}

export function getActive(flag) {
    if (flag) {
        return "Активно"
    } else {
        return "Закончено"
    }
}

function CompetitionsCreate() {
  const [nameComp, setNameComp] = useState('')
  const [ref, setRef] = useState('')
    const competitions = useLoaderData();
  const navigate = useNavigate();
   const makeComp = async () => {
        let toke = localStorage.getItem('token');
        let id = sessionStorage.getItem('username');
        let data_ans = await axios.post('/create/competition', {"parsing_ref": ref, "name": nameComp}, {params: {id}, headers: {"X-Token": toke, "X-Username": id}});
        if (data_ans.status !== 200) {
            alert(data_ans.data.text)
        } else {
            alert("Соревнование успешно создано")
        }
    }
    const handleComp = () => {
       navigate('/competitions');
    }
  return (
      <body>
  <div class="e22_130">
    <div class="e22_131"></div>
    <div class="e22_132"></div><span class="e22_133">Ставки</span><span class="e22_134">telegram_nick</span>
    <div class="e22_135">
      <div class="e22_136">
        <div class="e22_137"></div>
      </div>
    </div>
    <div class="e22_138"><span class="e22_139">Создать соревнование</span></div><span class="e22_140"><input type="checkbox"></input></span>


     <div class="e1_40">

   <table border="1">

    <caption><div class="e1_180">Соревнования</div></caption>
   <tr>

     <th><div class="e1_190">№</div></th>
     <th><div class="e1_200">Название</div></th>
     <th><div class="e1_210">Создатель</div></th>
     <th><div class="e1_220">Статус</div></th>
    <th></th>
   </tr>
  {competitions.map((elem, index) => {
                            return <tr>
                                <td>
                                    <div className="e1_289">{index + 1}</div>
                                </td>
                                <td>
                                    <Link to={`/competition/${elem.id}`} className="e1_290">{elem.name}</Link>
                                </td>
                                <td>
                                    <div className="e1_291">{elem.created_by}</div>
                                </td>
                                <td>
                                    <div className="e1_292">{getActive(elem.is_active)}</div>
                                </td>
                                <td><a href=""><img src={Vector1} alt=""
                                                    height="15" width="15"></img></a></td>
                            </tr>
                        })}
  </table>
    </div>
    <div class="e22_179"></div>


    <div class="e22_180">
      <div class="e22_181"></div><span class="e22_182">Создание соревнования</span>
      <button onClick={handleComp} class="e22_183">
        <div class="e22_184">
          <img src={Vector} alt="" height="15" width="15"></img>
          <div class="e22_185"></div>
        </div>
      </button>
      <button onClick={makeComp} class="e22_186"><span class="e22_187">Готово</span></button>
      <div class="e22_188"><span class="e22_189">Название</span>
        <input class="e22_190" type="text2" id="name2" name="name2" required minlength="4" maxlength="80"
          size="12" value={nameComp} onChange={(e) => setNameComp(e.target.value)}></input>
      </div>
      <div class="e22_192"><span class="e22_193">Ссылка на парсинг</span>
        <input class="e22_194" type="text2" id="name2" name="name2" required minlength="4" maxlength="80"
          size="12" value={ref} onChange={(e) => setRef(e.target.value)}></input>
    </div>
  </div>
  </div>
</body>
  );
}

export default CompetitionsCreate;