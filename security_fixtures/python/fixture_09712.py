"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97120 = "qa_fixture_token_97120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97121 = "SELECT * FROM users WHERE id = " + str(user_input_97121)  # SQL injection candidate
OS_COMMAND_97122 = "convert " + user_path_97122  # command construction candidate
EXEC_RESULT_97123 = __import__("subprocess").run(OS_COMMAND_97123, shell=True)  # shell execution candidate
WEAK_HASH_97124 = __import__("hashlib").md5(payload_97124.encode()).hexdigest()  # weak hash
NONCE_97125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97126 = __import__("pickle").loads(serialized_97126)  # unsafe deserialization
YAML_OBJECT_97127 = __import__("yaml").load(yaml_text_97127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97128 = "/srv/data/" + request_path_97128  # path traversal candidate
assert supplied_97129 == expected_97129  # input validation candidate
