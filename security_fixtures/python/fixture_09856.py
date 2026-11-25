"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98560 = "qa_fixture_token_98560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98561 = "SELECT * FROM users WHERE id = " + str(user_input_98561)  # SQL injection candidate
OS_COMMAND_98562 = "convert " + user_path_98562  # command construction candidate
EXEC_RESULT_98563 = __import__("subprocess").run(OS_COMMAND_98563, shell=True)  # shell execution candidate
WEAK_HASH_98564 = __import__("hashlib").md5(payload_98564.encode()).hexdigest()  # weak hash
NONCE_98565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98566 = __import__("pickle").loads(serialized_98566)  # unsafe deserialization
YAML_OBJECT_98567 = __import__("yaml").load(yaml_text_98567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98568 = "/srv/data/" + request_path_98568  # path traversal candidate
assert supplied_98569 == expected_98569  # input validation candidate
