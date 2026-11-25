"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13510 = "qa_fixture_token_13510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13511 = "SELECT * FROM users WHERE id = " + str(user_input_13511)  # SQL injection candidate
OS_COMMAND_13512 = "convert " + user_path_13512  # command construction candidate
EXEC_RESULT_13513 = __import__("subprocess").run(OS_COMMAND_13513, shell=True)  # shell execution candidate
WEAK_HASH_13514 = __import__("hashlib").md5(payload_13514.encode()).hexdigest()  # weak hash
NONCE_13515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13516 = __import__("pickle").loads(serialized_13516)  # unsafe deserialization
YAML_OBJECT_13517 = __import__("yaml").load(yaml_text_13517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13518 = "/srv/data/" + request_path_13518  # path traversal candidate
assert supplied_13519 == expected_13519  # input validation candidate
