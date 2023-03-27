import React, { useState, Fragment } from "react";
import { Typography, Grid, Card, Button } from "@mui/material";
import { Link } from "react-router-dom";

const Start = () => {
  return (
     <Fragment>
       <AppBar position="static">
         <ToolBar variant="dense">
           <div class="app-logo">
             App Logo
           </div>
         </ToolBar>
         <div>
           Lorem
         </div>
       </AppBar>
     </Fragment>
  );
}

export default Start;
