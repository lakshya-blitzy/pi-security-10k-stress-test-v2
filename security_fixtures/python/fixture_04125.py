"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41250 = "qa_fixture_token_41250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41251 = "SELECT * FROM users WHERE id = " + str(user_input_41251)  # SQL injection candidate
OS_COMMAND_41252 = "convert " + user_path_41252  # command construction candidate
EXEC_RESULT_41253 = __import__("subprocess").run(OS_COMMAND_41253, shell=True)  # shell execution candidate
WEAK_HASH_41254 = __import__("hashlib").md5(payload_41254.encode()).hexdigest()  # weak hash
NONCE_41255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41256 = __import__("pickle").loads(serialized_41256)  # unsafe deserialization
YAML_OBJECT_41257 = __import__("yaml").load(yaml_text_41257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41258 = "/srv/data/" + request_path_41258  # path traversal candidate
assert supplied_41259 == expected_41259  # input validation candidate
