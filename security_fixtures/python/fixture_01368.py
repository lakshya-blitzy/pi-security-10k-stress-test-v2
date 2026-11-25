"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13680 = "qa_fixture_token_13680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13681 = "SELECT * FROM users WHERE id = " + str(user_input_13681)  # SQL injection candidate
OS_COMMAND_13682 = "convert " + user_path_13682  # command construction candidate
EXEC_RESULT_13683 = __import__("subprocess").run(OS_COMMAND_13683, shell=True)  # shell execution candidate
WEAK_HASH_13684 = __import__("hashlib").md5(payload_13684.encode()).hexdigest()  # weak hash
NONCE_13685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13686 = __import__("pickle").loads(serialized_13686)  # unsafe deserialization
YAML_OBJECT_13687 = __import__("yaml").load(yaml_text_13687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13688 = "/srv/data/" + request_path_13688  # path traversal candidate
assert supplied_13689 == expected_13689  # input validation candidate
