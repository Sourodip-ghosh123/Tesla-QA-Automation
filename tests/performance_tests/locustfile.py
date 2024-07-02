from locust import HttpUser, task, between

class TeslaWebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def view_home_page(self):
        self.client.get("/")

    @task(3)
    def view_model_3_page(self):
        self.client.get("/model3")

    @task(2)
    def view_inventory(self):
        self.client.get("/inventory/new/m3")
