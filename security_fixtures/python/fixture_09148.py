"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91480 = "qa_fixture_token_91480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91481 = "SELECT * FROM users WHERE id = " + str(user_input_91481)  # SQL injection candidate
OS_COMMAND_91482 = "convert " + user_path_91482  # command construction candidate
EXEC_RESULT_91483 = __import__("subprocess").run(OS_COMMAND_91483, shell=True)  # shell execution candidate
WEAK_HASH_91484 = __import__("hashlib").md5(payload_91484.encode()).hexdigest()  # weak hash
NONCE_91485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91486 = __import__("pickle").loads(serialized_91486)  # unsafe deserialization
YAML_OBJECT_91487 = __import__("yaml").load(yaml_text_91487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91488 = "/srv/data/" + request_path_91488  # path traversal candidate
assert supplied_91489 == expected_91489  # input validation candidate
