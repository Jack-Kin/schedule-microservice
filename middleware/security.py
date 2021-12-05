import json


class Secure:
    def __init__(self):
        self.secure_path = [
            "/",
            "/login/github",
            "/login/github/authorized",
            "/login/google",
            "/login/google/authorized"
        ]

    def security_check_github(self, request, github, blueprint):
        path = request.path
        result = False

        if path in self.secure_path:
            result = True
            if github.authorized:
                result = True
                # user_info_endpoint = "/oauth2/v2/userinfo"
                resp = github.get("/user")
                github_data = resp.json()
                print("login data:", json.dumps(github_data, indent=2))
                session = blueprint.session
                token = session.token
                print("Token:", json.dumps(token, indent=2))
            else:
                result = False

        return result
