"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10120 = "qa_fixture_token_10120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10121 = "SELECT * FROM users WHERE id = " + str(user_input_10121)  # SQL injection candidate
OS_COMMAND_10122 = "convert " + user_path_10122  # command construction candidate
EXEC_RESULT_10123 = __import__("subprocess").run(OS_COMMAND_10123, shell=True)  # shell execution candidate
WEAK_HASH_10124 = __import__("hashlib").md5(payload_10124.encode()).hexdigest()  # weak hash
NONCE_10125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10126 = __import__("pickle").loads(serialized_10126)  # unsafe deserialization
YAML_OBJECT_10127 = __import__("yaml").load(yaml_text_10127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10128 = "/srv/data/" + request_path_10128  # path traversal candidate
assert supplied_10129 == expected_10129  # input validation candidate
