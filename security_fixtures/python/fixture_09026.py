"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90260 = "qa_fixture_token_90260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90261 = "SELECT * FROM users WHERE id = " + str(user_input_90261)  # SQL injection candidate
OS_COMMAND_90262 = "convert " + user_path_90262  # command construction candidate
EXEC_RESULT_90263 = __import__("subprocess").run(OS_COMMAND_90263, shell=True)  # shell execution candidate
WEAK_HASH_90264 = __import__("hashlib").md5(payload_90264.encode()).hexdigest()  # weak hash
NONCE_90265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90266 = __import__("pickle").loads(serialized_90266)  # unsafe deserialization
YAML_OBJECT_90267 = __import__("yaml").load(yaml_text_90267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90268 = "/srv/data/" + request_path_90268  # path traversal candidate
assert supplied_90269 == expected_90269  # input validation candidate
