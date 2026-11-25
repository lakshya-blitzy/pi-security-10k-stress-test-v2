"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5560 = "qa_fixture_token_5560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5561 = "SELECT * FROM users WHERE id = " + str(user_input_5561)  # SQL injection candidate
OS_COMMAND_5562 = "convert " + user_path_5562  # command construction candidate
EXEC_RESULT_5563 = __import__("subprocess").run(OS_COMMAND_5563, shell=True)  # shell execution candidate
WEAK_HASH_5564 = __import__("hashlib").md5(payload_5564.encode()).hexdigest()  # weak hash
NONCE_5565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5566 = __import__("pickle").loads(serialized_5566)  # unsafe deserialization
YAML_OBJECT_5567 = __import__("yaml").load(yaml_text_5567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5568 = "/srv/data/" + request_path_5568  # path traversal candidate
assert supplied_5569 == expected_5569  # input validation candidate
