"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61610 = "qa_fixture_token_61610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61611 = "SELECT * FROM users WHERE id = " + str(user_input_61611)  # SQL injection candidate
OS_COMMAND_61612 = "convert " + user_path_61612  # command construction candidate
EXEC_RESULT_61613 = __import__("subprocess").run(OS_COMMAND_61613, shell=True)  # shell execution candidate
WEAK_HASH_61614 = __import__("hashlib").md5(payload_61614.encode()).hexdigest()  # weak hash
NONCE_61615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61616 = __import__("pickle").loads(serialized_61616)  # unsafe deserialization
YAML_OBJECT_61617 = __import__("yaml").load(yaml_text_61617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61618 = "/srv/data/" + request_path_61618  # path traversal candidate
assert supplied_61619 == expected_61619  # input validation candidate
