import axios from 'axios';

const API_URL = 'http://localhost:5555';
// const API_URL = 'http://someapp-api:5000';

// Users
export function fetchUsers (jwt) {
  return axios.get(`${API_URL}/user/`, {
    headers: { Authorization: `Bearer: ${jwt}` }
  });
}

export function editUsers (jwt, payload) {
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${jwt}`
  }
  return axios.put(`${API_URL}/user/list/`, payload,
  {
    headers: headers
  });
}

// Games
export function fetchGames (jwt, userId) {
  return axios.get(`${API_URL}/game/user/${userId}`, {
    headers: { Authorization: `Bearer ${jwt}` }
  });
}

export function addGame (jwt, payload) {
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${jwt}`
  }
  return axios.post(`${API_URL}/game/`, payload,
  {
    headers: headers
  });
}

export function editGame (jwt, payload) {
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${jwt}`
  }
  return axios.put(`${API_URL}/game/${payload.gameId}`, payload,
  {
    headers: headers
  });
}

export function removeGame (jwt, payload) {
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${jwt}`
  }
  console.log('api. removeGame. payload:', payload);
  return axios.delete(`${API_URL}/game/${payload.userId}`, { data: payload,
    headers: headers
  });
}

// Game Types
export function fetchGameTypes (jwt) {
  return axios.get(`${API_URL}/game-type/`, {
    headers: { Authorization: `Bearer ${jwt}` }
  });
}

// Roles
export function fetchRoles () {
  return axios.get(`${API_URL}/role/`);
}

// Authentication
export function authenticate (userData) {
  return axios.post(`${API_URL}/auth/login`, userData);
}

// Registration
export function register (userData) {
  return axios.post(`${API_URL}/auth/register`, userData);
}
