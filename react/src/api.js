import axios from 'axios';

const api = axios.create({
    baseURL:"https://premier-league-data-website-production.up.railway.app/"
})

export default api;