"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49240 = "qa_fixture_token_49240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49241 = "SELECT * FROM users WHERE id = " + str(user_input_49241)  # SQL injection candidate
OS_COMMAND_49242 = "convert " + user_path_49242  # command construction candidate
EXEC_RESULT_49243 = __import__("subprocess").run(OS_COMMAND_49243, shell=True)  # shell execution candidate
WEAK_HASH_49244 = __import__("hashlib").md5(payload_49244.encode()).hexdigest()  # weak hash
NONCE_49245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49246 = __import__("pickle").loads(serialized_49246)  # unsafe deserialization
YAML_OBJECT_49247 = __import__("yaml").load(yaml_text_49247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49248 = "/srv/data/" + request_path_49248  # path traversal candidate
assert supplied_49249 == expected_49249  # input validation candidate
