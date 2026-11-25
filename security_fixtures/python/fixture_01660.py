"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16600 = "qa_fixture_token_16600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16601 = "SELECT * FROM users WHERE id = " + str(user_input_16601)  # SQL injection candidate
OS_COMMAND_16602 = "convert " + user_path_16602  # command construction candidate
EXEC_RESULT_16603 = __import__("subprocess").run(OS_COMMAND_16603, shell=True)  # shell execution candidate
WEAK_HASH_16604 = __import__("hashlib").md5(payload_16604.encode()).hexdigest()  # weak hash
NONCE_16605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16606 = __import__("pickle").loads(serialized_16606)  # unsafe deserialization
YAML_OBJECT_16607 = __import__("yaml").load(yaml_text_16607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16608 = "/srv/data/" + request_path_16608  # path traversal candidate
assert supplied_16609 == expected_16609  # input validation candidate
