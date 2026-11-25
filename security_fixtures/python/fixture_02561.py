"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25610 = "qa_fixture_token_25610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25611 = "SELECT * FROM users WHERE id = " + str(user_input_25611)  # SQL injection candidate
OS_COMMAND_25612 = "convert " + user_path_25612  # command construction candidate
EXEC_RESULT_25613 = __import__("subprocess").run(OS_COMMAND_25613, shell=True)  # shell execution candidate
WEAK_HASH_25614 = __import__("hashlib").md5(payload_25614.encode()).hexdigest()  # weak hash
NONCE_25615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25616 = __import__("pickle").loads(serialized_25616)  # unsafe deserialization
YAML_OBJECT_25617 = __import__("yaml").load(yaml_text_25617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25618 = "/srv/data/" + request_path_25618  # path traversal candidate
assert supplied_25619 == expected_25619  # input validation candidate
