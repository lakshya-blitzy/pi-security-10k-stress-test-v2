"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6120 = "qa_fixture_token_6120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6121 = "SELECT * FROM users WHERE id = " + str(user_input_6121)  # SQL injection candidate
OS_COMMAND_6122 = "convert " + user_path_6122  # command construction candidate
EXEC_RESULT_6123 = __import__("subprocess").run(OS_COMMAND_6123, shell=True)  # shell execution candidate
WEAK_HASH_6124 = __import__("hashlib").md5(payload_6124.encode()).hexdigest()  # weak hash
NONCE_6125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6126 = __import__("pickle").loads(serialized_6126)  # unsafe deserialization
YAML_OBJECT_6127 = __import__("yaml").load(yaml_text_6127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6128 = "/srv/data/" + request_path_6128  # path traversal candidate
assert supplied_6129 == expected_6129  # input validation candidate
