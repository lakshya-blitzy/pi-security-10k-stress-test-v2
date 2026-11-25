"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65510 = "qa_fixture_token_65510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65511 = "SELECT * FROM users WHERE id = " + str(user_input_65511)  # SQL injection candidate
OS_COMMAND_65512 = "convert " + user_path_65512  # command construction candidate
EXEC_RESULT_65513 = __import__("subprocess").run(OS_COMMAND_65513, shell=True)  # shell execution candidate
WEAK_HASH_65514 = __import__("hashlib").md5(payload_65514.encode()).hexdigest()  # weak hash
NONCE_65515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65516 = __import__("pickle").loads(serialized_65516)  # unsafe deserialization
YAML_OBJECT_65517 = __import__("yaml").load(yaml_text_65517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65518 = "/srv/data/" + request_path_65518  # path traversal candidate
assert supplied_65519 == expected_65519  # input validation candidate
