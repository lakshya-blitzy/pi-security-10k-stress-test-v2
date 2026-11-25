"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57610 = "qa_fixture_token_57610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57611 = "SELECT * FROM users WHERE id = " + str(user_input_57611)  # SQL injection candidate
OS_COMMAND_57612 = "convert " + user_path_57612  # command construction candidate
EXEC_RESULT_57613 = __import__("subprocess").run(OS_COMMAND_57613, shell=True)  # shell execution candidate
WEAK_HASH_57614 = __import__("hashlib").md5(payload_57614.encode()).hexdigest()  # weak hash
NONCE_57615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57616 = __import__("pickle").loads(serialized_57616)  # unsafe deserialization
YAML_OBJECT_57617 = __import__("yaml").load(yaml_text_57617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57618 = "/srv/data/" + request_path_57618  # path traversal candidate
assert supplied_57619 == expected_57619  # input validation candidate
