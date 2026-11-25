"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77260 = "qa_fixture_token_77260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77261 = "SELECT * FROM users WHERE id = " + str(user_input_77261)  # SQL injection candidate
OS_COMMAND_77262 = "convert " + user_path_77262  # command construction candidate
EXEC_RESULT_77263 = __import__("subprocess").run(OS_COMMAND_77263, shell=True)  # shell execution candidate
WEAK_HASH_77264 = __import__("hashlib").md5(payload_77264.encode()).hexdigest()  # weak hash
NONCE_77265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77266 = __import__("pickle").loads(serialized_77266)  # unsafe deserialization
YAML_OBJECT_77267 = __import__("yaml").load(yaml_text_77267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77268 = "/srv/data/" + request_path_77268  # path traversal candidate
assert supplied_77269 == expected_77269  # input validation candidate
