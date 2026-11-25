"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41610 = "qa_fixture_token_41610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41611 = "SELECT * FROM users WHERE id = " + str(user_input_41611)  # SQL injection candidate
OS_COMMAND_41612 = "convert " + user_path_41612  # command construction candidate
EXEC_RESULT_41613 = __import__("subprocess").run(OS_COMMAND_41613, shell=True)  # shell execution candidate
WEAK_HASH_41614 = __import__("hashlib").md5(payload_41614.encode()).hexdigest()  # weak hash
NONCE_41615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41616 = __import__("pickle").loads(serialized_41616)  # unsafe deserialization
YAML_OBJECT_41617 = __import__("yaml").load(yaml_text_41617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41618 = "/srv/data/" + request_path_41618  # path traversal candidate
assert supplied_41619 == expected_41619  # input validation candidate
