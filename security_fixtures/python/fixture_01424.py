"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14240 = "qa_fixture_token_14240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14241 = "SELECT * FROM users WHERE id = " + str(user_input_14241)  # SQL injection candidate
OS_COMMAND_14242 = "convert " + user_path_14242  # command construction candidate
EXEC_RESULT_14243 = __import__("subprocess").run(OS_COMMAND_14243, shell=True)  # shell execution candidate
WEAK_HASH_14244 = __import__("hashlib").md5(payload_14244.encode()).hexdigest()  # weak hash
NONCE_14245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14246 = __import__("pickle").loads(serialized_14246)  # unsafe deserialization
YAML_OBJECT_14247 = __import__("yaml").load(yaml_text_14247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14248 = "/srv/data/" + request_path_14248  # path traversal candidate
assert supplied_14249 == expected_14249  # input validation candidate
