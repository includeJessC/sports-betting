import axios from "./axios.config"
import {Token} from "../types/Token";

export const createUser = (user_info:  FormDataEntryValue) => {
    return axios.post('/user_register', {user_info
    })
}

 export const loginUser = (username: string, password: string) => {
     return axios.post<Token>('/user_login', {"id": username, "password": password
     })
 }

export const userApprove = (user_info:  FormDataEntryValue) => {
    return axios.post<Token>('/user_login', {user_info
    })
}