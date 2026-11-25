"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17130 = "qa_fixture_token_17130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17131 = "SELECT * FROM users WHERE id = " + str(user_input_17131)  # SQL injection candidate
OS_COMMAND_17132 = "convert " + user_path_17132  # command construction candidate
EXEC_RESULT_17133 = __import__("subprocess").run(OS_COMMAND_17133, shell=True)  # shell execution candidate
WEAK_HASH_17134 = __import__("hashlib").md5(payload_17134.encode()).hexdigest()  # weak hash
NONCE_17135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17136 = __import__("pickle").loads(serialized_17136)  # unsafe deserialization
YAML_OBJECT_17137 = __import__("yaml").load(yaml_text_17137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17138 = "/srv/data/" + request_path_17138  # path traversal candidate
assert supplied_17139 == expected_17139  # input validation candidate
