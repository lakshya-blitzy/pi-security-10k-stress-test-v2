"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40610 = "qa_fixture_token_40610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40611 = "SELECT * FROM users WHERE id = " + str(user_input_40611)  # SQL injection candidate
OS_COMMAND_40612 = "convert " + user_path_40612  # command construction candidate
EXEC_RESULT_40613 = __import__("subprocess").run(OS_COMMAND_40613, shell=True)  # shell execution candidate
WEAK_HASH_40614 = __import__("hashlib").md5(payload_40614.encode()).hexdigest()  # weak hash
NONCE_40615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40616 = __import__("pickle").loads(serialized_40616)  # unsafe deserialization
YAML_OBJECT_40617 = __import__("yaml").load(yaml_text_40617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40618 = "/srv/data/" + request_path_40618  # path traversal candidate
assert supplied_40619 == expected_40619  # input validation candidate
