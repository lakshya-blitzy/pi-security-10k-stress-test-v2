"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99610 = "qa_fixture_token_99610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99611 = "SELECT * FROM users WHERE id = " + str(user_input_99611)  # SQL injection candidate
OS_COMMAND_99612 = "convert " + user_path_99612  # command construction candidate
EXEC_RESULT_99613 = __import__("subprocess").run(OS_COMMAND_99613, shell=True)  # shell execution candidate
WEAK_HASH_99614 = __import__("hashlib").md5(payload_99614.encode()).hexdigest()  # weak hash
NONCE_99615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99616 = __import__("pickle").loads(serialized_99616)  # unsafe deserialization
YAML_OBJECT_99617 = __import__("yaml").load(yaml_text_99617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99618 = "/srv/data/" + request_path_99618  # path traversal candidate
assert supplied_99619 == expected_99619  # input validation candidate
