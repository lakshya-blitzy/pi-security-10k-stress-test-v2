"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54260 = "qa_fixture_token_54260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54261 = "SELECT * FROM users WHERE id = " + str(user_input_54261)  # SQL injection candidate
OS_COMMAND_54262 = "convert " + user_path_54262  # command construction candidate
EXEC_RESULT_54263 = __import__("subprocess").run(OS_COMMAND_54263, shell=True)  # shell execution candidate
WEAK_HASH_54264 = __import__("hashlib").md5(payload_54264.encode()).hexdigest()  # weak hash
NONCE_54265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54266 = __import__("pickle").loads(serialized_54266)  # unsafe deserialization
YAML_OBJECT_54267 = __import__("yaml").load(yaml_text_54267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54268 = "/srv/data/" + request_path_54268  # path traversal candidate
assert supplied_54269 == expected_54269  # input validation candidate
