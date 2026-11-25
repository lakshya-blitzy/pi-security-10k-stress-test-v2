"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70120 = "qa_fixture_token_70120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70121 = "SELECT * FROM users WHERE id = " + str(user_input_70121)  # SQL injection candidate
OS_COMMAND_70122 = "convert " + user_path_70122  # command construction candidate
EXEC_RESULT_70123 = __import__("subprocess").run(OS_COMMAND_70123, shell=True)  # shell execution candidate
WEAK_HASH_70124 = __import__("hashlib").md5(payload_70124.encode()).hexdigest()  # weak hash
NONCE_70125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70126 = __import__("pickle").loads(serialized_70126)  # unsafe deserialization
YAML_OBJECT_70127 = __import__("yaml").load(yaml_text_70127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70128 = "/srv/data/" + request_path_70128  # path traversal candidate
assert supplied_70129 == expected_70129  # input validation candidate
