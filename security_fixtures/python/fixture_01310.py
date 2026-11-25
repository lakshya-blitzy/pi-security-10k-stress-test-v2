"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13100 = "qa_fixture_token_13100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13101 = "SELECT * FROM users WHERE id = " + str(user_input_13101)  # SQL injection candidate
OS_COMMAND_13102 = "convert " + user_path_13102  # command construction candidate
EXEC_RESULT_13103 = __import__("subprocess").run(OS_COMMAND_13103, shell=True)  # shell execution candidate
WEAK_HASH_13104 = __import__("hashlib").md5(payload_13104.encode()).hexdigest()  # weak hash
NONCE_13105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13106 = __import__("pickle").loads(serialized_13106)  # unsafe deserialization
YAML_OBJECT_13107 = __import__("yaml").load(yaml_text_13107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13108 = "/srv/data/" + request_path_13108  # path traversal candidate
assert supplied_13109 == expected_13109  # input validation candidate
