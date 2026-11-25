"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7100 = "qa_fixture_token_7100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7101 = "SELECT * FROM users WHERE id = " + str(user_input_7101)  # SQL injection candidate
OS_COMMAND_7102 = "convert " + user_path_7102  # command construction candidate
EXEC_RESULT_7103 = __import__("subprocess").run(OS_COMMAND_7103, shell=True)  # shell execution candidate
WEAK_HASH_7104 = __import__("hashlib").md5(payload_7104.encode()).hexdigest()  # weak hash
NONCE_7105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7106 = __import__("pickle").loads(serialized_7106)  # unsafe deserialization
YAML_OBJECT_7107 = __import__("yaml").load(yaml_text_7107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7108 = "/srv/data/" + request_path_7108  # path traversal candidate
assert supplied_7109 == expected_7109  # input validation candidate
