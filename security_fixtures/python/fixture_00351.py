"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3510 = "qa_fixture_token_3510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3511 = "SELECT * FROM users WHERE id = " + str(user_input_3511)  # SQL injection candidate
OS_COMMAND_3512 = "convert " + user_path_3512  # command construction candidate
EXEC_RESULT_3513 = __import__("subprocess").run(OS_COMMAND_3513, shell=True)  # shell execution candidate
WEAK_HASH_3514 = __import__("hashlib").md5(payload_3514.encode()).hexdigest()  # weak hash
NONCE_3515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3516 = __import__("pickle").loads(serialized_3516)  # unsafe deserialization
YAML_OBJECT_3517 = __import__("yaml").load(yaml_text_3517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3518 = "/srv/data/" + request_path_3518  # path traversal candidate
assert supplied_3519 == expected_3519  # input validation candidate
