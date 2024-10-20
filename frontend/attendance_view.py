import requests
from bs4 import BeautifulSoup
import flet as ft

class AttendanceFetcher:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.Session()

    def login(self):
        # URL for the login endpoint for username
        username_url = "https://academia.srmist.edu.in/accounts/p/10002227248/signin/v2/lookup/ab3135@srmist.edu.in"
        username_payload = {'username': self.username}
        
        headers = {
            'Content-Type': 'application/json',  # Ensure you set the right content type
            'Accept': 'application/json',         # Specify the accepted response type
        }

        # Send POST request for username
        username_response = self.session.post(username_url, json=username_payload, headers=headers)

        if username_response.ok:
            print("Username submission successful")
        else:
            print("Username submission failed:", username_response.status_code, username_response.text)
            return False

        # URL for the login endpoint for password
        password_url = "https://academia.srmist.edu.in/accounts/p/10002227248/signin/v2/primary/10063513102/password?digest=b067675755a2cb7b029e2dd2e2045ce3c1db7a834617c46799c32d7d1f36650bfbd93df12d305ae972e25b66b6c89c2d4cc91fbd7f8f4878e8a189b47765f05d46428b1425ec5ae11af924d8e0975835ab43ed106e1767a54b79e838c3601b79c393038b0654722545ee4628c5342a94&cli_time=1729420540318&servicename=ZohoCreator&service_language=en&serviceurl=https%3A%2F%2Facademia.srmist.edu.in%2Fportal%2Facademia-academic-services%2FredirectFromLogin"
        
        # Send POST request for password
        password_payload = {'password': self.password}
        password_response = self.session.post(password_url, json=password_payload, headers=headers)

        if password_response.ok:
            print("Login successful")
            return True
        else:
            print("Login failed:", password_response.status_code, password_response.text)
            return False

    def fetch_attendance(self):
        # URL to fetch attendance data
        attendance_url = "https://academia.srmist.edu.in/srm_university/academia-academic-services/page/My_Attendance"
        response = self.session.get(attendance_url)

        if response.ok:
            return response.text  # Return HTML for parsing
        else:
            print("Unable to fetch attendance data:", response.status_code, response.text)
            return None

    def parse_attendance_data(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        attendance_data = {}

        # Assuming there's a table with attendance data
        table = soup.find('table')  # Adjust if needed
        if table:
            for row in table.find_all('tr')[1:]:  # Skip header
                cells = row.find_all('td')
                if len(cells) >= 4:
                    class_name = cells[0].text.strip()
                    total_classes = int(cells[1].text.strip())
                    classes_attended = int(cells[2].text.strip())
                    attendance_percentage = (classes_attended / total_classes) * 100

                    attendance_data[class_name] = {
                        'total_classes': total_classes,
                        'classes_attended': classes_attended,
                        'attendance_percentage': attendance_percentage,
                    }
        return attendance_data

    def calculate_attendance_metrics(self, attendance_data):
        results = {}
        for class_name, data in attendance_data.items():
            total_classes = data['total_classes']
            classes_attended = data['classes_attended']
            attendance_percentage = data['attendance_percentage']
            
            # Calculate attendance margin
            required_classes = max(0, (total_classes * 0.75) - classes_attended)
            can_miss_classes = max(0, classes_attended - (total_classes * 0.75) // 0.25)

            results[class_name] = {
                'attendance_percentage': attendance_percentage,
                'required_classes': required_classes,
                'can_miss_classes': can_miss_classes,
            }
        return results

# GUI for handling login and displaying attendance data
def main(page: ft.Page):
    page.title = "Attendance Fetcher"

    username_input = ft.TextField(label="Username", width=300)
    password_input = ft.TextField(label="Password", password=True, width=300)
    login_button = ft.ElevatedButton(text="Login", on_click=lambda e: login_action())
    result_area = ft.Column()

    def login_action():
        username = username_input.value
        password = password_input.value

        fetcher = AttendanceFetcher(username, password)

        if fetcher.login():
            attendance_html = fetcher.fetch_attendance()
            if attendance_html:
                attendance_data = fetcher.parse_attendance_data(attendance_html)
                attendance_results = fetcher.calculate_attendance_metrics(attendance_data)
                display_attendance(attendance_results)

    def display_attendance(data):
        result_area.controls.clear()  # Clear previous results
        # Display attendance information
        for class_name, metrics in data.items():
            if metrics['attendance_percentage'] < 75:
                color = ft.colors.RED
                requirement_text = f"Required Classes to Attend: {metrics['required_classes']}"
            else:
                color = ft.colors.GREEN
                requirement_text = f"Can Miss Classes: {metrics['can_miss_classes']}"
            
            result_area.controls.append(ft.Text(
                f"{class_name}: {metrics['attendance_percentage']:.2f}% - {requirement_text}",
                size=16,
                color=color
            ))

        page.update()

    # Layout
    page.add(
        ft.Column(
            controls=[
                username_input,
                password_input,
                login_button,
                result_area
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=True
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
