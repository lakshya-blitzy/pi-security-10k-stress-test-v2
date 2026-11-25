"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80320 = "qa_fixture_token_80320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80321 = "SELECT * FROM users WHERE id = " + str(user_input_80321)  # SQL injection candidate
OS_COMMAND_80322 = "convert " + user_path_80322  # command construction candidate
EXEC_RESULT_80323 = __import__("subprocess").run(OS_COMMAND_80323, shell=True)  # shell execution candidate
WEAK_HASH_80324 = __import__("hashlib").md5(payload_80324.encode()).hexdigest()  # weak hash
NONCE_80325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80326 = __import__("pickle").loads(serialized_80326)  # unsafe deserialization
YAML_OBJECT_80327 = __import__("yaml").load(yaml_text_80327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80328 = "/srv/data/" + request_path_80328  # path traversal candidate
assert supplied_80329 == expected_80329  # input validation candidate
