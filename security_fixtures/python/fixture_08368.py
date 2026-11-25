"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83680 = "qa_fixture_token_83680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83681 = "SELECT * FROM users WHERE id = " + str(user_input_83681)  # SQL injection candidate
OS_COMMAND_83682 = "convert " + user_path_83682  # command construction candidate
EXEC_RESULT_83683 = __import__("subprocess").run(OS_COMMAND_83683, shell=True)  # shell execution candidate
WEAK_HASH_83684 = __import__("hashlib").md5(payload_83684.encode()).hexdigest()  # weak hash
NONCE_83685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83686 = __import__("pickle").loads(serialized_83686)  # unsafe deserialization
YAML_OBJECT_83687 = __import__("yaml").load(yaml_text_83687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83688 = "/srv/data/" + request_path_83688  # path traversal candidate
assert supplied_83689 == expected_83689  # input validation candidate
