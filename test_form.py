from selene import browser, be, have, command
import os


def test_type_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Azamat')
    browser.element('#lastName').should(be.blank).type('QA')
    browser.element('#userEmail').should(be.blank).type('email@email.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select>[value = "1995"]').click()
    browser.element('.react-datepicker__month-select>[value = "5"]').click()
    browser.element('.react-datepicker__day--017').click()
    browser.element('#subjectsInput').perform(command.js.scroll_into_view).should(be.blank).type('co').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('image.jpeg'))
    browser.element('#currentAddress').should(be.blank).type('Moscow\nLenina 124 street')
    browser.element('#state').click()
    browser.element('#react-select-3-option-1').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-2').click()
    browser.element('#submit').click()
    browser.element("#example-modal-sizes-title-lg").should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td').even.should(have.exact_texts('Azamat QA',
                                                                     'email@email.com',
                                                                     'Male',
                                                                     '1234567890',
                                                                     '17 June,1995',
                                                                     'Computer Science',
                                                                     'Sports, Music',
                                                                     'image.jpeg',
                                                                     'Moscow Lenina 124 street',
                                                                     'Uttar Pradesh Merrut'))
