# ruff: noqa: T201
import os

from ..utils.slack.send_only import send_text


def check_one_env(env_var):
    value = os.environ.get(env_var)
    if value is None:
        print(f"🤢 Please set the environment variable {env_var}.")
        return False
    print(f"✅ {env_var} is set to {value}")
    return True


def check_many_env(env_vars):
    ret = True
    for env_var in env_vars:
        if not check_one_env(env_var):
            ret = False
    return ret


def check_env():
    return check_many_env(["SLACK_BOT_TOKEN", "SLACK_APP_TOKEN", "SLACK_CHANNEL_ID"])


def check_send_text():
    print("🚀 Sending a test message to the Slack channel...")
    response = send_text("💪 Checking health of the Slack bot.")

    if response is None:
        print("🤢 The response is None.")
        return False

    if response["ok"]:
        print("✅ The message was sent successfully.")
        return True

    print(f"🤢 The message was not sent successfully. Response: {response}")
    return False
