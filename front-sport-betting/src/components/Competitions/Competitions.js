import './styles.css';
import {useNavigate} from "react-router-dom"
import React, {useState} from "react";
import axios from "../../network/axios.config";

function Competitions() {
    const navigate = useNavigate();
    const getCompetions = () => {
        console.log(localStorage.getItem('token'))
        console.log(sessionStorage.getItem('username'))
        let toke = localStorage.getItem('token');
        while (toke === null) {
            toke = localStorage.getItem('token');
        }
        console.log(localStorage.getItem('token'))
        let id = sessionStorage.getItem('username');
        axios.get('/competitions', {params: {id}, headers: {"X-Token": toke, "X-Username": id}}).then((resp) => { return resp.data.competitions})
    }
    getCompetions();
  return (
      <body>
  <div class="e1_4">
    <div class="e1_5"></div>
    <div class="e1_6"></div><span class="e1_7">Ставки</span><a href="" class="e1_8">telegram_nick</a>

      <a href="" class="e1_12"><span class="e1_13">Создать соревнование</span></a><div class="e1_14"><input type="checkbox" value="Только действующие"/></div>

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
       <tr><td><div class="e1_289">1</div></td><td><div class="e1_290">Лига Чемпионов</div></td><td><div class="e1_291">aabogacheva</div></td><td><div class="e1_292">Активно</div></td><td><a href=""><img src="/Users/nakap/Downloads/project/competitions/Vector.png" alt="" height="15" width="15"></img></a></td></tr></table>
    </div>
  </div>
</body>
  );
}

export default Competitions;