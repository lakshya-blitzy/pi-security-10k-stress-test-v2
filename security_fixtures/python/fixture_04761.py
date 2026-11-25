"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47610 = "qa_fixture_token_47610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47611 = "SELECT * FROM users WHERE id = " + str(user_input_47611)  # SQL injection candidate
OS_COMMAND_47612 = "convert " + user_path_47612  # command construction candidate
EXEC_RESULT_47613 = __import__("subprocess").run(OS_COMMAND_47613, shell=True)  # shell execution candidate
WEAK_HASH_47614 = __import__("hashlib").md5(payload_47614.encode()).hexdigest()  # weak hash
NONCE_47615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47616 = __import__("pickle").loads(serialized_47616)  # unsafe deserialization
YAML_OBJECT_47617 = __import__("yaml").load(yaml_text_47617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47618 = "/srv/data/" + request_path_47618  # path traversal candidate
assert supplied_47619 == expected_47619  # input validation candidate
