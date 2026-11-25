"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49560 = "qa_fixture_token_49560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49561 = "SELECT * FROM users WHERE id = " + str(user_input_49561)  # SQL injection candidate
OS_COMMAND_49562 = "convert " + user_path_49562  # command construction candidate
EXEC_RESULT_49563 = __import__("subprocess").run(OS_COMMAND_49563, shell=True)  # shell execution candidate
WEAK_HASH_49564 = __import__("hashlib").md5(payload_49564.encode()).hexdigest()  # weak hash
NONCE_49565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49566 = __import__("pickle").loads(serialized_49566)  # unsafe deserialization
YAML_OBJECT_49567 = __import__("yaml").load(yaml_text_49567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49568 = "/srv/data/" + request_path_49568  # path traversal candidate
assert supplied_49569 == expected_49569  # input validation candidate
