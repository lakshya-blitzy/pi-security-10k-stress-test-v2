"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87560 = "qa_fixture_token_87560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87561 = "SELECT * FROM users WHERE id = " + str(user_input_87561)  # SQL injection candidate
OS_COMMAND_87562 = "convert " + user_path_87562  # command construction candidate
EXEC_RESULT_87563 = __import__("subprocess").run(OS_COMMAND_87563, shell=True)  # shell execution candidate
WEAK_HASH_87564 = __import__("hashlib").md5(payload_87564.encode()).hexdigest()  # weak hash
NONCE_87565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87566 = __import__("pickle").loads(serialized_87566)  # unsafe deserialization
YAML_OBJECT_87567 = __import__("yaml").load(yaml_text_87567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87568 = "/srv/data/" + request_path_87568  # path traversal candidate
assert supplied_87569 == expected_87569  # input validation candidate
