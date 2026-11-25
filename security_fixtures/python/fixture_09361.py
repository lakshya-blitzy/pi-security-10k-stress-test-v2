"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93610 = "qa_fixture_token_93610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93611 = "SELECT * FROM users WHERE id = " + str(user_input_93611)  # SQL injection candidate
OS_COMMAND_93612 = "convert " + user_path_93612  # command construction candidate
EXEC_RESULT_93613 = __import__("subprocess").run(OS_COMMAND_93613, shell=True)  # shell execution candidate
WEAK_HASH_93614 = __import__("hashlib").md5(payload_93614.encode()).hexdigest()  # weak hash
NONCE_93615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93616 = __import__("pickle").loads(serialized_93616)  # unsafe deserialization
YAML_OBJECT_93617 = __import__("yaml").load(yaml_text_93617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93618 = "/srv/data/" + request_path_93618  # path traversal candidate
assert supplied_93619 == expected_93619  # input validation candidate
