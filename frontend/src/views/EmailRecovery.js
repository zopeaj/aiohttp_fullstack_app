import React, { useState, Fragment } from "react";
import { Typography, Button, Grid, CircularProgress } from "@mui/material";

const EmailRecovery = () => {
  const [checkEmail, setCheckEmail ] = useState();
  const [loading, setLoading] = useState(false);

  const onCheckEmailChange = (e) => {
    setCheckEmail(e.target.value);
  }

  const handleCheckEmail = () => {
    setLoading(true);
  }

  return (
     <Fragment>
       <AppBar class="email-recovery-app-bar">
         <ToolBar class="email-toolbar">
           <div class="app-logo">
             App Logo
           </div>
         </ToolBar>
       </AppBar>
       <div>
         <div class="email-recover-header">
           <h5>Email Recovery</h5>
           <div>
             <TextInput value={checkEmail} onChange={onCheckEmailChange} label="check-email" type="text" InputLabelProps={{
                 shrink: true
             }} />
             <Button variant="contained" disabled={loading} onChange={handleCheckEmail}>{loading && <CircularProgress size={18}/>}Check Email</Button>
           </div>
         </div>
       </div>
     </Fragment>
  );
}
