"""
Sample demonstration of else with try..catch..finally construct.


Author: GAN MOHIM.
"""
def lock_house():
    print("Locking house")
    return True


def secure_house():
    try:
        print("Securing house...")
        raise Exception("Something went wrong")
    except Exception as e:
        print("WARNING: Unable to secure house")
        print("Exception: {}".format(e))
    else:
        return lock_house()
    finally:
        print("Closing opened channels finally...")


if __name__ == "__main__":
    security_flag = secure_house()
    print("Is house secured: {}".format("Yes" if security_flag else "No"))
