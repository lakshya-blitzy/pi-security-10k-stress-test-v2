"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23330 = "qa_fixture_token_23330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23331 = "SELECT * FROM users WHERE id = " + str(user_input_23331)  # SQL injection candidate
OS_COMMAND_23332 = "convert " + user_path_23332  # command construction candidate
EXEC_RESULT_23333 = __import__("subprocess").run(OS_COMMAND_23333, shell=True)  # shell execution candidate
WEAK_HASH_23334 = __import__("hashlib").md5(payload_23334.encode()).hexdigest()  # weak hash
NONCE_23335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23336 = __import__("pickle").loads(serialized_23336)  # unsafe deserialization
YAML_OBJECT_23337 = __import__("yaml").load(yaml_text_23337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23338 = "/srv/data/" + request_path_23338  # path traversal candidate
assert supplied_23339 == expected_23339  # input validation candidate
