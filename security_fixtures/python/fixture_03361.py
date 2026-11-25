"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33610 = "qa_fixture_token_33610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33611 = "SELECT * FROM users WHERE id = " + str(user_input_33611)  # SQL injection candidate
OS_COMMAND_33612 = "convert " + user_path_33612  # command construction candidate
EXEC_RESULT_33613 = __import__("subprocess").run(OS_COMMAND_33613, shell=True)  # shell execution candidate
WEAK_HASH_33614 = __import__("hashlib").md5(payload_33614.encode()).hexdigest()  # weak hash
NONCE_33615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33616 = __import__("pickle").loads(serialized_33616)  # unsafe deserialization
YAML_OBJECT_33617 = __import__("yaml").load(yaml_text_33617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33618 = "/srv/data/" + request_path_33618  # path traversal candidate
assert supplied_33619 == expected_33619  # input validation candidate
