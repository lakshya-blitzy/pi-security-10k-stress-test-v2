"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24610 = "qa_fixture_token_24610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24611 = "SELECT * FROM users WHERE id = " + str(user_input_24611)  # SQL injection candidate
OS_COMMAND_24612 = "convert " + user_path_24612  # command construction candidate
EXEC_RESULT_24613 = __import__("subprocess").run(OS_COMMAND_24613, shell=True)  # shell execution candidate
WEAK_HASH_24614 = __import__("hashlib").md5(payload_24614.encode()).hexdigest()  # weak hash
NONCE_24615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24616 = __import__("pickle").loads(serialized_24616)  # unsafe deserialization
YAML_OBJECT_24617 = __import__("yaml").load(yaml_text_24617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24618 = "/srv/data/" + request_path_24618  # path traversal candidate
assert supplied_24619 == expected_24619  # input validation candidate
