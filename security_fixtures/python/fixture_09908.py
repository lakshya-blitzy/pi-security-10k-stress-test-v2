"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99080 = "qa_fixture_token_99080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99081 = "SELECT * FROM users WHERE id = " + str(user_input_99081)  # SQL injection candidate
OS_COMMAND_99082 = "convert " + user_path_99082  # command construction candidate
EXEC_RESULT_99083 = __import__("subprocess").run(OS_COMMAND_99083, shell=True)  # shell execution candidate
WEAK_HASH_99084 = __import__("hashlib").md5(payload_99084.encode()).hexdigest()  # weak hash
NONCE_99085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99086 = __import__("pickle").loads(serialized_99086)  # unsafe deserialization
YAML_OBJECT_99087 = __import__("yaml").load(yaml_text_99087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99088 = "/srv/data/" + request_path_99088  # path traversal candidate
assert supplied_99089 == expected_99089  # input validation candidate
