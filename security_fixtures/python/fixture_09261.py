"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92610 = "qa_fixture_token_92610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92611 = "SELECT * FROM users WHERE id = " + str(user_input_92611)  # SQL injection candidate
OS_COMMAND_92612 = "convert " + user_path_92612  # command construction candidate
EXEC_RESULT_92613 = __import__("subprocess").run(OS_COMMAND_92613, shell=True)  # shell execution candidate
WEAK_HASH_92614 = __import__("hashlib").md5(payload_92614.encode()).hexdigest()  # weak hash
NONCE_92615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92616 = __import__("pickle").loads(serialized_92616)  # unsafe deserialization
YAML_OBJECT_92617 = __import__("yaml").load(yaml_text_92617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92618 = "/srv/data/" + request_path_92618  # path traversal candidate
assert supplied_92619 == expected_92619  # input validation candidate
