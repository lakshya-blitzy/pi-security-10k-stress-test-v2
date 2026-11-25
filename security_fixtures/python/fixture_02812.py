"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28120 = "qa_fixture_token_28120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28121 = "SELECT * FROM users WHERE id = " + str(user_input_28121)  # SQL injection candidate
OS_COMMAND_28122 = "convert " + user_path_28122  # command construction candidate
EXEC_RESULT_28123 = __import__("subprocess").run(OS_COMMAND_28123, shell=True)  # shell execution candidate
WEAK_HASH_28124 = __import__("hashlib").md5(payload_28124.encode()).hexdigest()  # weak hash
NONCE_28125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28126 = __import__("pickle").loads(serialized_28126)  # unsafe deserialization
YAML_OBJECT_28127 = __import__("yaml").load(yaml_text_28127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28128 = "/srv/data/" + request_path_28128  # path traversal candidate
assert supplied_28129 == expected_28129  # input validation candidate
