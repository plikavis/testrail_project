import allure
from allure_commons._allure import step
from testrail_project_test.pages.case_page import case
from tests.conftest import api_add_project, api_delete_project


@allure.title("Try empty case and check message")
@allure.tag("UI", "regress")
@allure.feature("Cases")
@allure.label("owner", "Vishnyakova P.")
@allure.story("UI: Adding interface for cases")
@allure.step("UI: Try create test case with empty name")
def test_try_add_empty_test_case(browser_config_ui, auth):
    with step(f"Go to cases page for project with id - 377"):
        case.open_cases_page(377)
    with step("Click 'Add case' button"):
        case.click_add_case_button()
    with step("Click 'Add and next' button"):
        case.click_add_next_button()
    with step("Check message about fail"):
        case.check_message_fail()


@allure.title("Add new test case")
@allure.tag("UI", "Smoke")
@allure.feature("Cases")
@allure.label("owner", "Vishnyakova P.")
@allure.story("UI: Adding interface for cases")
@allure.step("UI: Add new test case")
def test_add_test_case_successfully(browser_config_ui, auth):
    with allure.step("Create new project and get its id"):
        project_id = api_add_project(name="for add case 21",
                                     announcement="announcement for add case",
                                     show_announcement=True,
                                     suite_mode=1)
    with allure.step(f"Go to cases page for project with id - {project_id}"):
        case.open_cases_page(project_id)
    with allure.step("Click 'Add case' button"):
        case.click_add_case_button()
    with allure.step("Input case's name "):
        case.input_case_name_for_add()
    with allure.step("Click create button"):
        case.click_add_case_button_for_create()
    with allure.step("Check message about success"):
        case.check_message_create_success()
    with allure.step(f"Delete case with id - {project_id}"):
        api_delete_project(project_id=project_id)


@allure.title("Edit name of test case and save")
@allure.tag("API", "regress")
@allure.feature("Cases")
@allure.label("owner", "Vishnyakova P.")
@allure.story("UI: Adding interface for cases")
@allure.step("UI: Edit test case")
def test_edit_test_case(browser_config_ui, auth):
    with allure.step("Open case card in First project"):
        case.open_case_card()
    with allure.step("Click edit button"):
        case.click_edit_case_button()
    with allure.step("Input new case's name"):
        case.input_case_name_for_edit()
    with allure.step("Click Save Title button"):
        case.click_save_button()
    with allure.step("Check success message"):
        case.check_message_edit_success()
