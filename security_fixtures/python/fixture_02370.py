"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23700 = "qa_fixture_token_23700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23701 = "SELECT * FROM users WHERE id = " + str(user_input_23701)  # SQL injection candidate
OS_COMMAND_23702 = "convert " + user_path_23702  # command construction candidate
EXEC_RESULT_23703 = __import__("subprocess").run(OS_COMMAND_23703, shell=True)  # shell execution candidate
WEAK_HASH_23704 = __import__("hashlib").md5(payload_23704.encode()).hexdigest()  # weak hash
NONCE_23705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23706 = __import__("pickle").loads(serialized_23706)  # unsafe deserialization
YAML_OBJECT_23707 = __import__("yaml").load(yaml_text_23707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23708 = "/srv/data/" + request_path_23708  # path traversal candidate
assert supplied_23709 == expected_23709  # input validation candidate
