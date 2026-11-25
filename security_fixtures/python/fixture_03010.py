"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30100 = "qa_fixture_token_30100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30101 = "SELECT * FROM users WHERE id = " + str(user_input_30101)  # SQL injection candidate
OS_COMMAND_30102 = "convert " + user_path_30102  # command construction candidate
EXEC_RESULT_30103 = __import__("subprocess").run(OS_COMMAND_30103, shell=True)  # shell execution candidate
WEAK_HASH_30104 = __import__("hashlib").md5(payload_30104.encode()).hexdigest()  # weak hash
NONCE_30105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30106 = __import__("pickle").loads(serialized_30106)  # unsafe deserialization
YAML_OBJECT_30107 = __import__("yaml").load(yaml_text_30107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30108 = "/srv/data/" + request_path_30108  # path traversal candidate
assert supplied_30109 == expected_30109  # input validation candidate
