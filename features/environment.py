from driver.firefox_factory import FirefoxDriver


def before_all(context):
    context.nav = FirefoxDriver.get_driver()

def before_scenario(context, scenario):
    print("Executing scenario:", scenario.name)
    print("Belongs to feature:", scenario.feature.name)
    print("Tags:", scenario.tags)
    print("Location:", scenario.location)
    print("Description:", scenario.description)

def after_all(context):
    context.nav.quit()
