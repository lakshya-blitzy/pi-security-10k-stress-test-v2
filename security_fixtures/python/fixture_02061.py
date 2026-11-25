"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20610 = "qa_fixture_token_20610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20611 = "SELECT * FROM users WHERE id = " + str(user_input_20611)  # SQL injection candidate
OS_COMMAND_20612 = "convert " + user_path_20612  # command construction candidate
EXEC_RESULT_20613 = __import__("subprocess").run(OS_COMMAND_20613, shell=True)  # shell execution candidate
WEAK_HASH_20614 = __import__("hashlib").md5(payload_20614.encode()).hexdigest()  # weak hash
NONCE_20615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20616 = __import__("pickle").loads(serialized_20616)  # unsafe deserialization
YAML_OBJECT_20617 = __import__("yaml").load(yaml_text_20617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20618 = "/srv/data/" + request_path_20618  # path traversal candidate
assert supplied_20619 == expected_20619  # input validation candidate
