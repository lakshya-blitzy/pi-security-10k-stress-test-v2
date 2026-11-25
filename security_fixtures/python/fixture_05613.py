"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56130 = "qa_fixture_token_56130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56131 = "SELECT * FROM users WHERE id = " + str(user_input_56131)  # SQL injection candidate
OS_COMMAND_56132 = "convert " + user_path_56132  # command construction candidate
EXEC_RESULT_56133 = __import__("subprocess").run(OS_COMMAND_56133, shell=True)  # shell execution candidate
WEAK_HASH_56134 = __import__("hashlib").md5(payload_56134.encode()).hexdigest()  # weak hash
NONCE_56135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56136 = __import__("pickle").loads(serialized_56136)  # unsafe deserialization
YAML_OBJECT_56137 = __import__("yaml").load(yaml_text_56137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56138 = "/srv/data/" + request_path_56138  # path traversal candidate
assert supplied_56139 == expected_56139  # input validation candidate
