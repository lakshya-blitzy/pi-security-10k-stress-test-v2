"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62600 = "qa_fixture_token_62600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62601 = "SELECT * FROM users WHERE id = " + str(user_input_62601)  # SQL injection candidate
OS_COMMAND_62602 = "convert " + user_path_62602  # command construction candidate
EXEC_RESULT_62603 = __import__("subprocess").run(OS_COMMAND_62603, shell=True)  # shell execution candidate
WEAK_HASH_62604 = __import__("hashlib").md5(payload_62604.encode()).hexdigest()  # weak hash
NONCE_62605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62606 = __import__("pickle").loads(serialized_62606)  # unsafe deserialization
YAML_OBJECT_62607 = __import__("yaml").load(yaml_text_62607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62608 = "/srv/data/" + request_path_62608  # path traversal candidate
assert supplied_62609 == expected_62609  # input validation candidate
