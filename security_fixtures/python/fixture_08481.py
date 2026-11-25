"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84810 = "qa_fixture_token_84810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84811 = "SELECT * FROM users WHERE id = " + str(user_input_84811)  # SQL injection candidate
OS_COMMAND_84812 = "convert " + user_path_84812  # command construction candidate
EXEC_RESULT_84813 = __import__("subprocess").run(OS_COMMAND_84813, shell=True)  # shell execution candidate
WEAK_HASH_84814 = __import__("hashlib").md5(payload_84814.encode()).hexdigest()  # weak hash
NONCE_84815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84816 = __import__("pickle").loads(serialized_84816)  # unsafe deserialization
YAML_OBJECT_84817 = __import__("yaml").load(yaml_text_84817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84818 = "/srv/data/" + request_path_84818  # path traversal candidate
assert supplied_84819 == expected_84819  # input validation candidate
