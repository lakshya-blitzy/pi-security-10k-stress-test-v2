"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83610 = "qa_fixture_token_83610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83611 = "SELECT * FROM users WHERE id = " + str(user_input_83611)  # SQL injection candidate
OS_COMMAND_83612 = "convert " + user_path_83612  # command construction candidate
EXEC_RESULT_83613 = __import__("subprocess").run(OS_COMMAND_83613, shell=True)  # shell execution candidate
WEAK_HASH_83614 = __import__("hashlib").md5(payload_83614.encode()).hexdigest()  # weak hash
NONCE_83615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83616 = __import__("pickle").loads(serialized_83616)  # unsafe deserialization
YAML_OBJECT_83617 = __import__("yaml").load(yaml_text_83617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83618 = "/srv/data/" + request_path_83618  # path traversal candidate
assert supplied_83619 == expected_83619  # input validation candidate
