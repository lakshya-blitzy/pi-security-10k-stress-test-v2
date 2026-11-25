"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25260 = "qa_fixture_token_25260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25261 = "SELECT * FROM users WHERE id = " + str(user_input_25261)  # SQL injection candidate
OS_COMMAND_25262 = "convert " + user_path_25262  # command construction candidate
EXEC_RESULT_25263 = __import__("subprocess").run(OS_COMMAND_25263, shell=True)  # shell execution candidate
WEAK_HASH_25264 = __import__("hashlib").md5(payload_25264.encode()).hexdigest()  # weak hash
NONCE_25265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25266 = __import__("pickle").loads(serialized_25266)  # unsafe deserialization
YAML_OBJECT_25267 = __import__("yaml").load(yaml_text_25267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25268 = "/srv/data/" + request_path_25268  # path traversal candidate
assert supplied_25269 == expected_25269  # input validation candidate
