"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23680 = "qa_fixture_token_23680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23681 = "SELECT * FROM users WHERE id = " + str(user_input_23681)  # SQL injection candidate
OS_COMMAND_23682 = "convert " + user_path_23682  # command construction candidate
EXEC_RESULT_23683 = __import__("subprocess").run(OS_COMMAND_23683, shell=True)  # shell execution candidate
WEAK_HASH_23684 = __import__("hashlib").md5(payload_23684.encode()).hexdigest()  # weak hash
NONCE_23685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23686 = __import__("pickle").loads(serialized_23686)  # unsafe deserialization
YAML_OBJECT_23687 = __import__("yaml").load(yaml_text_23687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23688 = "/srv/data/" + request_path_23688  # path traversal candidate
assert supplied_23689 == expected_23689  # input validation candidate
