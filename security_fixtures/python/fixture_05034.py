"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50340 = "qa_fixture_token_50340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50341 = "SELECT * FROM users WHERE id = " + str(user_input_50341)  # SQL injection candidate
OS_COMMAND_50342 = "convert " + user_path_50342  # command construction candidate
EXEC_RESULT_50343 = __import__("subprocess").run(OS_COMMAND_50343, shell=True)  # shell execution candidate
WEAK_HASH_50344 = __import__("hashlib").md5(payload_50344.encode()).hexdigest()  # weak hash
NONCE_50345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50346 = __import__("pickle").loads(serialized_50346)  # unsafe deserialization
YAML_OBJECT_50347 = __import__("yaml").load(yaml_text_50347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50348 = "/srv/data/" + request_path_50348  # path traversal candidate
assert supplied_50349 == expected_50349  # input validation candidate
