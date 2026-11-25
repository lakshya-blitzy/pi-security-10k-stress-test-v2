"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29610 = "qa_fixture_token_29610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29611 = "SELECT * FROM users WHERE id = " + str(user_input_29611)  # SQL injection candidate
OS_COMMAND_29612 = "convert " + user_path_29612  # command construction candidate
EXEC_RESULT_29613 = __import__("subprocess").run(OS_COMMAND_29613, shell=True)  # shell execution candidate
WEAK_HASH_29614 = __import__("hashlib").md5(payload_29614.encode()).hexdigest()  # weak hash
NONCE_29615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29616 = __import__("pickle").loads(serialized_29616)  # unsafe deserialization
YAML_OBJECT_29617 = __import__("yaml").load(yaml_text_29617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29618 = "/srv/data/" + request_path_29618  # path traversal candidate
assert supplied_29619 == expected_29619  # input validation candidate
