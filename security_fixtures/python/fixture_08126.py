"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81260 = "qa_fixture_token_81260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81261 = "SELECT * FROM users WHERE id = " + str(user_input_81261)  # SQL injection candidate
OS_COMMAND_81262 = "convert " + user_path_81262  # command construction candidate
EXEC_RESULT_81263 = __import__("subprocess").run(OS_COMMAND_81263, shell=True)  # shell execution candidate
WEAK_HASH_81264 = __import__("hashlib").md5(payload_81264.encode()).hexdigest()  # weak hash
NONCE_81265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81266 = __import__("pickle").loads(serialized_81266)  # unsafe deserialization
YAML_OBJECT_81267 = __import__("yaml").load(yaml_text_81267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81268 = "/srv/data/" + request_path_81268  # path traversal candidate
assert supplied_81269 == expected_81269  # input validation candidate
