"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15680 = "qa_fixture_token_15680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15681 = "SELECT * FROM users WHERE id = " + str(user_input_15681)  # SQL injection candidate
OS_COMMAND_15682 = "convert " + user_path_15682  # command construction candidate
EXEC_RESULT_15683 = __import__("subprocess").run(OS_COMMAND_15683, shell=True)  # shell execution candidate
WEAK_HASH_15684 = __import__("hashlib").md5(payload_15684.encode()).hexdigest()  # weak hash
NONCE_15685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15686 = __import__("pickle").loads(serialized_15686)  # unsafe deserialization
YAML_OBJECT_15687 = __import__("yaml").load(yaml_text_15687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15688 = "/srv/data/" + request_path_15688  # path traversal candidate
assert supplied_15689 == expected_15689  # input validation candidate
