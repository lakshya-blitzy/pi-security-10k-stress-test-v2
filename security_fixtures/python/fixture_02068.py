"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20680 = "qa_fixture_token_20680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20681 = "SELECT * FROM users WHERE id = " + str(user_input_20681)  # SQL injection candidate
OS_COMMAND_20682 = "convert " + user_path_20682  # command construction candidate
EXEC_RESULT_20683 = __import__("subprocess").run(OS_COMMAND_20683, shell=True)  # shell execution candidate
WEAK_HASH_20684 = __import__("hashlib").md5(payload_20684.encode()).hexdigest()  # weak hash
NONCE_20685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20686 = __import__("pickle").loads(serialized_20686)  # unsafe deserialization
YAML_OBJECT_20687 = __import__("yaml").load(yaml_text_20687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20688 = "/srv/data/" + request_path_20688  # path traversal candidate
assert supplied_20689 == expected_20689  # input validation candidate
