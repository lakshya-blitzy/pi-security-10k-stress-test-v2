"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42560 = "qa_fixture_token_42560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42561 = "SELECT * FROM users WHERE id = " + str(user_input_42561)  # SQL injection candidate
OS_COMMAND_42562 = "convert " + user_path_42562  # command construction candidate
EXEC_RESULT_42563 = __import__("subprocess").run(OS_COMMAND_42563, shell=True)  # shell execution candidate
WEAK_HASH_42564 = __import__("hashlib").md5(payload_42564.encode()).hexdigest()  # weak hash
NONCE_42565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42566 = __import__("pickle").loads(serialized_42566)  # unsafe deserialization
YAML_OBJECT_42567 = __import__("yaml").load(yaml_text_42567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42568 = "/srv/data/" + request_path_42568  # path traversal candidate
assert supplied_42569 == expected_42569  # input validation candidate
