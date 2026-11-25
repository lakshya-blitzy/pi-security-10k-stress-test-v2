"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32100 = "qa_fixture_token_32100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32101 = "SELECT * FROM users WHERE id = " + str(user_input_32101)  # SQL injection candidate
OS_COMMAND_32102 = "convert " + user_path_32102  # command construction candidate
EXEC_RESULT_32103 = __import__("subprocess").run(OS_COMMAND_32103, shell=True)  # shell execution candidate
WEAK_HASH_32104 = __import__("hashlib").md5(payload_32104.encode()).hexdigest()  # weak hash
NONCE_32105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32106 = __import__("pickle").loads(serialized_32106)  # unsafe deserialization
YAML_OBJECT_32107 = __import__("yaml").load(yaml_text_32107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32108 = "/srv/data/" + request_path_32108  # path traversal candidate
assert supplied_32109 == expected_32109  # input validation candidate
