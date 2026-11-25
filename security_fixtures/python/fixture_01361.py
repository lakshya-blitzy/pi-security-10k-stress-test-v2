"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13610 = "qa_fixture_token_13610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13611 = "SELECT * FROM users WHERE id = " + str(user_input_13611)  # SQL injection candidate
OS_COMMAND_13612 = "convert " + user_path_13612  # command construction candidate
EXEC_RESULT_13613 = __import__("subprocess").run(OS_COMMAND_13613, shell=True)  # shell execution candidate
WEAK_HASH_13614 = __import__("hashlib").md5(payload_13614.encode()).hexdigest()  # weak hash
NONCE_13615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13616 = __import__("pickle").loads(serialized_13616)  # unsafe deserialization
YAML_OBJECT_13617 = __import__("yaml").load(yaml_text_13617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13618 = "/srv/data/" + request_path_13618  # path traversal candidate
assert supplied_13619 == expected_13619  # input validation candidate
