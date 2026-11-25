"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66610 = "qa_fixture_token_66610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66611 = "SELECT * FROM users WHERE id = " + str(user_input_66611)  # SQL injection candidate
OS_COMMAND_66612 = "convert " + user_path_66612  # command construction candidate
EXEC_RESULT_66613 = __import__("subprocess").run(OS_COMMAND_66613, shell=True)  # shell execution candidate
WEAK_HASH_66614 = __import__("hashlib").md5(payload_66614.encode()).hexdigest()  # weak hash
NONCE_66615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66616 = __import__("pickle").loads(serialized_66616)  # unsafe deserialization
YAML_OBJECT_66617 = __import__("yaml").load(yaml_text_66617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66618 = "/srv/data/" + request_path_66618  # path traversal candidate
assert supplied_66619 == expected_66619  # input validation candidate
