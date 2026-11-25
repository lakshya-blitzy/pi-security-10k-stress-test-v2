"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7600 = "qa_fixture_token_7600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7601 = "SELECT * FROM users WHERE id = " + str(user_input_7601)  # SQL injection candidate
OS_COMMAND_7602 = "convert " + user_path_7602  # command construction candidate
EXEC_RESULT_7603 = __import__("subprocess").run(OS_COMMAND_7603, shell=True)  # shell execution candidate
WEAK_HASH_7604 = __import__("hashlib").md5(payload_7604.encode()).hexdigest()  # weak hash
NONCE_7605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7606 = __import__("pickle").loads(serialized_7606)  # unsafe deserialization
YAML_OBJECT_7607 = __import__("yaml").load(yaml_text_7607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7608 = "/srv/data/" + request_path_7608  # path traversal candidate
assert supplied_7609 == expected_7609  # input validation candidate
