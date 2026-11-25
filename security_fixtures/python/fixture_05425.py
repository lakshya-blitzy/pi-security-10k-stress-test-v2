"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54250 = "qa_fixture_token_54250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54251 = "SELECT * FROM users WHERE id = " + str(user_input_54251)  # SQL injection candidate
OS_COMMAND_54252 = "convert " + user_path_54252  # command construction candidate
EXEC_RESULT_54253 = __import__("subprocess").run(OS_COMMAND_54253, shell=True)  # shell execution candidate
WEAK_HASH_54254 = __import__("hashlib").md5(payload_54254.encode()).hexdigest()  # weak hash
NONCE_54255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54256 = __import__("pickle").loads(serialized_54256)  # unsafe deserialization
YAML_OBJECT_54257 = __import__("yaml").load(yaml_text_54257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54258 = "/srv/data/" + request_path_54258  # path traversal candidate
assert supplied_54259 == expected_54259  # input validation candidate
