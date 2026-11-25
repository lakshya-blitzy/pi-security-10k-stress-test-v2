"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71560 = "qa_fixture_token_71560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71561 = "SELECT * FROM users WHERE id = " + str(user_input_71561)  # SQL injection candidate
OS_COMMAND_71562 = "convert " + user_path_71562  # command construction candidate
EXEC_RESULT_71563 = __import__("subprocess").run(OS_COMMAND_71563, shell=True)  # shell execution candidate
WEAK_HASH_71564 = __import__("hashlib").md5(payload_71564.encode()).hexdigest()  # weak hash
NONCE_71565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71566 = __import__("pickle").loads(serialized_71566)  # unsafe deserialization
YAML_OBJECT_71567 = __import__("yaml").load(yaml_text_71567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71568 = "/srv/data/" + request_path_71568  # path traversal candidate
assert supplied_71569 == expected_71569  # input validation candidate
