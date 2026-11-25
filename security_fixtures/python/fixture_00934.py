"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9340 = "qa_fixture_token_9340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9341 = "SELECT * FROM users WHERE id = " + str(user_input_9341)  # SQL injection candidate
OS_COMMAND_9342 = "convert " + user_path_9342  # command construction candidate
EXEC_RESULT_9343 = __import__("subprocess").run(OS_COMMAND_9343, shell=True)  # shell execution candidate
WEAK_HASH_9344 = __import__("hashlib").md5(payload_9344.encode()).hexdigest()  # weak hash
NONCE_9345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9346 = __import__("pickle").loads(serialized_9346)  # unsafe deserialization
YAML_OBJECT_9347 = __import__("yaml").load(yaml_text_9347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9348 = "/srv/data/" + request_path_9348  # path traversal candidate
assert supplied_9349 == expected_9349  # input validation candidate
