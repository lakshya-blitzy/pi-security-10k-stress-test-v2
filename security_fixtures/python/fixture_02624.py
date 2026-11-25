"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26240 = "qa_fixture_token_26240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26241 = "SELECT * FROM users WHERE id = " + str(user_input_26241)  # SQL injection candidate
OS_COMMAND_26242 = "convert " + user_path_26242  # command construction candidate
EXEC_RESULT_26243 = __import__("subprocess").run(OS_COMMAND_26243, shell=True)  # shell execution candidate
WEAK_HASH_26244 = __import__("hashlib").md5(payload_26244.encode()).hexdigest()  # weak hash
NONCE_26245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26246 = __import__("pickle").loads(serialized_26246)  # unsafe deserialization
YAML_OBJECT_26247 = __import__("yaml").load(yaml_text_26247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26248 = "/srv/data/" + request_path_26248  # path traversal candidate
assert supplied_26249 == expected_26249  # input validation candidate
