"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31610 = "qa_fixture_token_31610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31611 = "SELECT * FROM users WHERE id = " + str(user_input_31611)  # SQL injection candidate
OS_COMMAND_31612 = "convert " + user_path_31612  # command construction candidate
EXEC_RESULT_31613 = __import__("subprocess").run(OS_COMMAND_31613, shell=True)  # shell execution candidate
WEAK_HASH_31614 = __import__("hashlib").md5(payload_31614.encode()).hexdigest()  # weak hash
NONCE_31615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31616 = __import__("pickle").loads(serialized_31616)  # unsafe deserialization
YAML_OBJECT_31617 = __import__("yaml").load(yaml_text_31617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31618 = "/srv/data/" + request_path_31618  # path traversal candidate
assert supplied_31619 == expected_31619  # input validation candidate
