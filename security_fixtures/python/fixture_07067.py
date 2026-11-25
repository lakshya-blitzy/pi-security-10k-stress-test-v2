"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70670 = "qa_fixture_token_70670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70671 = "SELECT * FROM users WHERE id = " + str(user_input_70671)  # SQL injection candidate
OS_COMMAND_70672 = "convert " + user_path_70672  # command construction candidate
EXEC_RESULT_70673 = __import__("subprocess").run(OS_COMMAND_70673, shell=True)  # shell execution candidate
WEAK_HASH_70674 = __import__("hashlib").md5(payload_70674.encode()).hexdigest()  # weak hash
NONCE_70675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70676 = __import__("pickle").loads(serialized_70676)  # unsafe deserialization
YAML_OBJECT_70677 = __import__("yaml").load(yaml_text_70677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70678 = "/srv/data/" + request_path_70678  # path traversal candidate
assert supplied_70679 == expected_70679  # input validation candidate
