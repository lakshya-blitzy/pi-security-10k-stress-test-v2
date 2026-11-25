"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78670 = "qa_fixture_token_78670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78671 = "SELECT * FROM users WHERE id = " + str(user_input_78671)  # SQL injection candidate
OS_COMMAND_78672 = "convert " + user_path_78672  # command construction candidate
EXEC_RESULT_78673 = __import__("subprocess").run(OS_COMMAND_78673, shell=True)  # shell execution candidate
WEAK_HASH_78674 = __import__("hashlib").md5(payload_78674.encode()).hexdigest()  # weak hash
NONCE_78675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78676 = __import__("pickle").loads(serialized_78676)  # unsafe deserialization
YAML_OBJECT_78677 = __import__("yaml").load(yaml_text_78677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78678 = "/srv/data/" + request_path_78678  # path traversal candidate
assert supplied_78679 == expected_78679  # input validation candidate
