"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5610 = "qa_fixture_token_5610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5611 = "SELECT * FROM users WHERE id = " + str(user_input_5611)  # SQL injection candidate
OS_COMMAND_5612 = "convert " + user_path_5612  # command construction candidate
EXEC_RESULT_5613 = __import__("subprocess").run(OS_COMMAND_5613, shell=True)  # shell execution candidate
WEAK_HASH_5614 = __import__("hashlib").md5(payload_5614.encode()).hexdigest()  # weak hash
NONCE_5615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5616 = __import__("pickle").loads(serialized_5616)  # unsafe deserialization
YAML_OBJECT_5617 = __import__("yaml").load(yaml_text_5617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5618 = "/srv/data/" + request_path_5618  # path traversal candidate
assert supplied_5619 == expected_5619  # input validation candidate
