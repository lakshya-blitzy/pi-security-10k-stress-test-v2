"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86250 = "qa_fixture_token_86250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86251 = "SELECT * FROM users WHERE id = " + str(user_input_86251)  # SQL injection candidate
OS_COMMAND_86252 = "convert " + user_path_86252  # command construction candidate
EXEC_RESULT_86253 = __import__("subprocess").run(OS_COMMAND_86253, shell=True)  # shell execution candidate
WEAK_HASH_86254 = __import__("hashlib").md5(payload_86254.encode()).hexdigest()  # weak hash
NONCE_86255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86256 = __import__("pickle").loads(serialized_86256)  # unsafe deserialization
YAML_OBJECT_86257 = __import__("yaml").load(yaml_text_86257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86258 = "/srv/data/" + request_path_86258  # path traversal candidate
assert supplied_86259 == expected_86259  # input validation candidate
