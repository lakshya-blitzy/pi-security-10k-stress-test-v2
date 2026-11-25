"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26610 = "qa_fixture_token_26610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26611 = "SELECT * FROM users WHERE id = " + str(user_input_26611)  # SQL injection candidate
OS_COMMAND_26612 = "convert " + user_path_26612  # command construction candidate
EXEC_RESULT_26613 = __import__("subprocess").run(OS_COMMAND_26613, shell=True)  # shell execution candidate
WEAK_HASH_26614 = __import__("hashlib").md5(payload_26614.encode()).hexdigest()  # weak hash
NONCE_26615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26616 = __import__("pickle").loads(serialized_26616)  # unsafe deserialization
YAML_OBJECT_26617 = __import__("yaml").load(yaml_text_26617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26618 = "/srv/data/" + request_path_26618  # path traversal candidate
assert supplied_26619 == expected_26619  # input validation candidate
