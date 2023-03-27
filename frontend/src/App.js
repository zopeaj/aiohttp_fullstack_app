import React from 'react';
import { Route, BrowserRouter, Routes } from "react-dom-router";
import './App.css';

function App() {
  return (
     <BrowserRouter>
       <Routes>
           <Route path="/" element={<Start />}>
             <Route index element={<Home/>}  />
             <Route path="contact-us" element={<ContactUs />} />

              <Route path="user" element={<UserProfile />}>
                 <Route index element={<UserDashboard />} />
                 <Route path="reset-password" element={<ResetPassword />} />
                 <Route path="settings" element={<UserSettings />} />
              </Route>

              <Route path="login" element={<Login />} />
              <Route path="email-recovery" element={<EmailRecovery />} />
              <Route path="registration" element={<Registration />} />
              <Route path="*" element={<ErrorPage />} />
           </Route>
       </Routes>
     </BrowserRouter>
  );
}

export default App;
