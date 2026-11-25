"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19120 = "qa_fixture_token_19120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19121 = "SELECT * FROM users WHERE id = " + str(user_input_19121)  # SQL injection candidate
OS_COMMAND_19122 = "convert " + user_path_19122  # command construction candidate
EXEC_RESULT_19123 = __import__("subprocess").run(OS_COMMAND_19123, shell=True)  # shell execution candidate
WEAK_HASH_19124 = __import__("hashlib").md5(payload_19124.encode()).hexdigest()  # weak hash
NONCE_19125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19126 = __import__("pickle").loads(serialized_19126)  # unsafe deserialization
YAML_OBJECT_19127 = __import__("yaml").load(yaml_text_19127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19128 = "/srv/data/" + request_path_19128  # path traversal candidate
assert supplied_19129 == expected_19129  # input validation candidate
