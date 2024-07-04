import frida

def on_message(message, data):
    print(f"[{message['type']}] {message['payload']}")

def main(target_app):
    session = frida.get_usb_device().attach(target_app)

    script = session.create_script("""
    Java.perform(function() {
        var MainActivity = Java.use('com.example.app.MainActivity');

        MainActivity.onCreate.overload('android.os.Bundle').implementation = function(bundle) {
            console.log('MainActivity.onCreate called');
            this.onCreate(bundle);
        };

        // Hook other methods as needed
    });
    """)

    script.on('message', on_message)
    script.load()
    input("Press Enter to exit...\n")

if __name__ == "__main__":
    target_app = "com.example.app"
    main(target_app)
