# Blinks

Lights

## Message Spec

Format: \<channel> "message"

### Inputs

* \<blinks.front> "on"
  * Turns the front LED on
* \<blinks.front> "off"
  * Turns the front LED off
* \<blinks.top> "on"
  * Turns the top LED on
* \<blinks.top> "off"
  * Turns the top LED off

### Outputs

* \<blinks.front.status> "front.on"
  * The front LED has switched on
* \<blinks.front.status> "front.off"
  * The front LED has switched off
* \<blinks.top.status> "top.on"
  * The top LED has switched on
* \<blinks.top.status> "top.off"
  * The top LED has switched off