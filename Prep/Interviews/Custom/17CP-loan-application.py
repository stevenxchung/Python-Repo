import json
import re
from collections import defaultdict

# Email regex reference
# [^@]+@[^@]+\.[^@]+ -> re.match(r'[^@]+@[^@]+\.[^@]+', email) -> returns bool


class ApplicationEvaluator:
    def evaluateApplications(self, testInput):
        "your code here"
        income_map = defaultdict(int)
        for income in income_sources:
            if income.periodType == IncomePeriodType.Monthly:
                income_map[income.userId] += income.grossIncome
            elif income.periodType == IncomePeriodType.Yearly:
                income_map[income.userId] += income.grossIncome / 12

        accepted_app = []
        rejected_app = defaultdict(list)
        for i, app in enumerate(applications):
            # Reject
            if app.userId not in income_map:
                rejected_app[app.applicationId].append(
                    RejectionReason.IncomeRentRatioNotMet
                )
            elif app.userId in income_map:
                # Monthly | Yearly
                total_monthy_income = income_map[app.userId]
                ratio = total_monthy_income / landlord_requirements.monthlyRent
                if ratio < landlord_requirements.minimumIncomeToRentRatio:
                    rejected_app[app.applicationId].append(
                        RejectionReason.IncomeRentRatioNotMet
                    )

            if not (300 <= app.creditScore <= 850):
                rejected_app[app.applicationId].append(
                    RejectionReason.InvalidCreditScoreRange
                )
            if app.creditScore < landlord_requirements.minimumCreditScore:
                rejected_app[app.applicationId].append(
                    RejectionReason.MinimumCreditScoreNotMet
                )
            if app.email is None or len(app.email) == 0:
                rejected_app[app.applicationId].append(
                    RejectionReason.NullOrEmptyEmail
                )
            if not re.match(r"[^@]+@[^@]+\.[^@]+", app.email):
                rejected_app[app.applicationId].append(
                    RejectionReason.InvalidEmailFormat
                )

            # Accept
            if app.applicationId not in rejected_app:
                accepted_app.append(app.applicationId)

        return ApplicationEvaluatorResponse(accepted_app, rejected_app)


class Application:
    def __init__(
        self,
        applicationId=None,
        firstName=None,
        lastName=None,
        email=None,
        phoneNumber=None,
        userId=None,
        creditScore=None,
    ):
        self.applicationId = applicationId
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phoneNumber = phoneNumber
        self.userId = userId
        self.creditScore = creditScore


class ApplicationEvaluatorResponse:
    def __init__(self, acceptableApplications, rejectedApplicationReasons):
        self.acceptableApplications = (
            acceptableApplications  # list/set of applicationIds
        )
        # map of applicationId -> list/set of RejectionReasons
        self.rejectedApplicationReasons = rejectedApplicationReasons


class IncomePeriodType:
    Monthly = "Monthly"
    Yearly = "Yearly"


class IncomeSource:
    def __init__(
        self,
        title=None,
        employer=None,
        grossIncome=None,
        netIncome=None,
        startDate=None,
        endDate=None,
        userId=None,
        periodType=None,
    ):
        self.title = title
        self.employer = employer
        self.grossIncome = grossIncome
        self.netIncome = netIncome
        self.startDate = startDate
        self.endDate = endDate
        self.userId = userId
        self.periodType = periodType  # IncomePeriodType


class LandlordRequirements:
    def __init__(
        self,
        monthlyRent=None,
        minimumIncomeToRentRatio=None,
        minimumCreditScore=None,
    ):
        self.monthlyRent = monthlyRent
        self.minimumIncomeToRentRatio = minimumIncomeToRentRatio
        self.minimumCreditScore = minimumCreditScore


class TestInput:
    def __init__(self, applications, incomeSources, landlordRequirements):
        self.applications = applications  # list of Application objects
        self.incomeSources = incomeSources  # list of IncomeSource objects
        self.landlordRequirements = (
            landlordRequirements  # LandlordRequirements object
        )


