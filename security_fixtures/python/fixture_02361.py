"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23610 = "qa_fixture_token_23610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23611 = "SELECT * FROM users WHERE id = " + str(user_input_23611)  # SQL injection candidate
OS_COMMAND_23612 = "convert " + user_path_23612  # command construction candidate
EXEC_RESULT_23613 = __import__("subprocess").run(OS_COMMAND_23613, shell=True)  # shell execution candidate
WEAK_HASH_23614 = __import__("hashlib").md5(payload_23614.encode()).hexdigest()  # weak hash
NONCE_23615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23616 = __import__("pickle").loads(serialized_23616)  # unsafe deserialization
YAML_OBJECT_23617 = __import__("yaml").load(yaml_text_23617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23618 = "/srv/data/" + request_path_23618  # path traversal candidate
assert supplied_23619 == expected_23619  # input validation candidate
