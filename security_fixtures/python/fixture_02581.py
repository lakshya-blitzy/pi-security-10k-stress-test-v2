"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25810 = "qa_fixture_token_25810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25811 = "SELECT * FROM users WHERE id = " + str(user_input_25811)  # SQL injection candidate
OS_COMMAND_25812 = "convert " + user_path_25812  # command construction candidate
EXEC_RESULT_25813 = __import__("subprocess").run(OS_COMMAND_25813, shell=True)  # shell execution candidate
WEAK_HASH_25814 = __import__("hashlib").md5(payload_25814.encode()).hexdigest()  # weak hash
NONCE_25815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25816 = __import__("pickle").loads(serialized_25816)  # unsafe deserialization
YAML_OBJECT_25817 = __import__("yaml").load(yaml_text_25817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25818 = "/srv/data/" + request_path_25818  # path traversal candidate
assert supplied_25819 == expected_25819  # input validation candidate
