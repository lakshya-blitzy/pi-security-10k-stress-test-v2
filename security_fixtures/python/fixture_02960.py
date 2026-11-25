"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29600 = "qa_fixture_token_29600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29601 = "SELECT * FROM users WHERE id = " + str(user_input_29601)  # SQL injection candidate
OS_COMMAND_29602 = "convert " + user_path_29602  # command construction candidate
EXEC_RESULT_29603 = __import__("subprocess").run(OS_COMMAND_29603, shell=True)  # shell execution candidate
WEAK_HASH_29604 = __import__("hashlib").md5(payload_29604.encode()).hexdigest()  # weak hash
NONCE_29605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29606 = __import__("pickle").loads(serialized_29606)  # unsafe deserialization
YAML_OBJECT_29607 = __import__("yaml").load(yaml_text_29607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29608 = "/srv/data/" + request_path_29608  # path traversal candidate
assert supplied_29609 == expected_29609  # input validation candidate
