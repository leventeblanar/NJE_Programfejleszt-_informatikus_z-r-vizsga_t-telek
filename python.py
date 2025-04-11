from locust import task


@task
def login_user(self):
    self.client.post("/login", data={"email": "a@b.hu", "password": "123"})
