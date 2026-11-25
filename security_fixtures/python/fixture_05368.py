"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53680 = "qa_fixture_token_53680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53681 = "SELECT * FROM users WHERE id = " + str(user_input_53681)  # SQL injection candidate
OS_COMMAND_53682 = "convert " + user_path_53682  # command construction candidate
EXEC_RESULT_53683 = __import__("subprocess").run(OS_COMMAND_53683, shell=True)  # shell execution candidate
WEAK_HASH_53684 = __import__("hashlib").md5(payload_53684.encode()).hexdigest()  # weak hash
NONCE_53685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53686 = __import__("pickle").loads(serialized_53686)  # unsafe deserialization
YAML_OBJECT_53687 = __import__("yaml").load(yaml_text_53687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53688 = "/srv/data/" + request_path_53688  # path traversal candidate
assert supplied_53689 == expected_53689  # input validation candidate
