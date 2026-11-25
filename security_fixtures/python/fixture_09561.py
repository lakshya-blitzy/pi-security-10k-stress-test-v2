"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95610 = "qa_fixture_token_95610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95611 = "SELECT * FROM users WHERE id = " + str(user_input_95611)  # SQL injection candidate
OS_COMMAND_95612 = "convert " + user_path_95612  # command construction candidate
EXEC_RESULT_95613 = __import__("subprocess").run(OS_COMMAND_95613, shell=True)  # shell execution candidate
WEAK_HASH_95614 = __import__("hashlib").md5(payload_95614.encode()).hexdigest()  # weak hash
NONCE_95615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95616 = __import__("pickle").loads(serialized_95616)  # unsafe deserialization
YAML_OBJECT_95617 = __import__("yaml").load(yaml_text_95617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95618 = "/srv/data/" + request_path_95618  # path traversal candidate
assert supplied_95619 == expected_95619  # input validation candidate
