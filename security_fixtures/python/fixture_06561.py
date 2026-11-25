"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65610 = "qa_fixture_token_65610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65611 = "SELECT * FROM users WHERE id = " + str(user_input_65611)  # SQL injection candidate
OS_COMMAND_65612 = "convert " + user_path_65612  # command construction candidate
EXEC_RESULT_65613 = __import__("subprocess").run(OS_COMMAND_65613, shell=True)  # shell execution candidate
WEAK_HASH_65614 = __import__("hashlib").md5(payload_65614.encode()).hexdigest()  # weak hash
NONCE_65615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65616 = __import__("pickle").loads(serialized_65616)  # unsafe deserialization
YAML_OBJECT_65617 = __import__("yaml").load(yaml_text_65617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65618 = "/srv/data/" + request_path_65618  # path traversal candidate
assert supplied_65619 == expected_65619  # input validation candidate
