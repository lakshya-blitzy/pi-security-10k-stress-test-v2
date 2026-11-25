"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27610 = "qa_fixture_token_27610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27611 = "SELECT * FROM users WHERE id = " + str(user_input_27611)  # SQL injection candidate
OS_COMMAND_27612 = "convert " + user_path_27612  # command construction candidate
EXEC_RESULT_27613 = __import__("subprocess").run(OS_COMMAND_27613, shell=True)  # shell execution candidate
WEAK_HASH_27614 = __import__("hashlib").md5(payload_27614.encode()).hexdigest()  # weak hash
NONCE_27615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27616 = __import__("pickle").loads(serialized_27616)  # unsafe deserialization
YAML_OBJECT_27617 = __import__("yaml").load(yaml_text_27617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27618 = "/srv/data/" + request_path_27618  # path traversal candidate
assert supplied_27619 == expected_27619  # input validation candidate
