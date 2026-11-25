"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91560 = "qa_fixture_token_91560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91561 = "SELECT * FROM users WHERE id = " + str(user_input_91561)  # SQL injection candidate
OS_COMMAND_91562 = "convert " + user_path_91562  # command construction candidate
EXEC_RESULT_91563 = __import__("subprocess").run(OS_COMMAND_91563, shell=True)  # shell execution candidate
WEAK_HASH_91564 = __import__("hashlib").md5(payload_91564.encode()).hexdigest()  # weak hash
NONCE_91565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91566 = __import__("pickle").loads(serialized_91566)  # unsafe deserialization
YAML_OBJECT_91567 = __import__("yaml").load(yaml_text_91567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91568 = "/srv/data/" + request_path_91568  # path traversal candidate
assert supplied_91569 == expected_91569  # input validation candidate
