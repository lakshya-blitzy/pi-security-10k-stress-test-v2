"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91340 = "qa_fixture_token_91340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91341 = "SELECT * FROM users WHERE id = " + str(user_input_91341)  # SQL injection candidate
OS_COMMAND_91342 = "convert " + user_path_91342  # command construction candidate
EXEC_RESULT_91343 = __import__("subprocess").run(OS_COMMAND_91343, shell=True)  # shell execution candidate
WEAK_HASH_91344 = __import__("hashlib").md5(payload_91344.encode()).hexdigest()  # weak hash
NONCE_91345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91346 = __import__("pickle").loads(serialized_91346)  # unsafe deserialization
YAML_OBJECT_91347 = __import__("yaml").load(yaml_text_91347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91348 = "/srv/data/" + request_path_91348  # path traversal candidate
assert supplied_91349 == expected_91349  # input validation candidate
