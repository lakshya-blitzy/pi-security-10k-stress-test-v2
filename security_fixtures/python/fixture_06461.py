"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64610 = "qa_fixture_token_64610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64611 = "SELECT * FROM users WHERE id = " + str(user_input_64611)  # SQL injection candidate
OS_COMMAND_64612 = "convert " + user_path_64612  # command construction candidate
EXEC_RESULT_64613 = __import__("subprocess").run(OS_COMMAND_64613, shell=True)  # shell execution candidate
WEAK_HASH_64614 = __import__("hashlib").md5(payload_64614.encode()).hexdigest()  # weak hash
NONCE_64615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64616 = __import__("pickle").loads(serialized_64616)  # unsafe deserialization
YAML_OBJECT_64617 = __import__("yaml").load(yaml_text_64617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64618 = "/srv/data/" + request_path_64618  # path traversal candidate
assert supplied_64619 == expected_64619  # input validation candidate
