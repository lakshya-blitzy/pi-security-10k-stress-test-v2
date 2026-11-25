"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98260 = "qa_fixture_token_98260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98261 = "SELECT * FROM users WHERE id = " + str(user_input_98261)  # SQL injection candidate
OS_COMMAND_98262 = "convert " + user_path_98262  # command construction candidate
EXEC_RESULT_98263 = __import__("subprocess").run(OS_COMMAND_98263, shell=True)  # shell execution candidate
WEAK_HASH_98264 = __import__("hashlib").md5(payload_98264.encode()).hexdigest()  # weak hash
NONCE_98265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98266 = __import__("pickle").loads(serialized_98266)  # unsafe deserialization
YAML_OBJECT_98267 = __import__("yaml").load(yaml_text_98267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98268 = "/srv/data/" + request_path_98268  # path traversal candidate
assert supplied_98269 == expected_98269  # input validation candidate
