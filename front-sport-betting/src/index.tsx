import React from 'react';
// @ts-ignore
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './components/App/App.js';
import Login from "./components/Login/Login.js";
import Register from "./components/Register/Register.js";
import RegisterApprove from "./components/RegisterApprove/RegisterApprove.js";
import Competitions from "./components/Competitions/Competitions.js"
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
        element: <Competitions/>
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
