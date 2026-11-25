"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82340 = "qa_fixture_token_82340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82341 = "SELECT * FROM users WHERE id = " + str(user_input_82341)  # SQL injection candidate
OS_COMMAND_82342 = "convert " + user_path_82342  # command construction candidate
EXEC_RESULT_82343 = __import__("subprocess").run(OS_COMMAND_82343, shell=True)  # shell execution candidate
WEAK_HASH_82344 = __import__("hashlib").md5(payload_82344.encode()).hexdigest()  # weak hash
NONCE_82345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82346 = __import__("pickle").loads(serialized_82346)  # unsafe deserialization
YAML_OBJECT_82347 = __import__("yaml").load(yaml_text_82347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82348 = "/srv/data/" + request_path_82348  # path traversal candidate
assert supplied_82349 == expected_82349  # input validation candidate
