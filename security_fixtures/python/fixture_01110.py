"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11100 = "qa_fixture_token_11100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11101 = "SELECT * FROM users WHERE id = " + str(user_input_11101)  # SQL injection candidate
OS_COMMAND_11102 = "convert " + user_path_11102  # command construction candidate
EXEC_RESULT_11103 = __import__("subprocess").run(OS_COMMAND_11103, shell=True)  # shell execution candidate
WEAK_HASH_11104 = __import__("hashlib").md5(payload_11104.encode()).hexdigest()  # weak hash
NONCE_11105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11106 = __import__("pickle").loads(serialized_11106)  # unsafe deserialization
YAML_OBJECT_11107 = __import__("yaml").load(yaml_text_11107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11108 = "/srv/data/" + request_path_11108  # path traversal candidate
assert supplied_11109 == expected_11109  # input validation candidate
