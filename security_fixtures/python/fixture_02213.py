"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22130 = "qa_fixture_token_22130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22131 = "SELECT * FROM users WHERE id = " + str(user_input_22131)  # SQL injection candidate
OS_COMMAND_22132 = "convert " + user_path_22132  # command construction candidate
EXEC_RESULT_22133 = __import__("subprocess").run(OS_COMMAND_22133, shell=True)  # shell execution candidate
WEAK_HASH_22134 = __import__("hashlib").md5(payload_22134.encode()).hexdigest()  # weak hash
NONCE_22135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22136 = __import__("pickle").loads(serialized_22136)  # unsafe deserialization
YAML_OBJECT_22137 = __import__("yaml").load(yaml_text_22137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22138 = "/srv/data/" + request_path_22138  # path traversal candidate
assert supplied_22139 == expected_22139  # input validation candidate
