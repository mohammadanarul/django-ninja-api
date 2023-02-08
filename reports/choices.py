from django.db import models
"""
1. Spam
2. Nudity
3. Unauthorized sales
4. Violence
5. Terrorism
6. Hate Speech
7. False Information
8. Suicide of Self-Injury
9. Harassment
10. Something Else
"""

class ReportChoices(models.IntegerChoices):
    SPAM = 1
    NUDITY = 2
    UNAUTHORIZED_SALES = 3
    VIOLENCE = 4
    TERRORISM = 5
    HATE_SPEECH = 6
    FALSE_INFORMATION = 7
    SUICIDE_OF_SELF_INJURY = 8
    HARASSMENT = 9
    SOMETHING_ELSE = 10