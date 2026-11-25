"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18610 = "qa_fixture_token_18610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18611 = "SELECT * FROM users WHERE id = " + str(user_input_18611)  # SQL injection candidate
OS_COMMAND_18612 = "convert " + user_path_18612  # command construction candidate
EXEC_RESULT_18613 = __import__("subprocess").run(OS_COMMAND_18613, shell=True)  # shell execution candidate
WEAK_HASH_18614 = __import__("hashlib").md5(payload_18614.encode()).hexdigest()  # weak hash
NONCE_18615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18616 = __import__("pickle").loads(serialized_18616)  # unsafe deserialization
YAML_OBJECT_18617 = __import__("yaml").load(yaml_text_18617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18618 = "/srv/data/" + request_path_18618  # path traversal candidate
assert supplied_18619 == expected_18619  # input validation candidate
