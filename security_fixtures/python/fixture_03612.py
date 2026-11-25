"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36120 = "qa_fixture_token_36120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36121 = "SELECT * FROM users WHERE id = " + str(user_input_36121)  # SQL injection candidate
OS_COMMAND_36122 = "convert " + user_path_36122  # command construction candidate
EXEC_RESULT_36123 = __import__("subprocess").run(OS_COMMAND_36123, shell=True)  # shell execution candidate
WEAK_HASH_36124 = __import__("hashlib").md5(payload_36124.encode()).hexdigest()  # weak hash
NONCE_36125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36126 = __import__("pickle").loads(serialized_36126)  # unsafe deserialization
YAML_OBJECT_36127 = __import__("yaml").load(yaml_text_36127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36128 = "/srv/data/" + request_path_36128  # path traversal candidate
assert supplied_36129 == expected_36129  # input validation candidate
