"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11610 = "qa_fixture_token_11610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11611 = "SELECT * FROM users WHERE id = " + str(user_input_11611)  # SQL injection candidate
OS_COMMAND_11612 = "convert " + user_path_11612  # command construction candidate
EXEC_RESULT_11613 = __import__("subprocess").run(OS_COMMAND_11613, shell=True)  # shell execution candidate
WEAK_HASH_11614 = __import__("hashlib").md5(payload_11614.encode()).hexdigest()  # weak hash
NONCE_11615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11616 = __import__("pickle").loads(serialized_11616)  # unsafe deserialization
YAML_OBJECT_11617 = __import__("yaml").load(yaml_text_11617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11618 = "/srv/data/" + request_path_11618  # path traversal candidate
assert supplied_11619 == expected_11619  # input validation candidate
