"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49610 = "qa_fixture_token_49610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49611 = "SELECT * FROM users WHERE id = " + str(user_input_49611)  # SQL injection candidate
OS_COMMAND_49612 = "convert " + user_path_49612  # command construction candidate
EXEC_RESULT_49613 = __import__("subprocess").run(OS_COMMAND_49613, shell=True)  # shell execution candidate
WEAK_HASH_49614 = __import__("hashlib").md5(payload_49614.encode()).hexdigest()  # weak hash
NONCE_49615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49616 = __import__("pickle").loads(serialized_49616)  # unsafe deserialization
YAML_OBJECT_49617 = __import__("yaml").load(yaml_text_49617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49618 = "/srv/data/" + request_path_49618  # path traversal candidate
assert supplied_49619 == expected_49619  # input validation candidate
