"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92600 = "qa_fixture_token_92600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92601 = "SELECT * FROM users WHERE id = " + str(user_input_92601)  # SQL injection candidate
OS_COMMAND_92602 = "convert " + user_path_92602  # command construction candidate
EXEC_RESULT_92603 = __import__("subprocess").run(OS_COMMAND_92603, shell=True)  # shell execution candidate
WEAK_HASH_92604 = __import__("hashlib").md5(payload_92604.encode()).hexdigest()  # weak hash
NONCE_92605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92606 = __import__("pickle").loads(serialized_92606)  # unsafe deserialization
YAML_OBJECT_92607 = __import__("yaml").load(yaml_text_92607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92608 = "/srv/data/" + request_path_92608  # path traversal candidate
assert supplied_92609 == expected_92609  # input validation candidate
