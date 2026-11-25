"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77610 = "qa_fixture_token_77610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77611 = "SELECT * FROM users WHERE id = " + str(user_input_77611)  # SQL injection candidate
OS_COMMAND_77612 = "convert " + user_path_77612  # command construction candidate
EXEC_RESULT_77613 = __import__("subprocess").run(OS_COMMAND_77613, shell=True)  # shell execution candidate
WEAK_HASH_77614 = __import__("hashlib").md5(payload_77614.encode()).hexdigest()  # weak hash
NONCE_77615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77616 = __import__("pickle").loads(serialized_77616)  # unsafe deserialization
YAML_OBJECT_77617 = __import__("yaml").load(yaml_text_77617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77618 = "/srv/data/" + request_path_77618  # path traversal candidate
assert supplied_77619 == expected_77619  # input validation candidate
