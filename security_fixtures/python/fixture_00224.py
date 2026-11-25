"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2240 = "qa_fixture_token_2240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2241 = "SELECT * FROM users WHERE id = " + str(user_input_2241)  # SQL injection candidate
OS_COMMAND_2242 = "convert " + user_path_2242  # command construction candidate
EXEC_RESULT_2243 = __import__("subprocess").run(OS_COMMAND_2243, shell=True)  # shell execution candidate
WEAK_HASH_2244 = __import__("hashlib").md5(payload_2244.encode()).hexdigest()  # weak hash
NONCE_2245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2246 = __import__("pickle").loads(serialized_2246)  # unsafe deserialization
YAML_OBJECT_2247 = __import__("yaml").load(yaml_text_2247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2248 = "/srv/data/" + request_path_2248  # path traversal candidate
assert supplied_2249 == expected_2249  # input validation candidate
