import logging

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from ui.Ui_Preferences import Ui_PreferencesDialog


def _bool(settings, directive, fallback):
    value = settings.value(directive)

    if isinstance(value, bool):
        return value

    logging.debug(f"_bool(): {directive!r} is {value!r}")

    if value == "true":
        return True
    elif value == "false":
        return False

    return fallback


class PreferencesDialog(QDialog, Ui_PreferencesDialog):
    def __init__(self, settings, parent=None):
        super(PreferencesDialog, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.settings = settings
        self.readSettings()

        self.accepted.connect(self.saveSettings)

    def readSettings(self):
        s = self.settings

        self.startOnLoginCheckBox.setChecked(_bool(s, "preferences/startup", False))
        self.copyLinkToClipboardCheckBox.setChecked(
           _bool(s, "preferences/copyToClipboard", True))
        self.showUploadCompleteNotificationCheckBox.setChecked(
            _bool(s, "preferences/showNotification", True))
        self.openLinkInBrowserCheckBox.setChecked(
            _bool(s, "preferences/openInBrowser", False))

    def saveSettings(self):
        s = self.settings

        s.setValue("preferences/startup", self.startOnLoginCheckBox.isChecked())
        s.setValue("preferences/copyToClipboard", self.copyLinkToClipboardCheckBox.isChecked())
        s.setValue("preferences/showNotification",
                   self.showUploadCompleteNotificationCheckBox.isChecked())
        s.setValue("preferences/openInBrowser", self.openLinkInBrowserCheckBox.isChecked())
