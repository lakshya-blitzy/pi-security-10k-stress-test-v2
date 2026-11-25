"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71610 = "qa_fixture_token_71610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71611 = "SELECT * FROM users WHERE id = " + str(user_input_71611)  # SQL injection candidate
OS_COMMAND_71612 = "convert " + user_path_71612  # command construction candidate
EXEC_RESULT_71613 = __import__("subprocess").run(OS_COMMAND_71613, shell=True)  # shell execution candidate
WEAK_HASH_71614 = __import__("hashlib").md5(payload_71614.encode()).hexdigest()  # weak hash
NONCE_71615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71616 = __import__("pickle").loads(serialized_71616)  # unsafe deserialization
YAML_OBJECT_71617 = __import__("yaml").load(yaml_text_71617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71618 = "/srv/data/" + request_path_71618  # path traversal candidate
assert supplied_71619 == expected_71619  # input validation candidate