class RejectionReason:
    IncomeRentRatioNotMet = "IncomeRentRatioNotMet"
    InvalidCreditScoreRange = "InvalidCreditScoreRange"
    InvalidEmailFormat = "InvalidEmailFormat"
    NullOrEmptyEmail = "NullOrEmptyEmail"
    NullOrEmptyFirstName = "NullOrEmptyFirstName"
    NullOrEmptyLastName = "NullOrEmptyLastName"
    NullOrEmptyPhoneNumber = "NullOrEmptyPhoneNumber"
    MinimumCreditScoreNotMet = "MinimumCreditScoreNotMet"


def default(obj):
    if isinstance(obj, dict):
        return dict(obj)
    elif isinstance(obj, set):
        return sorted(list(obj))
    elif isinstance(obj, list):
        return sorted(obj)
    else:
        return obj


if __name__ == "__main__":
    # input_data = json.loads(sys.stdin.read())
    input_data = {
        "applications": [
            {
                "applicationId": 1,
                "firstName": "John",
                "lastName": "Doe",
                "email": "john.doe@example.com",
                "phoneNumber": "555-1234",
                "userId": 1001,
                "creditScore": 720,
            },
            {
                "applicationId": 2,
                "firstName": "Jane",
                "lastName": "Smith",
                "email": "jane.smith@example",
                "phoneNumber": "555-5678",
                "userId": 1002,
                "creditScore": 680,
            },
            {
                "applicationId": 3,
                "firstName": "",
                "lastName": "Brown",
                "email": "mike.brown@example.com",
                "phoneNumber": "555-8765",
                "userId": 1003,
                "creditScore": 650,
            },
            {
                "applicationId": 4,
                "firstName": "Emily",
                "lastName": "Davis",
                "email": "emily.davis@example.com",
                "phoneNumber": "",
                "userId": 1004,
                "creditScore": 630,
            },
            {
                "applicationId": 5,
                "firstName": "Chris",
                "lastName": "Wilson",
                "email": "chris.wilson@example.com",
                "phoneNumber": "555-4321",
                "userId": 1005,
                "creditScore": 590,
            },
        ],
        "incomeSources": [
            {
                "title": "Software Engineer",
                "employer": "Tech Corp",
                "grossIncome": 90000,
                "netIncome": 70000,
                "startDate": "2020-01-15",
                "endDate": None,
                "userId": 1001,
                "periodType": "Yearly",
            },
            {
                "title": "Marketing Manager",
                "employer": "Market Inc",
                "grossIncome": 60000,
                "netIncome": 50000,
                "startDate": "2019-05-20",
                "endDate": None,
                "userId": 1002,
                "periodType": "Yearly",
            },
            {
                "title": "Sales Associate",
                "employer": "Sales LLC",
                "grossIncome": 3500,
                "netIncome": 3000,
                "startDate": "2021-09-01",
                "endDate": None,
                "userId": 1003,
                "periodType": "Monthly",
            },
            {
                "title": "Graphic Designer",
                "employer": "Design Studio",
                "grossIncome": 4000,
                "netIncome": 3200,
                "startDate": "2022-03-10",
                "endDate": None,
                "userId": 1004,
                "periodType": "Monthly",
            },
            {
                "title": "Barista",
                "employer": "Coffee Shop",
                "grossIncome": 2500,
                "netIncome": 2000,
                "startDate": "2021-11-25",
                "endDate": None,
                "userId": 1005,
                "periodType": "Monthly",
            },
        ],
        "landlordRequirements": {
            "monthlyRent": 2000,
            "minimumIncomeToRentRatio": 3.0,
            "minimumCreditScore": 650,
        },
    }
    applications = list(
        map(lambda x: Application(**x), input_data["applications"])
    )
    income_sources = list(
        map(lambda x: IncomeSource(**x), input_data["incomeSources"])
    )
    landlord_requirements = LandlordRequirements(
        **input_data["landlordRequirements"]
    )
    test_input = TestInput(applications, income_sources, landlord_requirements)

    # Test input data
    test = ApplicationEvaluator()
    response = test.evaluateApplications(test_input)

    # Convert response to a JSON-friendly format
    def serialize_response(response):
        return {
            "acceptableApplications": response.acceptableApplications,
            "rejectedApplicationReasons": {
                appId: list(reasons)
                for appId, reasons in response.rejectedApplicationReasons.items()
            },
        }

    response_json = json.dumps(serialize_response(response), indent=4)
    print(response_json)
