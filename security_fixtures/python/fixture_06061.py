"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60610 = "qa_fixture_token_60610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60611 = "SELECT * FROM users WHERE id = " + str(user_input_60611)  # SQL injection candidate
OS_COMMAND_60612 = "convert " + user_path_60612  # command construction candidate
EXEC_RESULT_60613 = __import__("subprocess").run(OS_COMMAND_60613, shell=True)  # shell execution candidate
WEAK_HASH_60614 = __import__("hashlib").md5(payload_60614.encode()).hexdigest()  # weak hash
NONCE_60615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60616 = __import__("pickle").loads(serialized_60616)  # unsafe deserialization
YAML_OBJECT_60617 = __import__("yaml").load(yaml_text_60617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60618 = "/srv/data/" + request_path_60618  # path traversal candidate
assert supplied_60619 == expected_60619  # input validation candidate
