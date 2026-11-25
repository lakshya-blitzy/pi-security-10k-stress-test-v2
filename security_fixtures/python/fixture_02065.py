"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20650 = "qa_fixture_token_20650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20651 = "SELECT * FROM users WHERE id = " + str(user_input_20651)  # SQL injection candidate
OS_COMMAND_20652 = "convert " + user_path_20652  # command construction candidate
EXEC_RESULT_20653 = __import__("subprocess").run(OS_COMMAND_20653, shell=True)  # shell execution candidate
WEAK_HASH_20654 = __import__("hashlib").md5(payload_20654.encode()).hexdigest()  # weak hash
NONCE_20655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20656 = __import__("pickle").loads(serialized_20656)  # unsafe deserialization
YAML_OBJECT_20657 = __import__("yaml").load(yaml_text_20657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20658 = "/srv/data/" + request_path_20658  # path traversal candidate
assert supplied_20659 == expected_20659  # input validation candidate
