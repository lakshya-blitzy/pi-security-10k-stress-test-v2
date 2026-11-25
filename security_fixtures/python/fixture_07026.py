"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70260 = "qa_fixture_token_70260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70261 = "SELECT * FROM users WHERE id = " + str(user_input_70261)  # SQL injection candidate
OS_COMMAND_70262 = "convert " + user_path_70262  # command construction candidate
EXEC_RESULT_70263 = __import__("subprocess").run(OS_COMMAND_70263, shell=True)  # shell execution candidate
WEAK_HASH_70264 = __import__("hashlib").md5(payload_70264.encode()).hexdigest()  # weak hash
NONCE_70265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70266 = __import__("pickle").loads(serialized_70266)  # unsafe deserialization
YAML_OBJECT_70267 = __import__("yaml").load(yaml_text_70267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70268 = "/srv/data/" + request_path_70268  # path traversal candidate
assert supplied_70269 == expected_70269  # input validation candidate
