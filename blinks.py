import systemd.daemon
import redis


def execute():
    print('Startup')

    top_output = '6'
    front_output = '7'
    top_pfd_channel = 'pfd.output.' + top_output
    front_pfd_channel = 'pfd.output.' + front_output
    top_channel_status = top_pfd_channel + '.status'
    front_channel_status = front_pfd_channel + '.status'
    top_channel_on = 'output.' + top_output + '.on'
    top_channel_off = 'output.' + top_output + '.off'
    front_channel_on = 'output.' + front_output + '.on'
    front_channel_off = 'output.' + front_output + '.off'
    top_request_channel = 'blinks.top'
    front_request_channel = 'blinks.front'

    cmd_on = 'on'
    cmd_off = 'off'
    cmd_toggle = '/'
    cmd_query = '?'

    r = redis.Redis(host='192.168.0.1', port=6379,
                    db=0, decode_responses=True)
    p = r.pubsub(ignore_subscribe_messages=True)
    p.subscribe(top_request_channel, front_request_channel,
                top_channel_status, front_channel_status)

    r.publish('services', 'blinks.on')
    systemd.daemon.notify('READY=1')
    print('Startup complete')

    try:
        r.publish(top_pfd_channel, '?')
        r.publish(front_pfd_channel, '?')

        for message in p.listen():
            if message['channel'] == top_request_channel:
                if message['data'] == cmd_on:
                    r.publish(top_pfd_channel, 'on')
                elif message['data'] == cmd_off:
                    r.publish(top_pfd_channel, 'off')
                elif message['data'] == cmd_toggle:
                    r.publish(top_pfd_channel, '/')
                elif message['data'] == cmd_query:
                    r.publish(top_pfd_channel, '?')

            elif message['channel'] == front_request_channel:
                if message['data'] == cmd_on:
                    r.publish(front_pfd_channel, 'on')
                elif message['data'] == cmd_off:
                    r.publish(front_pfd_channel, 'off')
                elif message['data'] == cmd_toggle:
                    r.publish(front_pfd_channel, '/')
                elif message['data'] == cmd_query:
                    r.publish(front_pfd_channel, '?')

            elif message['channel'] == top_channel_status:
                if message['data'] == top_channel_on:
                    r.publish('blinks.front.status', 'front.on')
                elif message['data'] == top_channel_off:
                    r.publish('blinks.front.status', 'front.off')

            elif message['channel'] == front_channel_status:
                if message['data'] == front_channel_on:
                    r.publish('blinks.top.status', 'top.on')
                elif message['data'] == front_channel_off:
                    r.publish('blinks.top.status', 'top.off')
    except:
        p.close()
        r.publish('services', 'blinks.off')
        print('Goodbye')


if __name__ == '__main__':
    execute()
