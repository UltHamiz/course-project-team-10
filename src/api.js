//creates a new instance of the axios HTTP client that is configured to make requests to /api.
import axios from 'axios';

const api = axios.create({
  baseURL: '/api',
});

export default api;