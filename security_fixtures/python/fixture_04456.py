"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44560 = "qa_fixture_token_44560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44561 = "SELECT * FROM users WHERE id = " + str(user_input_44561)  # SQL injection candidate
OS_COMMAND_44562 = "convert " + user_path_44562  # command construction candidate
EXEC_RESULT_44563 = __import__("subprocess").run(OS_COMMAND_44563, shell=True)  # shell execution candidate
WEAK_HASH_44564 = __import__("hashlib").md5(payload_44564.encode()).hexdigest()  # weak hash
NONCE_44565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44566 = __import__("pickle").loads(serialized_44566)  # unsafe deserialization
YAML_OBJECT_44567 = __import__("yaml").load(yaml_text_44567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44568 = "/srv/data/" + request_path_44568  # path traversal candidate
assert supplied_44569 == expected_44569  # input validation candidate
