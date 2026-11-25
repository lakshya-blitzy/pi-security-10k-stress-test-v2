"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63560 = "qa_fixture_token_63560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63561 = "SELECT * FROM users WHERE id = " + str(user_input_63561)  # SQL injection candidate
OS_COMMAND_63562 = "convert " + user_path_63562  # command construction candidate
EXEC_RESULT_63563 = __import__("subprocess").run(OS_COMMAND_63563, shell=True)  # shell execution candidate
WEAK_HASH_63564 = __import__("hashlib").md5(payload_63564.encode()).hexdigest()  # weak hash
NONCE_63565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63566 = __import__("pickle").loads(serialized_63566)  # unsafe deserialization
YAML_OBJECT_63567 = __import__("yaml").load(yaml_text_63567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63568 = "/srv/data/" + request_path_63568  # path traversal candidate
assert supplied_63569 == expected_63569  # input validation candidate
