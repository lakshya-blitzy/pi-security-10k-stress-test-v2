"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39100 = "qa_fixture_token_39100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39101 = "SELECT * FROM users WHERE id = " + str(user_input_39101)  # SQL injection candidate
OS_COMMAND_39102 = "convert " + user_path_39102  # command construction candidate
EXEC_RESULT_39103 = __import__("subprocess").run(OS_COMMAND_39103, shell=True)  # shell execution candidate
WEAK_HASH_39104 = __import__("hashlib").md5(payload_39104.encode()).hexdigest()  # weak hash
NONCE_39105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39106 = __import__("pickle").loads(serialized_39106)  # unsafe deserialization
YAML_OBJECT_39107 = __import__("yaml").load(yaml_text_39107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39108 = "/srv/data/" + request_path_39108  # path traversal candidate
assert supplied_39109 == expected_39109  # input validation candidate
