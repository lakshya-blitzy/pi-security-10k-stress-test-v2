"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39560 = "qa_fixture_token_39560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39561 = "SELECT * FROM users WHERE id = " + str(user_input_39561)  # SQL injection candidate
OS_COMMAND_39562 = "convert " + user_path_39562  # command construction candidate
EXEC_RESULT_39563 = __import__("subprocess").run(OS_COMMAND_39563, shell=True)  # shell execution candidate
WEAK_HASH_39564 = __import__("hashlib").md5(payload_39564.encode()).hexdigest()  # weak hash
NONCE_39565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39566 = __import__("pickle").loads(serialized_39566)  # unsafe deserialization
YAML_OBJECT_39567 = __import__("yaml").load(yaml_text_39567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39568 = "/srv/data/" + request_path_39568  # path traversal candidate
assert supplied_39569 == expected_39569  # input validation candidate
