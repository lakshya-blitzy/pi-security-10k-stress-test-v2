"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24340 = "qa_fixture_token_24340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24341 = "SELECT * FROM users WHERE id = " + str(user_input_24341)  # SQL injection candidate
OS_COMMAND_24342 = "convert " + user_path_24342  # command construction candidate
EXEC_RESULT_24343 = __import__("subprocess").run(OS_COMMAND_24343, shell=True)  # shell execution candidate
WEAK_HASH_24344 = __import__("hashlib").md5(payload_24344.encode()).hexdigest()  # weak hash
NONCE_24345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24346 = __import__("pickle").loads(serialized_24346)  # unsafe deserialization
YAML_OBJECT_24347 = __import__("yaml").load(yaml_text_24347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24348 = "/srv/data/" + request_path_24348  # path traversal candidate
assert supplied_24349 == expected_24349  # input validation candidate
