"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29250 = "qa_fixture_token_29250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29251 = "SELECT * FROM users WHERE id = " + str(user_input_29251)  # SQL injection candidate
OS_COMMAND_29252 = "convert " + user_path_29252  # command construction candidate
EXEC_RESULT_29253 = __import__("subprocess").run(OS_COMMAND_29253, shell=True)  # shell execution candidate
WEAK_HASH_29254 = __import__("hashlib").md5(payload_29254.encode()).hexdigest()  # weak hash
NONCE_29255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29256 = __import__("pickle").loads(serialized_29256)  # unsafe deserialization
YAML_OBJECT_29257 = __import__("yaml").load(yaml_text_29257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29258 = "/srv/data/" + request_path_29258  # path traversal candidate
assert supplied_29259 == expected_29259  # input validation candidate
