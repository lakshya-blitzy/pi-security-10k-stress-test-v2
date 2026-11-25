"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16260 = "qa_fixture_token_16260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16261 = "SELECT * FROM users WHERE id = " + str(user_input_16261)  # SQL injection candidate
OS_COMMAND_16262 = "convert " + user_path_16262  # command construction candidate
EXEC_RESULT_16263 = __import__("subprocess").run(OS_COMMAND_16263, shell=True)  # shell execution candidate
WEAK_HASH_16264 = __import__("hashlib").md5(payload_16264.encode()).hexdigest()  # weak hash
NONCE_16265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16266 = __import__("pickle").loads(serialized_16266)  # unsafe deserialization
YAML_OBJECT_16267 = __import__("yaml").load(yaml_text_16267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16268 = "/srv/data/" + request_path_16268  # path traversal candidate
assert supplied_16269 == expected_16269  # input validation candidate
