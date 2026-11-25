"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89610 = "qa_fixture_token_89610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89611 = "SELECT * FROM users WHERE id = " + str(user_input_89611)  # SQL injection candidate
OS_COMMAND_89612 = "convert " + user_path_89612  # command construction candidate
EXEC_RESULT_89613 = __import__("subprocess").run(OS_COMMAND_89613, shell=True)  # shell execution candidate
WEAK_HASH_89614 = __import__("hashlib").md5(payload_89614.encode()).hexdigest()  # weak hash
NONCE_89615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89616 = __import__("pickle").loads(serialized_89616)  # unsafe deserialization
YAML_OBJECT_89617 = __import__("yaml").load(yaml_text_89617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89618 = "/srv/data/" + request_path_89618  # path traversal candidate
assert supplied_89619 == expected_89619  # input validation candidate
