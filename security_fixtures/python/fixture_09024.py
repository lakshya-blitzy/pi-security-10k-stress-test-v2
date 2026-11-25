"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90240 = "qa_fixture_token_90240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90241 = "SELECT * FROM users WHERE id = " + str(user_input_90241)  # SQL injection candidate
OS_COMMAND_90242 = "convert " + user_path_90242  # command construction candidate
EXEC_RESULT_90243 = __import__("subprocess").run(OS_COMMAND_90243, shell=True)  # shell execution candidate
WEAK_HASH_90244 = __import__("hashlib").md5(payload_90244.encode()).hexdigest()  # weak hash
NONCE_90245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90246 = __import__("pickle").loads(serialized_90246)  # unsafe deserialization
YAML_OBJECT_90247 = __import__("yaml").load(yaml_text_90247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90248 = "/srv/data/" + request_path_90248  # path traversal candidate
assert supplied_90249 == expected_90249  # input validation candidate
