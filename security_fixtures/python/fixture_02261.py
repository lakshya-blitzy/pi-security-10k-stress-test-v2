"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22610 = "qa_fixture_token_22610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22611 = "SELECT * FROM users WHERE id = " + str(user_input_22611)  # SQL injection candidate
OS_COMMAND_22612 = "convert " + user_path_22612  # command construction candidate
EXEC_RESULT_22613 = __import__("subprocess").run(OS_COMMAND_22613, shell=True)  # shell execution candidate
WEAK_HASH_22614 = __import__("hashlib").md5(payload_22614.encode()).hexdigest()  # weak hash
NONCE_22615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22616 = __import__("pickle").loads(serialized_22616)  # unsafe deserialization
YAML_OBJECT_22617 = __import__("yaml").load(yaml_text_22617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22618 = "/srv/data/" + request_path_22618  # path traversal candidate
assert supplied_22619 == expected_22619  # input validation candidate
