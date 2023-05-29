import './styles.css';
import {useNavigate} from "react-router-dom"
import React, {useState} from "react";
import axios from "../../network/axios.config";
import {Link, Outlet, useLoaderData} from "react-router-dom";
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

export function getActiveCompetitions(competitions) {
    let res = []
    for (var elem in competitions) {
        if (elem.is_active) {
            res.push(elem)
        }
    }
    return res
}


function Competitions() {
    const navigate = useNavigate();
    const handleCreate = async () => {
        navigate('/create_competitions');
    }
    const [value, setValue] = useState('')
    const competitions = useLoaderData();
    let competitions_res = competitions;
    const changeCompetitions = (value) => {
        if (!value) {
            competitions_res = competitions;
        }
       competitions_res = getActiveCompetitions(competitions);
    }
  return (
      <body>
  <div class="e1_4">
    <div class="e1_5"></div>
    <div class="e1_6"></div><span class="e1_7">Ставки</span><a href="" class="e1_8">telegram_nick</a>

      <button onClick={handleCreate} class="e1_12"><span class="e1_13">Создать соревнование</span></button><div class="e1_14"><input type="checkbox" value="Только действующие" name="Только действующие"  id="active"/><label
      htmlFor="active" value={value} onChange={(e) => {setValue(e.target.value); changeCompetitions(e.target.value)}}>Только действующие</label></div>

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
       {competitions_res.map((elem, index) => {
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
  </div>
</body>
  );
}

export default Competitions;