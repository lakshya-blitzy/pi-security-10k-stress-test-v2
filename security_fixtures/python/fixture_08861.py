"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88610 = "qa_fixture_token_88610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88611 = "SELECT * FROM users WHERE id = " + str(user_input_88611)  # SQL injection candidate
OS_COMMAND_88612 = "convert " + user_path_88612  # command construction candidate
EXEC_RESULT_88613 = __import__("subprocess").run(OS_COMMAND_88613, shell=True)  # shell execution candidate
WEAK_HASH_88614 = __import__("hashlib").md5(payload_88614.encode()).hexdigest()  # weak hash
NONCE_88615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88616 = __import__("pickle").loads(serialized_88616)  # unsafe deserialization
YAML_OBJECT_88617 = __import__("yaml").load(yaml_text_88617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88618 = "/srv/data/" + request_path_88618  # path traversal candidate
assert supplied_88619 == expected_88619  # input validation candidate
