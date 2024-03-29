import React from 'react';
// @ts-ignore
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './components/App/App.js';
import Login from "./components/Login/Login.js";
import Profile, {loader as profileLoader} from "./components/Profile/Profile.js";
import Register from "./components/Register/Register.js";
import RegisterApprove from "./components/RegisterApprove/RegisterApprove.js";
import Matches, {loader as matchesLoader} from "./components/Matches/Matches.js"
import EndedMatch, {loader as endedLoader} from "./components/EndedMatch/EndedMatch.js"
import ActiveMatch, {loader as activeLoader} from "./components/ActiveMatch/ActiveMatch.js"
import Competitions, {loader as competitionsLoader} from "./components/Competitions/Competitions.js";
// @ts-ignore
import CompetitionsCreate, {loader as crcompetitionsLoader} from "./components/CompetitionCreate/CompetitionCreate.js";
import reportWebVitals from './reportWebVitals';
import {createBrowserRouter, RouterProvider} from "react-router-dom";

const router = createBrowserRouter([
        {
            path: "/",
            element: <App/>,
        },
    {
                    path: '/login',
                    element: <Login/>
                },
    {
        path: '/register',
        element: <Register/>
    },
    {
        path: '/approve',
        element: <RegisterApprove/>
    },
    {
        path: '/competitions',
        loader: competitionsLoader,
        element: <Competitions/>
    },
    {
        path: '/create_competitions',
        loader: crcompetitionsLoader,
        element: <CompetitionsCreate/>
    },
    {
        path: '/profile',
        loader: profileLoader,
        element: <Profile/>
    },
    {
                        path: '/competition/:compId',
                        element: <Matches/>,
                        loader: matchesLoader,
                    },
    {
                        path: '/competitions/:compId/ended/:matchId',
                        element: <EndedMatch/>,
                        loader: endedLoader,
                    },
    {
                        path: '/competitions/:compId/active/:matchId',
                        element: <ActiveMatch/>,
                        loader: activeLoader,
                    }

]
);
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
