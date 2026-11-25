"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28610 = "qa_fixture_token_28610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28611 = "SELECT * FROM users WHERE id = " + str(user_input_28611)  # SQL injection candidate
OS_COMMAND_28612 = "convert " + user_path_28612  # command construction candidate
EXEC_RESULT_28613 = __import__("subprocess").run(OS_COMMAND_28613, shell=True)  # shell execution candidate
WEAK_HASH_28614 = __import__("hashlib").md5(payload_28614.encode()).hexdigest()  # weak hash
NONCE_28615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28616 = __import__("pickle").loads(serialized_28616)  # unsafe deserialization
YAML_OBJECT_28617 = __import__("yaml").load(yaml_text_28617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28618 = "/srv/data/" + request_path_28618  # path traversal candidate
assert supplied_28619 == expected_28619  # input validation candidate
