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

function ActiveMatch() {
    const navigate = useNavigate();
    const [first_team_result, setFirstTeamResult] = useState('')
    const [second_team_result, setSecondTeamResult] = useState('')
    const match = useLoaderData();
    if (typeof(match.user_bets) == "undefined") match.user_bets = []
    const handleBet = async () => {
        await axios.post('/create/bet', {"bets": [{"bet": parseInt(first_team_result, 10), "name": "first_team_result"}, {"bet": parseInt(second_team_result, 10), "name": "second_team_result"}]}, {params: {id: id, match_id: match.id, competition_id: id_comp}, headers: {"X-Token": toke, "X-Username": id}});
        navigate('/competitions')
    }
    let id = sessionStorage.getItem('username');
    let toke = localStorage.getItem('token');
    let name_comp = sessionStorage.getItem("comp_name");
     let id_comp = sessionStorage.getItem("comp_id");
  return (
      <body>
  <div class="e9_2">
    <div class="e9_3"></div><span class="e9_4">Ставки</span><a href="/profile" div class="e9_5">{id}</a>
    <div class="e9_6">
      <div class="e9_7">
        <div class="e9_8"></div>
      </div>
    </div>

    <button onClick={handleBet} class="e9_11"><span class="e9_12">Подтвердить</span></button>

  <span class="e9_14">{name_comp}</span>


    <div class="e9_32">
      <div class="e9_33"><span class="e9_34">{match.first_team_name}</span></div>
      <div class="e9_35">
        <div class="e9_36">
          <div class="e9_37"></div>
        </div>
      </div>
      <div class="e9_38"><span class="e9_39">{match.second_team_name}</span></div>
    </div>
    <div class="e9_40">



      <input class="e9_41" type="text2" id="name2" name="name2" required minlength="1" color="white" maxlength="2" value={first_team_result} onChange={(e) => setFirstTeamResult(e.target.value)}></input>
      <div class="e9_43">
        <div class="e9_44">
          <div class="e9_45"></div>
        </div>
      </div>
       <input class="e9_46" type="text2" id="name2" name="name2" required minlength="1" color="white" maxlength="2" value={second_team_result} onChange={(e) => setSecondTeamResult(e.target.value)}></input></div>
    </div>
    <div class="e9_48"></div><a href="/competitions" div class="e9_49">Назад</a>
    <div class="e9_50">
      <div class="e9_51">
        <div class="e9_52"></div>
      </div>
    </div>
    <div class="e9_53">
      <div class="e9_54">
        <div class="e9_55"></div>
      </div>
    </div>
    <div class="e9_56">
      <div class="e9_57">
        <div class="e9_58"></div>
      </div>
      <div class="e9_59">
        <div class="e9_60">
          <div class="e9_61"></div>
        </div>
      </div>
    </div>
</body>
  );
}

export default ActiveMatch;