"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8560 = "qa_fixture_token_8560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8561 = "SELECT * FROM users WHERE id = " + str(user_input_8561)  # SQL injection candidate
OS_COMMAND_8562 = "convert " + user_path_8562  # command construction candidate
EXEC_RESULT_8563 = __import__("subprocess").run(OS_COMMAND_8563, shell=True)  # shell execution candidate
WEAK_HASH_8564 = __import__("hashlib").md5(payload_8564.encode()).hexdigest()  # weak hash
NONCE_8565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8566 = __import__("pickle").loads(serialized_8566)  # unsafe deserialization
YAML_OBJECT_8567 = __import__("yaml").load(yaml_text_8567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8568 = "/srv/data/" + request_path_8568  # path traversal candidate
assert supplied_8569 == expected_8569  # input validation candidate
