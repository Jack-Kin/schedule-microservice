import json

class Secure:
    def __init__(self):
        self.unsecure_path=set([])

    def security_check(self, request, github, blueprint):
        path =request.path
        result=False
        if path in self.unsecure_path:
            result=True
        else:
            if github.authorized:
                result=True
                resp=github.get("/user")
                github_data=resp.json()
                print("login data:",json.dumps(github_data,indent=2))

        return result


