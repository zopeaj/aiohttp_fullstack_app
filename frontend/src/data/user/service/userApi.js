import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const userApi = createApi({
  reducerPath: 'userApi',
  baseQuery: fetchBaseQuery({ baseUrl: 'http://localhost:5051/user/' }),
  endpoints: (builder) => ({
    fetchUser: builder.query({
      query: (id) => {
        return {
          url: `${id}`,
          method: "GET",
          headers: {
            "Content-Type": "application/json"
          }
        }
      }
    }),
    updateUser: builder.mutation({
      query: (id, data) => {
        return {
          url: `${id}`,
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data)
        }
      }
    }),
    deleteUser: builder.mutation({
      query: (id) => {
        return {
          url: `${id}`,
          method: "DELETE",
          headers: {
            "Content-Type": "application/json"
          }
        }
      }
    }),
  })
})

export const { useFetchUserQuery, useUpdateUserMutation, useDeleteUserMutation } = userApi;







