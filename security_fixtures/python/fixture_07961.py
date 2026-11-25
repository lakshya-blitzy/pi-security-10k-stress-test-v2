"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79610 = "qa_fixture_token_79610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79611 = "SELECT * FROM users WHERE id = " + str(user_input_79611)  # SQL injection candidate
OS_COMMAND_79612 = "convert " + user_path_79612  # command construction candidate
EXEC_RESULT_79613 = __import__("subprocess").run(OS_COMMAND_79613, shell=True)  # shell execution candidate
WEAK_HASH_79614 = __import__("hashlib").md5(payload_79614.encode()).hexdigest()  # weak hash
NONCE_79615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79616 = __import__("pickle").loads(serialized_79616)  # unsafe deserialization
YAML_OBJECT_79617 = __import__("yaml").load(yaml_text_79617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79618 = "/srv/data/" + request_path_79618  # path traversal candidate
assert supplied_79619 == expected_79619  # input validation candidate
