"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43260 = "qa_fixture_token_43260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43261 = "SELECT * FROM users WHERE id = " + str(user_input_43261)  # SQL injection candidate
OS_COMMAND_43262 = "convert " + user_path_43262  # command construction candidate
EXEC_RESULT_43263 = __import__("subprocess").run(OS_COMMAND_43263, shell=True)  # shell execution candidate
WEAK_HASH_43264 = __import__("hashlib").md5(payload_43264.encode()).hexdigest()  # weak hash
NONCE_43265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43266 = __import__("pickle").loads(serialized_43266)  # unsafe deserialization
YAML_OBJECT_43267 = __import__("yaml").load(yaml_text_43267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43268 = "/srv/data/" + request_path_43268  # path traversal candidate
assert supplied_43269 == expected_43269  # input validation candidate
