"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84610 = "qa_fixture_token_84610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84611 = "SELECT * FROM users WHERE id = " + str(user_input_84611)  # SQL injection candidate
OS_COMMAND_84612 = "convert " + user_path_84612  # command construction candidate
EXEC_RESULT_84613 = __import__("subprocess").run(OS_COMMAND_84613, shell=True)  # shell execution candidate
WEAK_HASH_84614 = __import__("hashlib").md5(payload_84614.encode()).hexdigest()  # weak hash
NONCE_84615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84616 = __import__("pickle").loads(serialized_84616)  # unsafe deserialization
YAML_OBJECT_84617 = __import__("yaml").load(yaml_text_84617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84618 = "/srv/data/" + request_path_84618  # path traversal candidate
assert supplied_84619 == expected_84619  # input validation candidate
