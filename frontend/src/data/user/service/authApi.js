import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const authApi = createApi({
  reducerPath: 'authApi',
  baseQuery: fetchBaseQuery({ baseUrl: 'http://localhost:api/v1/' }),
  endpoints: (builder) => ({
    basicAuthentication: builder.mutation({
      query: (data) => {
        return {
          url: 'login/basic-auth',
          method: "POST",
          body: JSON.stringify(data),
          headers: {
            "Content-Type": "application/json"
          }
        }
      }
    }),
    authLogin: builder.mutation({
      query: (data) => {
        return {
          url: 'auth/login',
          method: "POST",
          data: JSON.stringify(data),
          headers: {
            "Content-Type": "application/json"
          }
        }
      }
    }),
    authRegistration: builder.mutation({
      query: (data) => {
        return {
          url: 'auth/register',
          method: "POST",
          data: JSON.stringify(data),
          headers: {
            "Content-Type": "application/json"
          }
        }
      }
    }),
    passwordRecoveryEmail: builder.mutation({
      query: (email, data) => {
        return {
          url: `auth/password-recovery/${email}`,
          method: "POST",
          data: JSON.stringify(data),
          headers: {
            "Content-Type": "application/json"
          }
        }
      }
    }),
    resetPassword: builder.mutation({
      query: (data) => {
        return {
          url: 'auth/reset-password/',
          method: "POST",
          data: JSON.stringify(data),
          headers: {
            "Content-Type": "application/json"
          }
        }
      }
    })
  })
})


export const { useBasicAuthenticationMutation, useAuthLoginMutation, useAuthRegistrationMutation, usePasswordRecoveryEmailMutation, useResetPasswordMutation } = authApi
