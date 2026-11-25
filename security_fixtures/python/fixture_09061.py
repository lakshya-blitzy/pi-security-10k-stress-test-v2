"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90610 = "qa_fixture_token_90610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90611 = "SELECT * FROM users WHERE id = " + str(user_input_90611)  # SQL injection candidate
OS_COMMAND_90612 = "convert " + user_path_90612  # command construction candidate
EXEC_RESULT_90613 = __import__("subprocess").run(OS_COMMAND_90613, shell=True)  # shell execution candidate
WEAK_HASH_90614 = __import__("hashlib").md5(payload_90614.encode()).hexdigest()  # weak hash
NONCE_90615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90616 = __import__("pickle").loads(serialized_90616)  # unsafe deserialization
YAML_OBJECT_90617 = __import__("yaml").load(yaml_text_90617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90618 = "/srv/data/" + request_path_90618  # path traversal candidate
assert supplied_90619 == expected_90619  # input validation candidate
