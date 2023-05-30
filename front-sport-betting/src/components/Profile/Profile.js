import './styles.css';
import {useNavigate} from "react-router-dom"
import React, {useState} from "react";
import axios from "../../network/axios.config";
import {Link, Outlet, useLoaderData} from "react-router-dom";
import Vector2 from "../../static/Vector2.png"

export async function loader()  {
    let toke = localStorage.getItem('token');
    let id = sessionStorage.getItem('username');
    let data_ans = await axios.get('/user', {params: {id}, headers: {"X-Token": toke, "X-Username": id}});
    if (data_ans.status !== 200) {
        alert(data_ans.data.text)
    }
    return (await data_ans.data.user_meta);
}

function Profile() {
    const navigate = useNavigate();
    const user = useLoaderData();
    let id = sessionStorage.getItem('username');
    const [name, setName] = useState('')
    const [surname, setSurname] = useState('')
    const editProfile = async () => {
        let toke = localStorage.getItem('token');
        let id = sessionStorage.getItem('username');
        let data_ans = await axios.put('/user', {"user_meta": {"name": name, "surname": surname, "password": ""}}, {params: {id}, headers: {"X-Token": toke, "X-Username": id}});
        if (data_ans.status !== 200) {
            alert(data_ans.data.text)
        } else {
            navigate("/competitions")
        }
    }
  return (
      <body>
  <div class="e20_60">
    <div class="e20_61"></div>
    <div class="e20_62"></div><span class="e20_63">Ставки</span><span class="e20_64">{id}</span>
    <div class="e20_65">
      <div class="e20_66">
        <div class="e20_67"></div>
      </div>
    </div>


     <div class="e1_40">
    </div>
    <div class="e20_109"></div>



    <div class="e20_110">
      <div class="e20_111"></div><span class="e20_112">Профиль</span>
      <div class="e20_113"><span class="e20_114">Телеграм</span>
        <div class="e20_115"></div><span class="e20_116">{id}</span>
      </div>
      <div class="e20_117">

        <div class="e20_118">

          <div class="e20_119"> <a href="/competitions"><img src={Vector2} alt="" height="15" width="15"></img></a></div>
        </div>
      </div>
      <button onClick={editProfile} class="e20_120"><span class="e20_121">Готово</span></button>
      <div class="e20_122"><span class="e20_123">{user.surname}</span>
        <input class="e20_124" type="text2" id="name2" name="name2" required minlength="4" maxlength="18"
          size="12" value={surname} onChange={(e) => setSurname(e.target.value)}></input>
      </div>
      <div class="e20_126"><span class="e20_127">{user.name}</span>
        <input class="e20_128" type="text2" id="name2" name="name2" required minlength="4" maxlength="18"
          size="12" value={name} onChange={(e) => setName(e.target.value)}></input>
      </div>
    </div>
  </div>
</body>
  );
}

export default Profile;