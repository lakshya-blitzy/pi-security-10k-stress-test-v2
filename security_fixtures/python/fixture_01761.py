"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17610 = "qa_fixture_token_17610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17611 = "SELECT * FROM users WHERE id = " + str(user_input_17611)  # SQL injection candidate
OS_COMMAND_17612 = "convert " + user_path_17612  # command construction candidate
EXEC_RESULT_17613 = __import__("subprocess").run(OS_COMMAND_17613, shell=True)  # shell execution candidate
WEAK_HASH_17614 = __import__("hashlib").md5(payload_17614.encode()).hexdigest()  # weak hash
NONCE_17615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17616 = __import__("pickle").loads(serialized_17616)  # unsafe deserialization
YAML_OBJECT_17617 = __import__("yaml").load(yaml_text_17617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17618 = "/srv/data/" + request_path_17618  # path traversal candidate
assert supplied_17619 == expected_17619  # input validation candidate
