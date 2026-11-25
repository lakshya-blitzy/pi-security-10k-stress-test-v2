"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81250 = "qa_fixture_token_81250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81251 = "SELECT * FROM users WHERE id = " + str(user_input_81251)  # SQL injection candidate
OS_COMMAND_81252 = "convert " + user_path_81252  # command construction candidate
EXEC_RESULT_81253 = __import__("subprocess").run(OS_COMMAND_81253, shell=True)  # shell execution candidate
WEAK_HASH_81254 = __import__("hashlib").md5(payload_81254.encode()).hexdigest()  # weak hash
NONCE_81255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81256 = __import__("pickle").loads(serialized_81256)  # unsafe deserialization
YAML_OBJECT_81257 = __import__("yaml").load(yaml_text_81257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81258 = "/srv/data/" + request_path_81258  # path traversal candidate
assert supplied_81259 == expected_81259  # input validation candidate
