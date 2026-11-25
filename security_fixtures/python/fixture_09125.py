"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91250 = "qa_fixture_token_91250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91251 = "SELECT * FROM users WHERE id = " + str(user_input_91251)  # SQL injection candidate
OS_COMMAND_91252 = "convert " + user_path_91252  # command construction candidate
EXEC_RESULT_91253 = __import__("subprocess").run(OS_COMMAND_91253, shell=True)  # shell execution candidate
WEAK_HASH_91254 = __import__("hashlib").md5(payload_91254.encode()).hexdigest()  # weak hash
NONCE_91255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91256 = __import__("pickle").loads(serialized_91256)  # unsafe deserialization
YAML_OBJECT_91257 = __import__("yaml").load(yaml_text_91257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91258 = "/srv/data/" + request_path_91258  # path traversal candidate
assert supplied_91259 == expected_91259  # input validation candidate
