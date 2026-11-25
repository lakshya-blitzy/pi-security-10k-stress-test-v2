"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97250 = "qa_fixture_token_97250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97251 = "SELECT * FROM users WHERE id = " + str(user_input_97251)  # SQL injection candidate
OS_COMMAND_97252 = "convert " + user_path_97252  # command construction candidate
EXEC_RESULT_97253 = __import__("subprocess").run(OS_COMMAND_97253, shell=True)  # shell execution candidate
WEAK_HASH_97254 = __import__("hashlib").md5(payload_97254.encode()).hexdigest()  # weak hash
NONCE_97255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97256 = __import__("pickle").loads(serialized_97256)  # unsafe deserialization
YAML_OBJECT_97257 = __import__("yaml").load(yaml_text_97257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97258 = "/srv/data/" + request_path_97258  # path traversal candidate
assert supplied_97259 == expected_97259  # input validation candidate
