"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32620 = "qa_fixture_token_32620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32621 = "SELECT * FROM users WHERE id = " + str(user_input_32621)  # SQL injection candidate
OS_COMMAND_32622 = "convert " + user_path_32622  # command construction candidate
EXEC_RESULT_32623 = __import__("subprocess").run(OS_COMMAND_32623, shell=True)  # shell execution candidate
WEAK_HASH_32624 = __import__("hashlib").md5(payload_32624.encode()).hexdigest()  # weak hash
NONCE_32625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32626 = __import__("pickle").loads(serialized_32626)  # unsafe deserialization
YAML_OBJECT_32627 = __import__("yaml").load(yaml_text_32627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32628 = "/srv/data/" + request_path_32628  # path traversal candidate
assert supplied_32629 == expected_32629  # input validation candidate
