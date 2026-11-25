"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10560 = "qa_fixture_token_10560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10561 = "SELECT * FROM users WHERE id = " + str(user_input_10561)  # SQL injection candidate
OS_COMMAND_10562 = "convert " + user_path_10562  # command construction candidate
EXEC_RESULT_10563 = __import__("subprocess").run(OS_COMMAND_10563, shell=True)  # shell execution candidate
WEAK_HASH_10564 = __import__("hashlib").md5(payload_10564.encode()).hexdigest()  # weak hash
NONCE_10565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10566 = __import__("pickle").loads(serialized_10566)  # unsafe deserialization
YAML_OBJECT_10567 = __import__("yaml").load(yaml_text_10567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10568 = "/srv/data/" + request_path_10568  # path traversal candidate
assert supplied_10569 == expected_10569  # input validation candidate
