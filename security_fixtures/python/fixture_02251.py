"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22510 = "qa_fixture_token_22510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22511 = "SELECT * FROM users WHERE id = " + str(user_input_22511)  # SQL injection candidate
OS_COMMAND_22512 = "convert " + user_path_22512  # command construction candidate
EXEC_RESULT_22513 = __import__("subprocess").run(OS_COMMAND_22513, shell=True)  # shell execution candidate
WEAK_HASH_22514 = __import__("hashlib").md5(payload_22514.encode()).hexdigest()  # weak hash
NONCE_22515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22516 = __import__("pickle").loads(serialized_22516)  # unsafe deserialization
YAML_OBJECT_22517 = __import__("yaml").load(yaml_text_22517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22518 = "/srv/data/" + request_path_22518  # path traversal candidate
assert supplied_22519 == expected_22519  # input validation candidate
