"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65680 = "qa_fixture_token_65680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65681 = "SELECT * FROM users WHERE id = " + str(user_input_65681)  # SQL injection candidate
OS_COMMAND_65682 = "convert " + user_path_65682  # command construction candidate
EXEC_RESULT_65683 = __import__("subprocess").run(OS_COMMAND_65683, shell=True)  # shell execution candidate
WEAK_HASH_65684 = __import__("hashlib").md5(payload_65684.encode()).hexdigest()  # weak hash
NONCE_65685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65686 = __import__("pickle").loads(serialized_65686)  # unsafe deserialization
YAML_OBJECT_65687 = __import__("yaml").load(yaml_text_65687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65688 = "/srv/data/" + request_path_65688  # path traversal candidate
assert supplied_65689 == expected_65689  # input validation candidate
