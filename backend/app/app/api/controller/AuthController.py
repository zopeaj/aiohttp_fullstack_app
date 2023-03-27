from aiohttp.web import RouteTableDef, Response, json_response
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBasicCredentials, HTTPBasic, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.app.db.get_db import get_db
from app.app.settings.settingConfiguration import settings


authroutes = RouteTableDef()


jwtConfig = JwtConfig()
passwordConfig = PasswordConfig()
emailSenderService = EmailSenderService()
userService = UserService()
httpBasic = HTTPBasic()
authManager = AuthManager()

@authroutes.post("/login/basic-auth")
def login_basic_auth(request, credentails: HTTPBasicCredentials = Depends(httpBasic)):
    user = { "username": credentials.username, "password": credentails.password }
    authenticated = authManager.authenticate(user.get("username"), user.get("password"))
    token_data = None
    if authenticated:
        token_data = jwtConfig.generate_token({}, authenticated.getUser())
    else:
        raise HTTPException(status_code=404, detail="Not Authenticated")

    return Response(data=token_data, detail="user is authenticated", status=status.HTTP_203_SOMETHING)

@authroutes.post("/api/v1/auth/login")
def login(request, *, db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    """
    get an access token for future request
    """
    user = authManager.authenticate(db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not authManager.userIsActive(db, user=user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token = jwtConfig.generate_token({}, user)
    return {"access_token": access_token} # "token_type": "bearer"

@authroutes.post("/api/v1/auth/register")
def register(request, *, db: Session = Depends(get_db), user_in: UserCreate, current_user: User = Depends(securityConfiguration.get_current_active_admin))
    user = userService.getUserByEmail(db, email=user_in.getEmail())
    if user:
        raise HTTPException(status_code=400, detail="The user with this username already exists in the system.")

    user = userService.create(db, obj_in=user_in)
    if settings.EMAILS_ENABLED and user.getEmail():
        emailSenderService.send_new_account_email(email_to=user_in.getEmail(), username=user_in.getEmail(), password=user_in.getPassword())
    return user

@router.post("/login/test-token", response_model=UserSchema)
def test_token(request, *, current_user: User = Depends(securityConfiguration.get_current_user)) -> Any:
    """
    Test access token
    """
    return current_user

@router.post("/api/v1/auth/password-recovery/{email}", response_model=Msg)
def recover_password(request, *, email: str, db: Session = Depends(get_db)) -> Any:
    """
    Password Recovery
    """
    user = UserService.getUserByEmail(db, email=email)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system."
        )
    password_reset_token = jwtConfig.generate_password_reset_token(email=email)
    emailSenderService.send_reset_password_email(email_to=user.getEmail(), email=email, token=password_reset_token)
    return {"msg": "Password recovery email sent"}

@router.post("/api/v1/auth/reset-password/", response_model=Msg)
def reset_password(request, *, token: str = Body(...), new_password: str = Body(...), db: Session = Depends(get_db),) -> Any:
    """
    Reset Password
    """
    email = jwtConfig.verify_password_reset_token(token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = userService.getUserByEmail(db, email=email)
    if not user:
        raise HTTPException(
            status_code=404, detail="The user with this username does not exist in the system."
        )
    elif not authManager.userIsActive(user):
        raise HTTPException(status_code=400, detail="Inactive user")

    hashed_password = passwordConfig.get_password_hash(new_password)
    user_data = UserCreate(**user)
    user_data.setPassword(hashed_password)
    userService.save(db, user, user_data)
    return {"msg": "Password updated successfully"}
