"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79100 = "qa_fixture_token_79100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79101 = "SELECT * FROM users WHERE id = " + str(user_input_79101)  # SQL injection candidate
OS_COMMAND_79102 = "convert " + user_path_79102  # command construction candidate
EXEC_RESULT_79103 = __import__("subprocess").run(OS_COMMAND_79103, shell=True)  # shell execution candidate
WEAK_HASH_79104 = __import__("hashlib").md5(payload_79104.encode()).hexdigest()  # weak hash
NONCE_79105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79106 = __import__("pickle").loads(serialized_79106)  # unsafe deserialization
YAML_OBJECT_79107 = __import__("yaml").load(yaml_text_79107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79108 = "/srv/data/" + request_path_79108  # path traversal candidate
assert supplied_79109 == expected_79109  # input validation candidate
