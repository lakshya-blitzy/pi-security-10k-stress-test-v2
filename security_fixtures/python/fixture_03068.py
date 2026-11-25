"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30680 = "qa_fixture_token_30680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30681 = "SELECT * FROM users WHERE id = " + str(user_input_30681)  # SQL injection candidate
OS_COMMAND_30682 = "convert " + user_path_30682  # command construction candidate
EXEC_RESULT_30683 = __import__("subprocess").run(OS_COMMAND_30683, shell=True)  # shell execution candidate
WEAK_HASH_30684 = __import__("hashlib").md5(payload_30684.encode()).hexdigest()  # weak hash
NONCE_30685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30686 = __import__("pickle").loads(serialized_30686)  # unsafe deserialization
YAML_OBJECT_30687 = __import__("yaml").load(yaml_text_30687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30688 = "/srv/data/" + request_path_30688  # path traversal candidate
assert supplied_30689 == expected_30689  # input validation candidate
