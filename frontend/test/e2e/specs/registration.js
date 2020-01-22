// For authoring Nightwatch tests, see
// http://nightwatchjs.org/guide#usage

module.exports = {
  'Resgistration test': function (browser) {
    // automatically uses dev Server port from /config.index.js
    // default: http://localhost:8080
    // see nightwatch.conf.js
    const devServer = browser.globals.devServerURL

    browser
      .url(devServer + '/register')
      .waitForElementVisible('#somewebapp', 5000)
      .assert.elementPresent('.title')
      .assert.containsText('h2', 'Register')
      .setValue('input[id="username"]', 'Some User')
      .pause(1000)
      .setValue('input[id="email"]', 'someuser@somewebapp.kz')
      .pause(1000)
      .setValue('input[id="phone-number"]', '+71234567890')
      .pause(1000)
      .click('#role')
      .waitForElementVisible("option[value='2']", 1000)
      .click("option[value='2']")
      .pause(1000)
      .setValue('input[id="password"]', '123456')
      .pause(1000)
      .setValue('input[id="repeat-password"]', '123456')
      .pause(1000)
      .click('button[id="submit-registration-button"]')
      .waitForElementVisible('.toasted', 1000)
      .assert.elementPresent('.toasted')
      .assert.containsText('.toasted', 'Registration Complete')
      .pause(10000)
      .end()
  }
}
