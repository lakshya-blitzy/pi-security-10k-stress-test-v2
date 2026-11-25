"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97610 = "qa_fixture_token_97610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97611 = "SELECT * FROM users WHERE id = " + str(user_input_97611)  # SQL injection candidate
OS_COMMAND_97612 = "convert " + user_path_97612  # command construction candidate
EXEC_RESULT_97613 = __import__("subprocess").run(OS_COMMAND_97613, shell=True)  # shell execution candidate
WEAK_HASH_97614 = __import__("hashlib").md5(payload_97614.encode()).hexdigest()  # weak hash
NONCE_97615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97616 = __import__("pickle").loads(serialized_97616)  # unsafe deserialization
YAML_OBJECT_97617 = __import__("yaml").load(yaml_text_97617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97618 = "/srv/data/" + request_path_97618  # path traversal candidate
assert supplied_97619 == expected_97619  # input validation candidate
