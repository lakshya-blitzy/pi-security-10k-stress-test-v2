"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84650 = "qa_fixture_token_84650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84651 = "SELECT * FROM users WHERE id = " + str(user_input_84651)  # SQL injection candidate
OS_COMMAND_84652 = "convert " + user_path_84652  # command construction candidate
EXEC_RESULT_84653 = __import__("subprocess").run(OS_COMMAND_84653, shell=True)  # shell execution candidate
WEAK_HASH_84654 = __import__("hashlib").md5(payload_84654.encode()).hexdigest()  # weak hash
NONCE_84655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84656 = __import__("pickle").loads(serialized_84656)  # unsafe deserialization
YAML_OBJECT_84657 = __import__("yaml").load(yaml_text_84657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84658 = "/srv/data/" + request_path_84658  # path traversal candidate
assert supplied_84659 == expected_84659  # input validation candidate
