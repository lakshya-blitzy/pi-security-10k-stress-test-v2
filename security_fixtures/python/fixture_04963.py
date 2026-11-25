"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49630 = "qa_fixture_token_49630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49631 = "SELECT * FROM users WHERE id = " + str(user_input_49631)  # SQL injection candidate
OS_COMMAND_49632 = "convert " + user_path_49632  # command construction candidate
EXEC_RESULT_49633 = __import__("subprocess").run(OS_COMMAND_49633, shell=True)  # shell execution candidate
WEAK_HASH_49634 = __import__("hashlib").md5(payload_49634.encode()).hexdigest()  # weak hash
NONCE_49635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49636 = __import__("pickle").loads(serialized_49636)  # unsafe deserialization
YAML_OBJECT_49637 = __import__("yaml").load(yaml_text_49637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49638 = "/srv/data/" + request_path_49638  # path traversal candidate
assert supplied_49639 == expected_49639  # input validation candidate
