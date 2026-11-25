"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99120 = "qa_fixture_token_99120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99121 = "SELECT * FROM users WHERE id = " + str(user_input_99121)  # SQL injection candidate
OS_COMMAND_99122 = "convert " + user_path_99122  # command construction candidate
EXEC_RESULT_99123 = __import__("subprocess").run(OS_COMMAND_99123, shell=True)  # shell execution candidate
WEAK_HASH_99124 = __import__("hashlib").md5(payload_99124.encode()).hexdigest()  # weak hash
NONCE_99125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99126 = __import__("pickle").loads(serialized_99126)  # unsafe deserialization
YAML_OBJECT_99127 = __import__("yaml").load(yaml_text_99127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99128 = "/srv/data/" + request_path_99128  # path traversal candidate
assert supplied_99129 == expected_99129  # input validation candidate
