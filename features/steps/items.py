@when(u'I go to the homepage')
def step_impl(context):
    br = context.browser
    br.get('http://localhost:5000')

@then(u'I should see a question')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id('question')

@then(u'I should see three options')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_class_name('answer')

@then(u'I should see three unique answers')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_class_name('test')

    

# @when(u'I check the completed box')
# def step_impl(context):
#     br = context.browser
#     br.find_element_by_class_name("open_label").click()
#     br.find_element_by_class_name("completed_box").click()

# @then(u'I should see a strikethough through the item')
# def step_impl(context):
#     br = context.browser
#     assert br.find_element_by_class_name("closed")

# @when(u'I submit a blank form')
# def step_impl(context):
#     br = context.browser
#     br.find_element_by_id("submit").click()

# @then(u'I should see an error')
# def step_impl(context):
#     br = context.browser
#     assert br.find_element_by_class_name("alert-dismissable")
