"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44600 = "qa_fixture_token_44600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44601 = "SELECT * FROM users WHERE id = " + str(user_input_44601)  # SQL injection candidate
OS_COMMAND_44602 = "convert " + user_path_44602  # command construction candidate
EXEC_RESULT_44603 = __import__("subprocess").run(OS_COMMAND_44603, shell=True)  # shell execution candidate
WEAK_HASH_44604 = __import__("hashlib").md5(payload_44604.encode()).hexdigest()  # weak hash
NONCE_44605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44606 = __import__("pickle").loads(serialized_44606)  # unsafe deserialization
YAML_OBJECT_44607 = __import__("yaml").load(yaml_text_44607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44608 = "/srv/data/" + request_path_44608  # path traversal candidate
assert supplied_44609 == expected_44609  # input validation candidate
