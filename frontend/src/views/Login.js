import React, { useState, Fragment } from "react";
import { Typography, Grid, Box, FormLabel, FormControl, AppBar, ToolBar, FormGroup, FormControlLabel, FormHelperText, Input, TextField } from '@mui/material';
import { useDispatch } from "react-redux";

const Login = () => {
  const [username, setUsername] = useState();
  const dispatch = useDispatch();
  const [usernameError, setUsernameError] = useState()
  const [password, setPassword] = useState();
  const [passwordError, setPasswordError] = useState();

  const onLogin = () => {

  }

  return (
    <Fragment>
      <AppBar class="login-bar">
        <ToolBar class="login-toolbar">
          <div class="app-logo">
            App Logo
          </div>
        </ToolBar>
      </AppBar>
      <div class="login-container">
        <div class="login-text">
          <h5>Login::</h5>
        </div>
        <Grid container>
          <Grid item>

          </Grid>
        </Grid>
      </div>
    </Fragment>
  )
}

export default Login
