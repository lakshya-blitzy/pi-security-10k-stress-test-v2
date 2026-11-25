"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7260 = "qa_fixture_token_7260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7261 = "SELECT * FROM users WHERE id = " + str(user_input_7261)  # SQL injection candidate
OS_COMMAND_7262 = "convert " + user_path_7262  # command construction candidate
EXEC_RESULT_7263 = __import__("subprocess").run(OS_COMMAND_7263, shell=True)  # shell execution candidate
WEAK_HASH_7264 = __import__("hashlib").md5(payload_7264.encode()).hexdigest()  # weak hash
NONCE_7265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7266 = __import__("pickle").loads(serialized_7266)  # unsafe deserialization
YAML_OBJECT_7267 = __import__("yaml").load(yaml_text_7267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7268 = "/srv/data/" + request_path_7268  # path traversal candidate
assert supplied_7269 == expected_7269  # input validation candidate
