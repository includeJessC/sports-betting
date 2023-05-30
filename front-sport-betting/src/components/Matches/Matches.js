import './styles.css';
import {useNavigate} from "react-router-dom"
import React, {useState} from "react";
import axios from "../../network/axios.config";
import {Link, Outlet, useLoaderData} from "react-router-dom";
import Vector3 from "../../static/Vector3.png"

export async function loader({params})  {
    let toke = localStorage.getItem('token');
    let id = sessionStorage.getItem('username');
    let data_ans = await axios.get('/competitions_info', {params: {competition_id: params.compId, id: id}, headers: {"X-Token": toke, "X-Username": id}});
    if (data_ans.status !== 200) {
        alert(data_ans.data.text)
    }
    console.log(data_ans.data);
    return (await data_ans.data);
}

export function getActive(flag) {
    if (flag) {
        return "Активно"
    } else {
        return "Закончено"
    }
}

export function getActiveLink(flag, comp_id, match_id, bets) {
    if (flag && typeof(bets) == "undefined") {
        return `/competitions/${comp_id}/active/${match_id}`
    } else {
        return `/competitions/${comp_id}/ended/${match_id}`
    }
}

function Matches() {
    const navigate = useNavigate();
    const handleCreate = async () => {
        navigate('/create_match');
    }
    const competition = useLoaderData();
    sessionStorage.setItem("comp_name", competition.name)
    sessionStorage.setItem("comp_id", competition.id)
    let id = sessionStorage.getItem('username');
  return (
      <body>
      <div className="e23_196">
          <div className="e23_197"></div>
          <span className="e23_198">Ставки</span><a href="/profile" div className="e23_199">{id}</a>


          <a href="" className="e23_205"><span className="e23_206">Добавить матч</span></a>
          <span className="e23_208">Согревнования</span>


          <div className="e23_244"></div>
          <a href="" className="e23_245">Список лидеров</a><a href="" div className="e23_246">Пригласить</a>
          <div className="e23_247"></div>
          <a href="/competitions" div className="e23_248">Назад</a>


          <div className="e1_40">

              <table border="1" style={{maxHeight: '800px', overflow: 'scroll'}}>

                  <caption>
                      <div className="e1_180">Матчи</div>
                  </caption>
                  <tr>

                      <th>
                          <div className="e1_190">№</div>
                      </th>
                      <th>
                          <div className="e1_200">Матч</div>
                      </th>
                      <th>
                          <div className="e1_210">Результат</div>
                      </th>
                      <th>
                          <div className="e1_220">Кол-во очков</div>
                      </th>
                      <th>
                          <div className="e1_220">Дата</div>
                      </th>
                      <th>
                          <div className="e1_220">Статус</div>
                      </th>
                      <th></th>
                  </tr>
                  {competition.matches.map((elem, index) => {
                            return <tr>
                      <td>
                          <div className="e1_289">{index + 1}</div>
                      </td>
                      <td>
                          <Link to={getActiveLink(elem.is_active, competition.id, elem.id, elem.user_bets)} className="e1_290">{elem.name}</Link>
                      </td>
                      <td>
                          <div className="e1_291">{`${elem.first_team_result} : ${elem.second_team_result}`}</div>
                      </td>
                      <td>
                          <div className="e1_292">{elem.bets_result}</div>
                      </td>
                      <td>
                          <div className="e1_292">{elem.start_time}</div>
                      </td>
                      <td>
                          <div className="e1_292">{getActive(elem.is_active, elem)}</div>
                      </td>
                      <td><a href=""><img src={Vector3} alt="" height="15"
                                          width="15"></img></a></td>
                  </tr>
                        })}
          </table>
      </div>
      </div>

      </body>
  );
}

export default Matches;