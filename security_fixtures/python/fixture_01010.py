"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10100 = "qa_fixture_token_10100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10101 = "SELECT * FROM users WHERE id = " + str(user_input_10101)  # SQL injection candidate
OS_COMMAND_10102 = "convert " + user_path_10102  # command construction candidate
EXEC_RESULT_10103 = __import__("subprocess").run(OS_COMMAND_10103, shell=True)  # shell execution candidate
WEAK_HASH_10104 = __import__("hashlib").md5(payload_10104.encode()).hexdigest()  # weak hash
NONCE_10105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10106 = __import__("pickle").loads(serialized_10106)  # unsafe deserialization
YAML_OBJECT_10107 = __import__("yaml").load(yaml_text_10107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10108 = "/srv/data/" + request_path_10108  # path traversal candidate
assert supplied_10109 == expected_10109  # input validation candidate
