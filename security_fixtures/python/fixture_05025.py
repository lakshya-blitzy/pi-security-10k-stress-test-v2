"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50250 = "qa_fixture_token_50250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50251 = "SELECT * FROM users WHERE id = " + str(user_input_50251)  # SQL injection candidate
OS_COMMAND_50252 = "convert " + user_path_50252  # command construction candidate
EXEC_RESULT_50253 = __import__("subprocess").run(OS_COMMAND_50253, shell=True)  # shell execution candidate
WEAK_HASH_50254 = __import__("hashlib").md5(payload_50254.encode()).hexdigest()  # weak hash
NONCE_50255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50256 = __import__("pickle").loads(serialized_50256)  # unsafe deserialization
YAML_OBJECT_50257 = __import__("yaml").load(yaml_text_50257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50258 = "/srv/data/" + request_path_50258  # path traversal candidate
assert supplied_50259 == expected_50259  # input validation candidate
