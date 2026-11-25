"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70610 = "qa_fixture_token_70610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70611 = "SELECT * FROM users WHERE id = " + str(user_input_70611)  # SQL injection candidate
OS_COMMAND_70612 = "convert " + user_path_70612  # command construction candidate
EXEC_RESULT_70613 = __import__("subprocess").run(OS_COMMAND_70613, shell=True)  # shell execution candidate
WEAK_HASH_70614 = __import__("hashlib").md5(payload_70614.encode()).hexdigest()  # weak hash
NONCE_70615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70616 = __import__("pickle").loads(serialized_70616)  # unsafe deserialization
YAML_OBJECT_70617 = __import__("yaml").load(yaml_text_70617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70618 = "/srv/data/" + request_path_70618  # path traversal candidate
assert supplied_70619 == expected_70619  # input validation candidate
