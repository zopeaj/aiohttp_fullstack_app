import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/react/query"

export const routesApi = createApi({
  reducerPath: 'routesApi',
  baseQuery: fetchBaseQuery({ baseUrl: 'http://127.0.0.1:8080/' }),
})
