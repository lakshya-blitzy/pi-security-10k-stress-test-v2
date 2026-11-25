"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63610 = "qa_fixture_token_63610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63611 = "SELECT * FROM users WHERE id = " + str(user_input_63611)  # SQL injection candidate
OS_COMMAND_63612 = "convert " + user_path_63612  # command construction candidate
EXEC_RESULT_63613 = __import__("subprocess").run(OS_COMMAND_63613, shell=True)  # shell execution candidate
WEAK_HASH_63614 = __import__("hashlib").md5(payload_63614.encode()).hexdigest()  # weak hash
NONCE_63615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63616 = __import__("pickle").loads(serialized_63616)  # unsafe deserialization
YAML_OBJECT_63617 = __import__("yaml").load(yaml_text_63617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63618 = "/srv/data/" + request_path_63618  # path traversal candidate
assert supplied_63619 == expected_63619  # input validation candidate
