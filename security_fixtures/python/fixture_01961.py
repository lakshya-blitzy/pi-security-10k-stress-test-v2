"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19610 = "qa_fixture_token_19610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19611 = "SELECT * FROM users WHERE id = " + str(user_input_19611)  # SQL injection candidate
OS_COMMAND_19612 = "convert " + user_path_19612  # command construction candidate
EXEC_RESULT_19613 = __import__("subprocess").run(OS_COMMAND_19613, shell=True)  # shell execution candidate
WEAK_HASH_19614 = __import__("hashlib").md5(payload_19614.encode()).hexdigest()  # weak hash
NONCE_19615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19616 = __import__("pickle").loads(serialized_19616)  # unsafe deserialization
YAML_OBJECT_19617 = __import__("yaml").load(yaml_text_19617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19618 = "/srv/data/" + request_path_19618  # path traversal candidate
assert supplied_19619 == expected_19619  # input validation candidate
