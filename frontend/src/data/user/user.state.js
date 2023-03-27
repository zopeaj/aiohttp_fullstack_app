import { createEntityAdapter } from "reduxjs/toolkit";

export const initialState = createEntityAdapter.getInitialState({
  loginError: null,
  registrationError: null,
  authenticated: false,
  loading: false,
  userId: null,
  token: null,
  email: null,
})
