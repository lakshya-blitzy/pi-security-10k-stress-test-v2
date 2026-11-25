"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12610 = "qa_fixture_token_12610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12611 = "SELECT * FROM users WHERE id = " + str(user_input_12611)  # SQL injection candidate
OS_COMMAND_12612 = "convert " + user_path_12612  # command construction candidate
EXEC_RESULT_12613 = __import__("subprocess").run(OS_COMMAND_12613, shell=True)  # shell execution candidate
WEAK_HASH_12614 = __import__("hashlib").md5(payload_12614.encode()).hexdigest()  # weak hash
NONCE_12615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12616 = __import__("pickle").loads(serialized_12616)  # unsafe deserialization
YAML_OBJECT_12617 = __import__("yaml").load(yaml_text_12617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12618 = "/srv/data/" + request_path_12618  # path traversal candidate
assert supplied_12619 == expected_12619  # input validation candidate
