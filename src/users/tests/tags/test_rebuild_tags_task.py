import pytest

from users import tasks

pytestmark = [
    pytest.mark.django_db,
]


@pytest.fixture(autouse=True)
def update_subscription(mocker):
    return mocker.patch("app.tasks.update_dashamail_subscription.delay")


@pytest.fixture(autouse=True)
def apply_tags(mocker):
    return mocker.patch("users.tasks.apply_tags")


def test_task(user, apply_tags, update_subscription):
    tasks.rebuild_tags.delay(
        student_id=user.id,
        list_id="1",
    )

    apply_tags.assert_called_once_with(user)
    update_subscription.assert_called_once_with(
        list_id="1",
        user_id=user.pk,
    )
