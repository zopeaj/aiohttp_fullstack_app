import React, { useState, useEffect, Fragment } from "react";
import { Typography, AppBar, ToolBar, Grid, Box, Button, Card, Divider, FormLabel, FormControl, FormGroup, Checkbox, Radio, Switch, InputLabel, Select, Input, TextField } from "@mui/material";


const Registration = () => {
  const [username, setUsername] = useState()
  const [password, setPassword] = useState()
  const [confirmPassword, setConfirmPassword] = useState()
  const [usernameError, setUsernameError] = useState()
  const [passwordError, setPasswordError] = useState()
  const [email, setEmail] = useState()


  return (
    <Fragment>
      <AppBar>
        <ToolBar class="registration-header-toolbar">
          <div class="app-logo">
            App Logo
          </div>
        </ToolBar>
      </AppBar>
      <div class="container">
        <div class="header-container">
          <h5>Register</h5>
        </div>
        <Divider />
      </div>
      <div>
        <Grid container>

        </Grid>
      </div>
    </Fragment>
  );
}

export default Registration

