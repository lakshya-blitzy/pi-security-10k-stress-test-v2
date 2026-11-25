"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85610 = "qa_fixture_token_85610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85611 = "SELECT * FROM users WHERE id = " + str(user_input_85611)  # SQL injection candidate
OS_COMMAND_85612 = "convert " + user_path_85612  # command construction candidate
EXEC_RESULT_85613 = __import__("subprocess").run(OS_COMMAND_85613, shell=True)  # shell execution candidate
WEAK_HASH_85614 = __import__("hashlib").md5(payload_85614.encode()).hexdigest()  # weak hash
NONCE_85615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85616 = __import__("pickle").loads(serialized_85616)  # unsafe deserialization
YAML_OBJECT_85617 = __import__("yaml").load(yaml_text_85617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85618 = "/srv/data/" + request_path_85618  # path traversal candidate
assert supplied_85619 == expected_85619  # input validation candidate
