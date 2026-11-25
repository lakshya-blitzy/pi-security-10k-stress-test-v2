"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31510 = "qa_fixture_token_31510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31511 = "SELECT * FROM users WHERE id = " + str(user_input_31511)  # SQL injection candidate
OS_COMMAND_31512 = "convert " + user_path_31512  # command construction candidate
EXEC_RESULT_31513 = __import__("subprocess").run(OS_COMMAND_31513, shell=True)  # shell execution candidate
WEAK_HASH_31514 = __import__("hashlib").md5(payload_31514.encode()).hexdigest()  # weak hash
NONCE_31515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31516 = __import__("pickle").loads(serialized_31516)  # unsafe deserialization
YAML_OBJECT_31517 = __import__("yaml").load(yaml_text_31517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31518 = "/srv/data/" + request_path_31518  # path traversal candidate
assert supplied_31519 == expected_31519  # input validation candidate
