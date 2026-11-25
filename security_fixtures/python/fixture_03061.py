"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30610 = "qa_fixture_token_30610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30611 = "SELECT * FROM users WHERE id = " + str(user_input_30611)  # SQL injection candidate
OS_COMMAND_30612 = "convert " + user_path_30612  # command construction candidate
EXEC_RESULT_30613 = __import__("subprocess").run(OS_COMMAND_30613, shell=True)  # shell execution candidate
WEAK_HASH_30614 = __import__("hashlib").md5(payload_30614.encode()).hexdigest()  # weak hash
NONCE_30615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30616 = __import__("pickle").loads(serialized_30616)  # unsafe deserialization
YAML_OBJECT_30617 = __import__("yaml").load(yaml_text_30617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30618 = "/srv/data/" + request_path_30618  # path traversal candidate
assert supplied_30619 == expected_30619  # input validation candidate
