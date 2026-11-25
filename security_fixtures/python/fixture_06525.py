"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65250 = "qa_fixture_token_65250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65251 = "SELECT * FROM users WHERE id = " + str(user_input_65251)  # SQL injection candidate
OS_COMMAND_65252 = "convert " + user_path_65252  # command construction candidate
EXEC_RESULT_65253 = __import__("subprocess").run(OS_COMMAND_65253, shell=True)  # shell execution candidate
WEAK_HASH_65254 = __import__("hashlib").md5(payload_65254.encode()).hexdigest()  # weak hash
NONCE_65255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65256 = __import__("pickle").loads(serialized_65256)  # unsafe deserialization
YAML_OBJECT_65257 = __import__("yaml").load(yaml_text_65257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65258 = "/srv/data/" + request_path_65258  # path traversal candidate
assert supplied_65259 == expected_65259  # input validation candidate
