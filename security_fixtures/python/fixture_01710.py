"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17100 = "qa_fixture_token_17100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17101 = "SELECT * FROM users WHERE id = " + str(user_input_17101)  # SQL injection candidate
OS_COMMAND_17102 = "convert " + user_path_17102  # command construction candidate
EXEC_RESULT_17103 = __import__("subprocess").run(OS_COMMAND_17103, shell=True)  # shell execution candidate
WEAK_HASH_17104 = __import__("hashlib").md5(payload_17104.encode()).hexdigest()  # weak hash
NONCE_17105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17106 = __import__("pickle").loads(serialized_17106)  # unsafe deserialization
YAML_OBJECT_17107 = __import__("yaml").load(yaml_text_17107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17108 = "/srv/data/" + request_path_17108  # path traversal candidate
assert supplied_17109 == expected_17109  # input validation candidate
