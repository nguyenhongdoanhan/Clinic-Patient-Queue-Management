import api from "./api";

export const login = (data) => {
    return api.post("/auth/login", data);
};

export const register = (data) => {
    return api.post("/auth/register", data);
};  

export const getProfile = () => {
    return api.get("/users/me");
};

export const refreshToken = (refreshToken) => {
    return api.post("/auth/refresh", {
        refresh_token: refreshToken
    });
};

export const logout = () => {
    return api.post("/auth/logout");
};