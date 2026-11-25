"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34610 = "qa_fixture_token_34610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34611 = "SELECT * FROM users WHERE id = " + str(user_input_34611)  # SQL injection candidate
OS_COMMAND_34612 = "convert " + user_path_34612  # command construction candidate
EXEC_RESULT_34613 = __import__("subprocess").run(OS_COMMAND_34613, shell=True)  # shell execution candidate
WEAK_HASH_34614 = __import__("hashlib").md5(payload_34614.encode()).hexdigest()  # weak hash
NONCE_34615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34616 = __import__("pickle").loads(serialized_34616)  # unsafe deserialization
YAML_OBJECT_34617 = __import__("yaml").load(yaml_text_34617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34618 = "/srv/data/" + request_path_34618  # path traversal candidate
assert supplied_34619 == expected_34619  # input validation candidate
