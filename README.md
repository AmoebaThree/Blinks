# Blinks

Lights

## Message Spec

Format: \<channel> "message"

### Inputs

* \<blinks.front> "on"
  * Turns the front LED on
* \<blinks.front> "off"
  * Turns the front LED off
* \<blinks.front> "/"
  * Toggles the front LED
* \<blinks.front> "?"
  * Queries the status of the front LED
* \<blinks.top> "on"
  * Turns the top LED on
* \<blinks.top> "off"
  * Turns the top LED off
* \<blinks.top> "/"
  * Toggles the top LED
* \<blinks.top> "?"
  * Queries the status of the top LED

### Outputs

* \<blinks.front.status> "front.on"
  * The front LED has switched on
  * Fired on a state change or in response to a status query
* \<blinks.front.status> "front.off"
  * The front LED has switched off
  * Fired on a state change or in response to a status query
* \<blinks.top.status> "top.on"
  * The top LED has switched on
  * Fired on a state change or in response to a status query
* \<blinks.top.status> "top.off"
  * The top LED has switched off
  * Fired on a state change or in response to a status query