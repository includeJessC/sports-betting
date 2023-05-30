import './styles.css';
import {useNavigate} from "react-router-dom"
import React, {useState} from "react";
import axios from "../../network/axios.config";
import {Link, Outlet, useLoaderData} from "react-router-dom";
import Vector5 from "../../static/Vector5.png"
import Vector3 from "../../static/Vector3.png";
import {getActiveLink} from "../Matches/Matches";

export async function loader({params})  {
    let toke = localStorage.getItem('token');
    let id = sessionStorage.getItem('username');
    let data_ans = await axios.get('/match_info', {params: {id: id, match_id: params.matchId, competition_id: params.compId}, headers: {"X-Token": toke, "X-Username": id}});
    if (data_ans.status !== 200) {
        alert(data_ans.data.text)
    }
    return (await data_ans.data);
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

function EndedMatch() {
    const navigate = useNavigate();
    const handleCreate = async () => {
        navigate('/create_competitions');
    }
    const match = useLoaderData();
    let id = sessionStorage.getItem('username');
    let name_comp = sessionStorage.getItem("comp_name");
  return (

<body>
  <div class="e8_158">
    <div class="e8_159"></div><span class="e8_160">Ставки</span><a href="/profile" div class="e8_161">{id}</a>
    <div class="e8_162">
      <div class="e8_163">
        <div class="e8_164"></div>
      </div>
    </div>
    <span class="e8_166">{name_comp}</span>
      <div class="e1_40">

      <table border="1">

        <caption>
          <div class="e1_180">Ставки</div>
        </caption>
        <tr>

          <th>
            <div class="e1_190">#</div>
          </th>
          <th>
            <div class="e1_200">Ставка</div>
          </th>
          <th>
            <div class="e1_210">Очки</div>
          </th>

        </tr>
          {match.user_bets.map((elem, index) => {
              <tr>
                  <td>
                      <div className="e1_289">{index + 1}</div>
                  </td>
                  <td>
                      <div className="e1_290">{elem.name}</div>
                  </td>
                  <td>
                      <div className="e1_291">{elem.bet}</div>
                  </td>

              </tr>
                        })}
      </table>
    </div>
    <div class="e8_187">
      <div class="e8_188"><span class="e8_189">{match.first_team_name}</span></div>
      <div class="e8_190">
        <div class="e8_191">
          <div class="e8_192"></div>
        </div>
      </div>
      <div class="e8_193"><span class="e8_194">{match.second_team_name}</span></div>
    </div>
    <div class="e8_195">
      <div class="e8_196"><span class="e8_197">{match.first_team_result}</span></div>
      <div class="e8_198">
        <div class="e8_199">
          <div class="e8_200"></div>
        </div>
      </div>
      <div class="e8_201"><span class="e8_202">{match.second_team_result}</span></div>
    </div>

    <div class="e8_203"></div><a href="" div class="e8_204">Назад</a><span class="e8_205"><img src={Vector5} alt="" height="15" width="15"></img>  На этот матч больше нельзя ставить
      ставки</span>
    <div class="e8_206">
      <div class="e8_207">
        <div class="e8_208"></div>
      </div>
    </div>
  </div>
</body>
  );
}

export default EndedMatch;