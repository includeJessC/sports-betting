import { default as axiosLib } from 'axios';

const axios = axiosLib.create({
    baseURL: 'https://cors-anywhere.herokuapp.com/http://51.250.21.113:80',
    timeout: 10000,
    headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json'
    }
});

axios.interceptors.request.use((config) => {
    config.headers['X-Token'] = localStorage.getItem('token')
    config.headers['X-Username'] = localStorage.getItem('username')
    return config;
});

export default axios;

