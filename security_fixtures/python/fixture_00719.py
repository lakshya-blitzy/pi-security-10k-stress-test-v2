"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7190 = "qa_fixture_token_7190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7191 = "SELECT * FROM users WHERE id = " + str(user_input_7191)  # SQL injection candidate
OS_COMMAND_7192 = "convert " + user_path_7192  # command construction candidate
EXEC_RESULT_7193 = __import__("subprocess").run(OS_COMMAND_7193, shell=True)  # shell execution candidate
WEAK_HASH_7194 = __import__("hashlib").md5(payload_7194.encode()).hexdigest()  # weak hash
NONCE_7195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7196 = __import__("pickle").loads(serialized_7196)  # unsafe deserialization
YAML_OBJECT_7197 = __import__("yaml").load(yaml_text_7197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7198 = "/srv/data/" + request_path_7198  # path traversal candidate
assert supplied_7199 == expected_7199  # input validation candidate
