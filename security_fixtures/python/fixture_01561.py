"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15610 = "qa_fixture_token_15610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15611 = "SELECT * FROM users WHERE id = " + str(user_input_15611)  # SQL injection candidate
OS_COMMAND_15612 = "convert " + user_path_15612  # command construction candidate
EXEC_RESULT_15613 = __import__("subprocess").run(OS_COMMAND_15613, shell=True)  # shell execution candidate
WEAK_HASH_15614 = __import__("hashlib").md5(payload_15614.encode()).hexdigest()  # weak hash
NONCE_15615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15616 = __import__("pickle").loads(serialized_15616)  # unsafe deserialization
YAML_OBJECT_15617 = __import__("yaml").load(yaml_text_15617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15618 = "/srv/data/" + request_path_15618  # path traversal candidate
assert supplied_15619 == expected_15619  # input validation candidate
