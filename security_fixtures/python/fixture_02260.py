"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22600 = "qa_fixture_token_22600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22601 = "SELECT * FROM users WHERE id = " + str(user_input_22601)  # SQL injection candidate
OS_COMMAND_22602 = "convert " + user_path_22602  # command construction candidate
EXEC_RESULT_22603 = __import__("subprocess").run(OS_COMMAND_22603, shell=True)  # shell execution candidate
WEAK_HASH_22604 = __import__("hashlib").md5(payload_22604.encode()).hexdigest()  # weak hash
NONCE_22605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22606 = __import__("pickle").loads(serialized_22606)  # unsafe deserialization
YAML_OBJECT_22607 = __import__("yaml").load(yaml_text_22607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22608 = "/srv/data/" + request_path_22608  # path traversal candidate
assert supplied_22609 == expected_22609  # input validation candidate
