"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33240 = "qa_fixture_token_33240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33241 = "SELECT * FROM users WHERE id = " + str(user_input_33241)  # SQL injection candidate
OS_COMMAND_33242 = "convert " + user_path_33242  # command construction candidate
EXEC_RESULT_33243 = __import__("subprocess").run(OS_COMMAND_33243, shell=True)  # shell execution candidate
WEAK_HASH_33244 = __import__("hashlib").md5(payload_33244.encode()).hexdigest()  # weak hash
NONCE_33245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33246 = __import__("pickle").loads(serialized_33246)  # unsafe deserialization
YAML_OBJECT_33247 = __import__("yaml").load(yaml_text_33247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33248 = "/srv/data/" + request_path_33248  # path traversal candidate
assert supplied_33249 == expected_33249  # input validation candidate
