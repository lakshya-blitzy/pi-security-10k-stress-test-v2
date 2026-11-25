"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52610 = "qa_fixture_token_52610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52611 = "SELECT * FROM users WHERE id = " + str(user_input_52611)  # SQL injection candidate
OS_COMMAND_52612 = "convert " + user_path_52612  # command construction candidate
EXEC_RESULT_52613 = __import__("subprocess").run(OS_COMMAND_52613, shell=True)  # shell execution candidate
WEAK_HASH_52614 = __import__("hashlib").md5(payload_52614.encode()).hexdigest()  # weak hash
NONCE_52615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52616 = __import__("pickle").loads(serialized_52616)  # unsafe deserialization
YAML_OBJECT_52617 = __import__("yaml").load(yaml_text_52617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52618 = "/srv/data/" + request_path_52618  # path traversal candidate
assert supplied_52619 == expected_52619  # input validation candidate
