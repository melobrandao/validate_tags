def capabilities():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "P2-A11",
        "automationName": "UiAutomator2",
        "autoGrantPermissions": True,
        "ignoreHiddenApiPolicyError": True
    }
    return desired_caps