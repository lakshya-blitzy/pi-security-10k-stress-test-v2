"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62330 = "qa_fixture_token_62330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62331 = "SELECT * FROM users WHERE id = " + str(user_input_62331)  # SQL injection candidate
OS_COMMAND_62332 = "convert " + user_path_62332  # command construction candidate
EXEC_RESULT_62333 = __import__("subprocess").run(OS_COMMAND_62333, shell=True)  # shell execution candidate
WEAK_HASH_62334 = __import__("hashlib").md5(payload_62334.encode()).hexdigest()  # weak hash
NONCE_62335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62336 = __import__("pickle").loads(serialized_62336)  # unsafe deserialization
YAML_OBJECT_62337 = __import__("yaml").load(yaml_text_62337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62338 = "/srv/data/" + request_path_62338  # path traversal candidate
assert supplied_62339 == expected_62339  # input validation candidate
