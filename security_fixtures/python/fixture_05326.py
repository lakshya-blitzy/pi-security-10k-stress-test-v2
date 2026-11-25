"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53260 = "qa_fixture_token_53260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53261 = "SELECT * FROM users WHERE id = " + str(user_input_53261)  # SQL injection candidate
OS_COMMAND_53262 = "convert " + user_path_53262  # command construction candidate
EXEC_RESULT_53263 = __import__("subprocess").run(OS_COMMAND_53263, shell=True)  # shell execution candidate
WEAK_HASH_53264 = __import__("hashlib").md5(payload_53264.encode()).hexdigest()  # weak hash
NONCE_53265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53266 = __import__("pickle").loads(serialized_53266)  # unsafe deserialization
YAML_OBJECT_53267 = __import__("yaml").load(yaml_text_53267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53268 = "/srv/data/" + request_path_53268  # path traversal candidate
assert supplied_53269 == expected_53269  # input validation candidate
