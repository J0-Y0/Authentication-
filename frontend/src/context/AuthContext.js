import React from 'react'
import { createContext, useState } from 'react'
import { jwtDecode } from "jwt-decode";


export const AuthContext = createContext()
export default AuthContext


export const AuthProvider = ({ children }) => {

  const authToken = localStorage.getItem('authToken')
  const [user, setUser] = useState(authToken ? jwtDecode(authToken):null)
  // const [authToken, setAuthToken] = useState(null)
  let loginUser = async (e) => {
      e.preventDefault()
      let response = await fetch('http://127.0.0.1:8000/account/api/token/', {
        method : 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'email': e.target.email.value,
            'password': e.target.password.value
  
        }) 
      })
      const data = await response.json()
    if (response.status === 200) {
      const token = JSON.stringify(data)
      localStorage.setItem('authToken', token )
      setUser(jwtDecode(token))
    } else{
      alert("Unable to login: some thing went wrong")
    }
  }
  let logoutUser = () => { 
    localStorage.removeItem('authToken')
    setUser(null)

  }

  let contextData = {
    loginUser: loginUser,
    logoutUser: logoutUser,
    user: user

  }

  return (
    <AuthContext.Provider value={contextData}>
      {children}
    </AuthContext.Provider>


  )
}
