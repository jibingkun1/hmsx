from flask import Blueprint



router_user = Blueprint("use_page",__name__)
@router_user.route("/login")
def login():
    return "这是登陆页面"