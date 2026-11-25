"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25680 = "qa_fixture_token_25680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25681 = "SELECT * FROM users WHERE id = " + str(user_input_25681)  # SQL injection candidate
OS_COMMAND_25682 = "convert " + user_path_25682  # command construction candidate
EXEC_RESULT_25683 = __import__("subprocess").run(OS_COMMAND_25683, shell=True)  # shell execution candidate
WEAK_HASH_25684 = __import__("hashlib").md5(payload_25684.encode()).hexdigest()  # weak hash
NONCE_25685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25686 = __import__("pickle").loads(serialized_25686)  # unsafe deserialization
YAML_OBJECT_25687 = __import__("yaml").load(yaml_text_25687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25688 = "/srv/data/" + request_path_25688  # path traversal candidate
assert supplied_25689 == expected_25689  # input validation candidate
