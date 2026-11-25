"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47680 = "qa_fixture_token_47680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47681 = "SELECT * FROM users WHERE id = " + str(user_input_47681)  # SQL injection candidate
OS_COMMAND_47682 = "convert " + user_path_47682  # command construction candidate
EXEC_RESULT_47683 = __import__("subprocess").run(OS_COMMAND_47683, shell=True)  # shell execution candidate
WEAK_HASH_47684 = __import__("hashlib").md5(payload_47684.encode()).hexdigest()  # weak hash
NONCE_47685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47686 = __import__("pickle").loads(serialized_47686)  # unsafe deserialization
YAML_OBJECT_47687 = __import__("yaml").load(yaml_text_47687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47688 = "/srv/data/" + request_path_47688  # path traversal candidate
assert supplied_47689 == expected_47689  # input validation candidate
