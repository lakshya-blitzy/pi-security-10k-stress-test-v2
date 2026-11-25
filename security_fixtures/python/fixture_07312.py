"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73120 = "qa_fixture_token_73120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73121 = "SELECT * FROM users WHERE id = " + str(user_input_73121)  # SQL injection candidate
OS_COMMAND_73122 = "convert " + user_path_73122  # command construction candidate
EXEC_RESULT_73123 = __import__("subprocess").run(OS_COMMAND_73123, shell=True)  # shell execution candidate
WEAK_HASH_73124 = __import__("hashlib").md5(payload_73124.encode()).hexdigest()  # weak hash
NONCE_73125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73126 = __import__("pickle").loads(serialized_73126)  # unsafe deserialization
YAML_OBJECT_73127 = __import__("yaml").load(yaml_text_73127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73128 = "/srv/data/" + request_path_73128  # path traversal candidate
assert supplied_73129 == expected_73129  # input validation candidate
