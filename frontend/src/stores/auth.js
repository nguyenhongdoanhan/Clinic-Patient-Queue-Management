import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import * as authService from '../services/authService';

export const useAuthStore = defineStore('auth', () => {
  const token = ref(localStorage.getItem('access_token') || '');
  const user = ref(JSON.parse(localStorage.getItem('user') || 'null'));
  const loading = ref(false);
  const error = ref('');

  const isAuthenticated = computed(() => !!token.value);

  const login = async (email, password) => {
    loading.value = true;
    error.value = '';
    
    try {
      const response = await authService.login({ email, password });
      
      token.value = response.data.access_token;
      user.value = response.data.user;
      
      localStorage.setItem('access_token', response.data.access_token);
      localStorage.setItem('user', JSON.stringify(response.data.user));
      
      return response.data;
    } catch (err) {
      error.value = err.response?.data?.detail || 'Đăng nhập thất bại';
      throw err;
    } finally {
      loading.value = false;
    }
  };

  const register = async (username, email, password) => {
    loading.value = true;
    error.value = '';
    
    try {
      const response = await authService.register({ username, email, password });
      return response.data;
    } catch (err) {
      error.value = err.response?.data?.detail || 'Đăng ký thất bại';
      throw err;
    } finally {
      loading.value = false;
    }
  };

  const logout = () => {
    token.value = '';
    user.value = null;
    localStorage.removeItem('access_token');
    localStorage.removeItem('user');
  };

  const getProfile = async () => {
    try {
      const response = await authService.getProfile();
      user.value = response.data;
      localStorage.setItem('user', JSON.stringify(response.data));
      return response.data;
    } catch (err) {
      console.error('Get profile failed:', err);
      throw err;
    }
  };

  return {
    token,
    user,
    loading,
    error,
    isAuthenticated,
    login,
    register,
    logout,
    getProfile
  };
});
