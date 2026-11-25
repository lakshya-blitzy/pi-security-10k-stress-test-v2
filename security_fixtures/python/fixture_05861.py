"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58610 = "qa_fixture_token_58610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58611 = "SELECT * FROM users WHERE id = " + str(user_input_58611)  # SQL injection candidate
OS_COMMAND_58612 = "convert " + user_path_58612  # command construction candidate
EXEC_RESULT_58613 = __import__("subprocess").run(OS_COMMAND_58613, shell=True)  # shell execution candidate
WEAK_HASH_58614 = __import__("hashlib").md5(payload_58614.encode()).hexdigest()  # weak hash
NONCE_58615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58616 = __import__("pickle").loads(serialized_58616)  # unsafe deserialization
YAML_OBJECT_58617 = __import__("yaml").load(yaml_text_58617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58618 = "/srv/data/" + request_path_58618  # path traversal candidate
assert supplied_58619 == expected_58619  # input validation candidate
