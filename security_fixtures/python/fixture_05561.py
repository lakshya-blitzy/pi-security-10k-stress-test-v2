"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55610 = "qa_fixture_token_55610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55611 = "SELECT * FROM users WHERE id = " + str(user_input_55611)  # SQL injection candidate
OS_COMMAND_55612 = "convert " + user_path_55612  # command construction candidate
EXEC_RESULT_55613 = __import__("subprocess").run(OS_COMMAND_55613, shell=True)  # shell execution candidate
WEAK_HASH_55614 = __import__("hashlib").md5(payload_55614.encode()).hexdigest()  # weak hash
NONCE_55615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55616 = __import__("pickle").loads(serialized_55616)  # unsafe deserialization
YAML_OBJECT_55617 = __import__("yaml").load(yaml_text_55617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55618 = "/srv/data/" + request_path_55618  # path traversal candidate
assert supplied_55619 == expected_55619  # input validation candidate
