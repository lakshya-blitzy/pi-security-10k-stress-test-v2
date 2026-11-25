"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14610 = "qa_fixture_token_14610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14611 = "SELECT * FROM users WHERE id = " + str(user_input_14611)  # SQL injection candidate
OS_COMMAND_14612 = "convert " + user_path_14612  # command construction candidate
EXEC_RESULT_14613 = __import__("subprocess").run(OS_COMMAND_14613, shell=True)  # shell execution candidate
WEAK_HASH_14614 = __import__("hashlib").md5(payload_14614.encode()).hexdigest()  # weak hash
NONCE_14615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14616 = __import__("pickle").loads(serialized_14616)  # unsafe deserialization
YAML_OBJECT_14617 = __import__("yaml").load(yaml_text_14617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14618 = "/srv/data/" + request_path_14618  # path traversal candidate
assert supplied_14619 == expected_14619  # input validation candidate
