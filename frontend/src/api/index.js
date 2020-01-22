import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000/api';

// Users
export function fetchUsers (jwt) {
  return axios.get(`${API_URL}/users/`, {
    headers: { Authorization: `Bearer: ${jwt}` }
  });
}

export function editUsers (jwt, payload) {
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${jwt}`
  }
  return axios.put(`${API_URL}/users/edit/`, payload,
  {
    headers: headers
  });
}

// Games
export function fetchGames (jwt) {
  return axios.get(`${API_URL}/games/`, {
    headers: { Authorization: `Bearer ${jwt}` }
  });
}

export function addGame (jwt, payload) {
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${jwt}`
  }
  return axios.post(`${API_URL}/games/add/`, payload,
  {
    headers: headers
  });
}

export function editGame (jwt, payload) {
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${jwt}`
  }
  return axios.put(`${API_URL}/games/edit/`, payload,
  {
    headers: headers
  });
}

export function removeGame (jwt, payload) {
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${jwt}`
  }
  return axios.delete(`${API_URL}/games/remove/`, { data: payload,
    headers: headers
  });
}

// Game Types
export function fetchGameTypes (jwt) {
  return axios.get(`${API_URL}/game-types/`, {
    headers: { Authorization: `Bearer ${jwt}` }
  });
}

// Roles
export function fetchRoles () {
  return axios.get(`${API_URL}/roles/`);
}

// Authentication
export function authenticate (userData) {
  return axios.post(`${API_URL}/login/`, userData);
}

// Registration
export function register (userData) {
  return axios.post(`${API_URL}/register/`, userData);
}
