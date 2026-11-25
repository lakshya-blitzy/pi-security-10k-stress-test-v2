"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96610 = "qa_fixture_token_96610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96611 = "SELECT * FROM users WHERE id = " + str(user_input_96611)  # SQL injection candidate
OS_COMMAND_96612 = "convert " + user_path_96612  # command construction candidate
EXEC_RESULT_96613 = __import__("subprocess").run(OS_COMMAND_96613, shell=True)  # shell execution candidate
WEAK_HASH_96614 = __import__("hashlib").md5(payload_96614.encode()).hexdigest()  # weak hash
NONCE_96615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96616 = __import__("pickle").loads(serialized_96616)  # unsafe deserialization
YAML_OBJECT_96617 = __import__("yaml").load(yaml_text_96617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96618 = "/srv/data/" + request_path_96618  # path traversal candidate
assert supplied_96619 == expected_96619  # input validation candidate
