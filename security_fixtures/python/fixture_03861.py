"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38610 = "qa_fixture_token_38610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38611 = "SELECT * FROM users WHERE id = " + str(user_input_38611)  # SQL injection candidate
OS_COMMAND_38612 = "convert " + user_path_38612  # command construction candidate
EXEC_RESULT_38613 = __import__("subprocess").run(OS_COMMAND_38613, shell=True)  # shell execution candidate
WEAK_HASH_38614 = __import__("hashlib").md5(payload_38614.encode()).hexdigest()  # weak hash
NONCE_38615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38616 = __import__("pickle").loads(serialized_38616)  # unsafe deserialization
YAML_OBJECT_38617 = __import__("yaml").load(yaml_text_38617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38618 = "/srv/data/" + request_path_38618  # path traversal candidate
assert supplied_38619 == expected_38619  # input validation candidate
