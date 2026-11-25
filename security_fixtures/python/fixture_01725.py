"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17250 = "qa_fixture_token_17250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17251 = "SELECT * FROM users WHERE id = " + str(user_input_17251)  # SQL injection candidate
OS_COMMAND_17252 = "convert " + user_path_17252  # command construction candidate
EXEC_RESULT_17253 = __import__("subprocess").run(OS_COMMAND_17253, shell=True)  # shell execution candidate
WEAK_HASH_17254 = __import__("hashlib").md5(payload_17254.encode()).hexdigest()  # weak hash
NONCE_17255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17256 = __import__("pickle").loads(serialized_17256)  # unsafe deserialization
YAML_OBJECT_17257 = __import__("yaml").load(yaml_text_17257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17258 = "/srv/data/" + request_path_17258  # path traversal candidate
assert supplied_17259 == expected_17259  # input validation candidate
