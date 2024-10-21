from bs4 import BeautifulSoup

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
