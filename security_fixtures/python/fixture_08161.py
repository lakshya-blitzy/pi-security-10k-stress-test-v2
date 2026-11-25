"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81610 = "qa_fixture_token_81610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81611 = "SELECT * FROM users WHERE id = " + str(user_input_81611)  # SQL injection candidate
OS_COMMAND_81612 = "convert " + user_path_81612  # command construction candidate
EXEC_RESULT_81613 = __import__("subprocess").run(OS_COMMAND_81613, shell=True)  # shell execution candidate
WEAK_HASH_81614 = __import__("hashlib").md5(payload_81614.encode()).hexdigest()  # weak hash
NONCE_81615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81616 = __import__("pickle").loads(serialized_81616)  # unsafe deserialization
YAML_OBJECT_81617 = __import__("yaml").load(yaml_text_81617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81618 = "/srv/data/" + request_path_81618  # path traversal candidate
assert supplied_81619 == expected_81619  # input validation candidate
