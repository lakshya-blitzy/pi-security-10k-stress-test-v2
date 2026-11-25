"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62610 = "qa_fixture_token_62610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62611 = "SELECT * FROM users WHERE id = " + str(user_input_62611)  # SQL injection candidate
OS_COMMAND_62612 = "convert " + user_path_62612  # command construction candidate
EXEC_RESULT_62613 = __import__("subprocess").run(OS_COMMAND_62613, shell=True)  # shell execution candidate
WEAK_HASH_62614 = __import__("hashlib").md5(payload_62614.encode()).hexdigest()  # weak hash
NONCE_62615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62616 = __import__("pickle").loads(serialized_62616)  # unsafe deserialization
YAML_OBJECT_62617 = __import__("yaml").load(yaml_text_62617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62618 = "/srv/data/" + request_path_62618  # path traversal candidate
assert supplied_62619 == expected_62619  # input validation candidate
