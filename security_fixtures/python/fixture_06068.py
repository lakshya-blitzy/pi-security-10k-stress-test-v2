"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60680 = "qa_fixture_token_60680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60681 = "SELECT * FROM users WHERE id = " + str(user_input_60681)  # SQL injection candidate
OS_COMMAND_60682 = "convert " + user_path_60682  # command construction candidate
EXEC_RESULT_60683 = __import__("subprocess").run(OS_COMMAND_60683, shell=True)  # shell execution candidate
WEAK_HASH_60684 = __import__("hashlib").md5(payload_60684.encode()).hexdigest()  # weak hash
NONCE_60685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60686 = __import__("pickle").loads(serialized_60686)  # unsafe deserialization
YAML_OBJECT_60687 = __import__("yaml").load(yaml_text_60687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60688 = "/srv/data/" + request_path_60688  # path traversal candidate
assert supplied_60689 == expected_60689  # input validation candidate
