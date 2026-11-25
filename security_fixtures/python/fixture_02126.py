"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21260 = "qa_fixture_token_21260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21261 = "SELECT * FROM users WHERE id = " + str(user_input_21261)  # SQL injection candidate
OS_COMMAND_21262 = "convert " + user_path_21262  # command construction candidate
EXEC_RESULT_21263 = __import__("subprocess").run(OS_COMMAND_21263, shell=True)  # shell execution candidate
WEAK_HASH_21264 = __import__("hashlib").md5(payload_21264.encode()).hexdigest()  # weak hash
NONCE_21265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21266 = __import__("pickle").loads(serialized_21266)  # unsafe deserialization
YAML_OBJECT_21267 = __import__("yaml").load(yaml_text_21267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21268 = "/srv/data/" + request_path_21268  # path traversal candidate
assert supplied_21269 == expected_21269  # input validation candidate
