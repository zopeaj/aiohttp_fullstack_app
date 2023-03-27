import React, { useState, Fragment } from "react";
import { Typography, AppBar, ToolBar, Grid, Box, Input } from "@mui/material";
import { username } from "../../../data/user/user.selectors";


const UserProfile = () => {

  return (
     <Fragment>
       <AppBar class="user-profile">
         <ToolBar class="user-profile-toolbar">
           <div class="app-logo">
             App Logo
           </div>
         </ToolBar>
       </AppBar>
       <div>
         <div class="user-profile">
           <h5>User Profile</h5>
         </div>
         <h3>
           Welcome { usename } !
         </h3>
       </div>
     </Fragment>
  );
}

export default UserProfile
