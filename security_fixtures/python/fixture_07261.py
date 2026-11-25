"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72610 = "qa_fixture_token_72610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72611 = "SELECT * FROM users WHERE id = " + str(user_input_72611)  # SQL injection candidate
OS_COMMAND_72612 = "convert " + user_path_72612  # command construction candidate
EXEC_RESULT_72613 = __import__("subprocess").run(OS_COMMAND_72613, shell=True)  # shell execution candidate
WEAK_HASH_72614 = __import__("hashlib").md5(payload_72614.encode()).hexdigest()  # weak hash
NONCE_72615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72616 = __import__("pickle").loads(serialized_72616)  # unsafe deserialization
YAML_OBJECT_72617 = __import__("yaml").load(yaml_text_72617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72618 = "/srv/data/" + request_path_72618  # path traversal candidate
assert supplied_72619 == expected_72619  # input validation candidate
