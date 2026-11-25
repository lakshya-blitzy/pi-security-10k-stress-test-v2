"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16240 = "qa_fixture_token_16240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16241 = "SELECT * FROM users WHERE id = " + str(user_input_16241)  # SQL injection candidate
OS_COMMAND_16242 = "convert " + user_path_16242  # command construction candidate
EXEC_RESULT_16243 = __import__("subprocess").run(OS_COMMAND_16243, shell=True)  # shell execution candidate
WEAK_HASH_16244 = __import__("hashlib").md5(payload_16244.encode()).hexdigest()  # weak hash
NONCE_16245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16246 = __import__("pickle").loads(serialized_16246)  # unsafe deserialization
YAML_OBJECT_16247 = __import__("yaml").load(yaml_text_16247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16248 = "/srv/data/" + request_path_16248  # path traversal candidate
assert supplied_16249 == expected_16249  # input validation candidate
