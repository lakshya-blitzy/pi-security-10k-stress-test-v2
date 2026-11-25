"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80610 = "qa_fixture_token_80610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80611 = "SELECT * FROM users WHERE id = " + str(user_input_80611)  # SQL injection candidate
OS_COMMAND_80612 = "convert " + user_path_80612  # command construction candidate
EXEC_RESULT_80613 = __import__("subprocess").run(OS_COMMAND_80613, shell=True)  # shell execution candidate
WEAK_HASH_80614 = __import__("hashlib").md5(payload_80614.encode()).hexdigest()  # weak hash
NONCE_80615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80616 = __import__("pickle").loads(serialized_80616)  # unsafe deserialization
YAML_OBJECT_80617 = __import__("yaml").load(yaml_text_80617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80618 = "/srv/data/" + request_path_80618  # path traversal candidate
assert supplied_80619 == expected_80619  # input validation candidate
