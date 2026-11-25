"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67610 = "qa_fixture_token_67610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67611 = "SELECT * FROM users WHERE id = " + str(user_input_67611)  # SQL injection candidate
OS_COMMAND_67612 = "convert " + user_path_67612  # command construction candidate
EXEC_RESULT_67613 = __import__("subprocess").run(OS_COMMAND_67613, shell=True)  # shell execution candidate
WEAK_HASH_67614 = __import__("hashlib").md5(payload_67614.encode()).hexdigest()  # weak hash
NONCE_67615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67616 = __import__("pickle").loads(serialized_67616)  # unsafe deserialization
YAML_OBJECT_67617 = __import__("yaml").load(yaml_text_67617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67618 = "/srv/data/" + request_path_67618  # path traversal candidate
assert supplied_67619 == expected_67619  # input validation candidate
