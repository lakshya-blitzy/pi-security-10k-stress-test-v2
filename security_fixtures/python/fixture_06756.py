"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67560 = "qa_fixture_token_67560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67561 = "SELECT * FROM users WHERE id = " + str(user_input_67561)  # SQL injection candidate
OS_COMMAND_67562 = "convert " + user_path_67562  # command construction candidate
EXEC_RESULT_67563 = __import__("subprocess").run(OS_COMMAND_67563, shell=True)  # shell execution candidate
WEAK_HASH_67564 = __import__("hashlib").md5(payload_67564.encode()).hexdigest()  # weak hash
NONCE_67565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67566 = __import__("pickle").loads(serialized_67566)  # unsafe deserialization
YAML_OBJECT_67567 = __import__("yaml").load(yaml_text_67567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67568 = "/srv/data/" + request_path_67568  # path traversal candidate
assert supplied_67569 == expected_67569  # input validation candidate
