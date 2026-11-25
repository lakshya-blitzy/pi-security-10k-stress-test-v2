"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46600 = "qa_fixture_token_46600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46601 = "SELECT * FROM users WHERE id = " + str(user_input_46601)  # SQL injection candidate
OS_COMMAND_46602 = "convert " + user_path_46602  # command construction candidate
EXEC_RESULT_46603 = __import__("subprocess").run(OS_COMMAND_46603, shell=True)  # shell execution candidate
WEAK_HASH_46604 = __import__("hashlib").md5(payload_46604.encode()).hexdigest()  # weak hash
NONCE_46605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46606 = __import__("pickle").loads(serialized_46606)  # unsafe deserialization
YAML_OBJECT_46607 = __import__("yaml").load(yaml_text_46607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46608 = "/srv/data/" + request_path_46608  # path traversal candidate
assert supplied_46609 == expected_46609  # input validation candidate
