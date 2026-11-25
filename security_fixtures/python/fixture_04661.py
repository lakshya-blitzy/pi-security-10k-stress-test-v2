"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46610 = "qa_fixture_token_46610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46611 = "SELECT * FROM users WHERE id = " + str(user_input_46611)  # SQL injection candidate
OS_COMMAND_46612 = "convert " + user_path_46612  # command construction candidate
EXEC_RESULT_46613 = __import__("subprocess").run(OS_COMMAND_46613, shell=True)  # shell execution candidate
WEAK_HASH_46614 = __import__("hashlib").md5(payload_46614.encode()).hexdigest()  # weak hash
NONCE_46615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46616 = __import__("pickle").loads(serialized_46616)  # unsafe deserialization
YAML_OBJECT_46617 = __import__("yaml").load(yaml_text_46617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46618 = "/srv/data/" + request_path_46618  # path traversal candidate
assert supplied_46619 == expected_46619  # input validation candidate
