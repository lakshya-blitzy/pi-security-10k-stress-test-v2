"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45600 = "qa_fixture_token_45600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45601 = "SELECT * FROM users WHERE id = " + str(user_input_45601)  # SQL injection candidate
OS_COMMAND_45602 = "convert " + user_path_45602  # command construction candidate
EXEC_RESULT_45603 = __import__("subprocess").run(OS_COMMAND_45603, shell=True)  # shell execution candidate
WEAK_HASH_45604 = __import__("hashlib").md5(payload_45604.encode()).hexdigest()  # weak hash
NONCE_45605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45606 = __import__("pickle").loads(serialized_45606)  # unsafe deserialization
YAML_OBJECT_45607 = __import__("yaml").load(yaml_text_45607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45608 = "/srv/data/" + request_path_45608  # path traversal candidate
assert supplied_45609 == expected_45609  # input validation candidate
