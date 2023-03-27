import React, { useState, Fragment } from "react";
import { AppBar, ToolBar, Grid, Typography, Container } from "@mui/material"

const UserResetPassword = () => {
  return (
    <Fragment>
      <AppBar class="user-reset-password-tool-bar">
        <ToolBar class="user-toolbar">
          <div class="app-logo">
            App Logo
          </div>
        </ToolBar>
      </AppBar>
      <div class="user-rest-password-contents">
        <Container maxWidth="sm" />
      </div>
    </Fragment>
  )
}

export default UserResetPassword;
