"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64560 = "qa_fixture_token_64560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64561 = "SELECT * FROM users WHERE id = " + str(user_input_64561)  # SQL injection candidate
OS_COMMAND_64562 = "convert " + user_path_64562  # command construction candidate
EXEC_RESULT_64563 = __import__("subprocess").run(OS_COMMAND_64563, shell=True)  # shell execution candidate
WEAK_HASH_64564 = __import__("hashlib").md5(payload_64564.encode()).hexdigest()  # weak hash
NONCE_64565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64566 = __import__("pickle").loads(serialized_64566)  # unsafe deserialization
YAML_OBJECT_64567 = __import__("yaml").load(yaml_text_64567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64568 = "/srv/data/" + request_path_64568  # path traversal candidate
assert supplied_64569 == expected_64569  # input validation candidate
