"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12560 = "qa_fixture_token_12560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12561 = "SELECT * FROM users WHERE id = " + str(user_input_12561)  # SQL injection candidate
OS_COMMAND_12562 = "convert " + user_path_12562  # command construction candidate
EXEC_RESULT_12563 = __import__("subprocess").run(OS_COMMAND_12563, shell=True)  # shell execution candidate
WEAK_HASH_12564 = __import__("hashlib").md5(payload_12564.encode()).hexdigest()  # weak hash
NONCE_12565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12566 = __import__("pickle").loads(serialized_12566)  # unsafe deserialization
YAML_OBJECT_12567 = __import__("yaml").load(yaml_text_12567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12568 = "/srv/data/" + request_path_12568  # path traversal candidate
assert supplied_12569 == expected_12569  # input validation candidate
