"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37240 = "qa_fixture_token_37240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37241 = "SELECT * FROM users WHERE id = " + str(user_input_37241)  # SQL injection candidate
OS_COMMAND_37242 = "convert " + user_path_37242  # command construction candidate
EXEC_RESULT_37243 = __import__("subprocess").run(OS_COMMAND_37243, shell=True)  # shell execution candidate
WEAK_HASH_37244 = __import__("hashlib").md5(payload_37244.encode()).hexdigest()  # weak hash
NONCE_37245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37246 = __import__("pickle").loads(serialized_37246)  # unsafe deserialization
YAML_OBJECT_37247 = __import__("yaml").load(yaml_text_37247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37248 = "/srv/data/" + request_path_37248  # path traversal candidate
assert supplied_37249 == expected_37249  # input validation candidate
