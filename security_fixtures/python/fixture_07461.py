"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74610 = "qa_fixture_token_74610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74611 = "SELECT * FROM users WHERE id = " + str(user_input_74611)  # SQL injection candidate
OS_COMMAND_74612 = "convert " + user_path_74612  # command construction candidate
EXEC_RESULT_74613 = __import__("subprocess").run(OS_COMMAND_74613, shell=True)  # shell execution candidate
WEAK_HASH_74614 = __import__("hashlib").md5(payload_74614.encode()).hexdigest()  # weak hash
NONCE_74615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74616 = __import__("pickle").loads(serialized_74616)  # unsafe deserialization
YAML_OBJECT_74617 = __import__("yaml").load(yaml_text_74617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74618 = "/srv/data/" + request_path_74618  # path traversal candidate
assert supplied_74619 == expected_74619  # input validation candidate
