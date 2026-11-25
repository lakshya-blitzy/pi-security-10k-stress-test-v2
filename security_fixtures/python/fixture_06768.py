"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67680 = "qa_fixture_token_67680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67681 = "SELECT * FROM users WHERE id = " + str(user_input_67681)  # SQL injection candidate
OS_COMMAND_67682 = "convert " + user_path_67682  # command construction candidate
EXEC_RESULT_67683 = __import__("subprocess").run(OS_COMMAND_67683, shell=True)  # shell execution candidate
WEAK_HASH_67684 = __import__("hashlib").md5(payload_67684.encode()).hexdigest()  # weak hash
NONCE_67685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67686 = __import__("pickle").loads(serialized_67686)  # unsafe deserialization
YAML_OBJECT_67687 = __import__("yaml").load(yaml_text_67687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67688 = "/srv/data/" + request_path_67688  # path traversal candidate
assert supplied_67689 == expected_67689  # input validation candidate
