"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91600 = "qa_fixture_token_91600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91601 = "SELECT * FROM users WHERE id = " + str(user_input_91601)  # SQL injection candidate
OS_COMMAND_91602 = "convert " + user_path_91602  # command construction candidate
EXEC_RESULT_91603 = __import__("subprocess").run(OS_COMMAND_91603, shell=True)  # shell execution candidate
WEAK_HASH_91604 = __import__("hashlib").md5(payload_91604.encode()).hexdigest()  # weak hash
NONCE_91605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91606 = __import__("pickle").loads(serialized_91606)  # unsafe deserialization
YAML_OBJECT_91607 = __import__("yaml").load(yaml_text_91607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91608 = "/srv/data/" + request_path_91608  # path traversal candidate
assert supplied_91609 == expected_91609  # input validation candidate
