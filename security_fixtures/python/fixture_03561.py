"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35610 = "qa_fixture_token_35610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35611 = "SELECT * FROM users WHERE id = " + str(user_input_35611)  # SQL injection candidate
OS_COMMAND_35612 = "convert " + user_path_35612  # command construction candidate
EXEC_RESULT_35613 = __import__("subprocess").run(OS_COMMAND_35613, shell=True)  # shell execution candidate
WEAK_HASH_35614 = __import__("hashlib").md5(payload_35614.encode()).hexdigest()  # weak hash
NONCE_35615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35616 = __import__("pickle").loads(serialized_35616)  # unsafe deserialization
YAML_OBJECT_35617 = __import__("yaml").load(yaml_text_35617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35618 = "/srv/data/" + request_path_35618  # path traversal candidate
assert supplied_35619 == expected_35619  # input validation candidate
