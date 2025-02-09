from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
 
class Sharing:
    def __init__(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.driver.get("http://127.0.0.1:5000")
       self.driver.find_element(By.LINK_TEXT, "Login").click()
 
    # New function that logins in user
    def login_user(self, username, password):
       self.driver.find_element(By.ID, "email").send_keys(username)
       self.driver.find_element(By.ID, "password").send_keys(password)
       createLink = self.driver.find_element(By.TAG_NAME, "button")
       createLink.click()
    
    # New function that creates a project
    def create_project(self, email, password, projectname, projectdescription, roster_file, rubric_file):
       Sharing.login_user(self, email, password)
       self.driver.find_element(By.LINK_TEXT, "Create New Project").click()
       self.driver.find_element(By.ID, "project_name").send_keys(projectname)
       self.driver.find_element(By.ID, "project_description").send_keys(projectdescription)
       self.driver.find_element(By.ID, "student_file").send_keys(roster_file)
       self.driver.find_element(By.ID, "json_file").send_keys(rubric_file)
       createLink = self.driver.find_element(By.TAG_NAME, "button")
       createLink.click()
  
    # New function that creates an evaluation
    def create_evaluation(self, projectname, evaluationname, evaluationdescription):
       self.driver.find_element(By.LINK_TEXT, projectname).click()
       self.driver.find_element(By.LINK_TEXT, "Create a New Evaluation").click()
       self.driver.find_element(By.ID, "evaluation_name").send_keys(evaluationname)
       self.driver.find_element(By.ID, "evaluation_description").send_keys(evaluationdescription)
       self.driver.find_element(By.ID, "evaluation_submit").click()
  
    # New function that creates a rating
    def create_rating(self, email, password, projectname, projectdescription, roster_file, rubric_file, evaluationname, evaluationdescription):
       Sharing.create_project(self, email, password, projectname, projectdescription, roster_file, rubric_file)
       Sharing.create_evaluation(self, projectname, evaluationname, evaluationdescription)
 
    # New function that returns the current url after clicking on the project name link
    def create_sharing_return_current_url_after_clicking_project_name_link(self, email, password, projectname, projectdescription, roster_file, rubric_file, evaluationname, evaluationdescription):
       Sharing.create_rating(self, email, password, projectname, projectdescription, roster_file, rubric_file, evaluationname, evaluationdescription)
       self.driver.find_element(By.LINK_TEXT, "Manage Projects").click()
       self.driver.find_element(By.LINK_TEXT, projectname).click()
       return self.driver.current_url
    
    # New function that returns the current url after clicking manage projects button

    def create_sharing_return_current_url_after_clicking_manage_projects_button(self, email, password):
        Sharing.login_user(self, email, password)
        self.driver.find_element(By.LINK_TEXT, "Manage Projects").click()
        self.driver.find_element(By.LINK_TEXT, "Manage").click()
        return self.driver.current_url
    

    # New function that returns the current url after clicking manage projects button
    def create_sharing_return_current_url_after_clicking_manage_projects_button(self, email, password):
        Sharing.login_user(self, email, password)
        self.driver.find_element(By.LINK_TEXT, "Manage Projects").click()
        self.driver.find_element(By.LINK_TEXT, "Manage").click()
        return self.driver.current_url
    
    # New function that returns the text after clicking delete project button
    def create_sharing_return_text_after_clicking_delete_project_button(self, email, password, projectname):
        Sharing.login_user(self, email, password)
        self.driver.find_element(By.LINK_TEXT, "Manage Projects").click()
        self.driver.find_element(By.LINK_TEXT, "Warning ! Delete the Rubric").click()
        text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        try:
            self.driver.find_element(By.LINK_TEXT, projectname)
        except:
            text = "not found"
        return text
    
    # New function that returns the current url after clicking downloading button
    def create_sharing_return_current_url_after_clicking_downloading_button(self, email, password, projectname, projectdescription, roster_file, rubric_file, evaluationname, evaluationdescription):
        Sharing.create_rating(self, email, password, projectname, projectdescription, roster_file, rubric_file, evaluationname, evaluationdescription)
        self.driver.find_element(By.LINK_TEXT, "Manage Projects").click()
        self.driver.find_element(By.LINK_TEXT, "Download all evaluations").click()
        return self.driver.current_url
      
    # New function that returns the current url after clicking the projects link in the breadcrumbs
    def create_sharing_return_current_url_after_clicking_projects_link_in_the_breadcrumbs(self, email, password):
         Sharing.login_user(self, email, password)
         self.driver.find_element(By.LINK_TEXT, "Manage Projects").click()
         self.driver.find_element(By.LINK_TEXT, "Manage").click()
         time.sleep(5)
         self.driver.find_element(By.LINK_TEXT, "Manage Projects").click()
         return self.driver.current_url

    # New function that returns the text after clicking the send email button
    def create_sharing_return_text_after_clicking_send_email_button(self, email, password, projectname, evaluationname):
        Sharing.login_user(self, email, password)
        self.driver.find_element(By.LINK_TEXT, projectname).click()
        self.driver.find_element(By.LINK_TEXT, "Create a New Evaluation").click()
        self.driver.find_element(By.ID, "evaluation_name").send_keys(evaluationname + "2")
        self.driver.find_element(By.ID, "evaluation_submit").click()
        self.driver.find_element(By.LINK_TEXT, "Manage Projects").click()
        self.driver.find_element(By.LINK_TEXT, "Manage").click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Send Email").click()
        text = self.driver.find_element(By.CLASS_NAME, "sending_progress_message").text
        return text
    

    # New function that returns checked after clicking the send with scores switch
    def create_sharing_return_checked_after_clicking_send_with_scores_switch(self, email, password):
        Sharing.login_user(self, email, password)
        self.driver.find_element(By.LINK_TEXT, "Manage Projects").click()
        self.driver.find_element(By.LINK_TEXT, "Manage").click()
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, "switch").click()
        checked = self.driver.find_element(By.CLASS_NAME, "switchCheckbox").get_attribute("checked")
        return checked


    def __del__(self):
       self.driver.quit()

