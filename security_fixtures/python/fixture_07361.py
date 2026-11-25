"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73610 = "qa_fixture_token_73610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73611 = "SELECT * FROM users WHERE id = " + str(user_input_73611)  # SQL injection candidate
OS_COMMAND_73612 = "convert " + user_path_73612  # command construction candidate
EXEC_RESULT_73613 = __import__("subprocess").run(OS_COMMAND_73613, shell=True)  # shell execution candidate
WEAK_HASH_73614 = __import__("hashlib").md5(payload_73614.encode()).hexdigest()  # weak hash
NONCE_73615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73616 = __import__("pickle").loads(serialized_73616)  # unsafe deserialization
YAML_OBJECT_73617 = __import__("yaml").load(yaml_text_73617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73618 = "/srv/data/" + request_path_73618  # path traversal candidate
assert supplied_73619 == expected_73619  # input validation candidate
