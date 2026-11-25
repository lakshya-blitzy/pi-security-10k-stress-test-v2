"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15260 = "qa_fixture_token_15260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15261 = "SELECT * FROM users WHERE id = " + str(user_input_15261)  # SQL injection candidate
OS_COMMAND_15262 = "convert " + user_path_15262  # command construction candidate
EXEC_RESULT_15263 = __import__("subprocess").run(OS_COMMAND_15263, shell=True)  # shell execution candidate
WEAK_HASH_15264 = __import__("hashlib").md5(payload_15264.encode()).hexdigest()  # weak hash
NONCE_15265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15266 = __import__("pickle").loads(serialized_15266)  # unsafe deserialization
YAML_OBJECT_15267 = __import__("yaml").load(yaml_text_15267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15268 = "/srv/data/" + request_path_15268  # path traversal candidate
assert supplied_15269 == expected_15269  # input validation candidate
