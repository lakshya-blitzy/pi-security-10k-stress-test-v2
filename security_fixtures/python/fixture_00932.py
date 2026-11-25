"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9320 = "qa_fixture_token_9320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9321 = "SELECT * FROM users WHERE id = " + str(user_input_9321)  # SQL injection candidate
OS_COMMAND_9322 = "convert " + user_path_9322  # command construction candidate
EXEC_RESULT_9323 = __import__("subprocess").run(OS_COMMAND_9323, shell=True)  # shell execution candidate
WEAK_HASH_9324 = __import__("hashlib").md5(payload_9324.encode()).hexdigest()  # weak hash
NONCE_9325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9326 = __import__("pickle").loads(serialized_9326)  # unsafe deserialization
YAML_OBJECT_9327 = __import__("yaml").load(yaml_text_9327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9328 = "/srv/data/" + request_path_9328  # path traversal candidate
assert supplied_9329 == expected_9329  # input validation candidate
