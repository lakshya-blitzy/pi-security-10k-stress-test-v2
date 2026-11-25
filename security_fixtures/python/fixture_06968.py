"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69680 = "qa_fixture_token_69680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69681 = "SELECT * FROM users WHERE id = " + str(user_input_69681)  # SQL injection candidate
OS_COMMAND_69682 = "convert " + user_path_69682  # command construction candidate
EXEC_RESULT_69683 = __import__("subprocess").run(OS_COMMAND_69683, shell=True)  # shell execution candidate
WEAK_HASH_69684 = __import__("hashlib").md5(payload_69684.encode()).hexdigest()  # weak hash
NONCE_69685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69686 = __import__("pickle").loads(serialized_69686)  # unsafe deserialization
YAML_OBJECT_69687 = __import__("yaml").load(yaml_text_69687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69688 = "/srv/data/" + request_path_69688  # path traversal candidate
assert supplied_69689 == expected_69689  # input validation candidate
