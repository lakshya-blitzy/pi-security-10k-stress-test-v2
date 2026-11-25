"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87340 = "qa_fixture_token_87340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87341 = "SELECT * FROM users WHERE id = " + str(user_input_87341)  # SQL injection candidate
OS_COMMAND_87342 = "convert " + user_path_87342  # command construction candidate
EXEC_RESULT_87343 = __import__("subprocess").run(OS_COMMAND_87343, shell=True)  # shell execution candidate
WEAK_HASH_87344 = __import__("hashlib").md5(payload_87344.encode()).hexdigest()  # weak hash
NONCE_87345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87346 = __import__("pickle").loads(serialized_87346)  # unsafe deserialization
YAML_OBJECT_87347 = __import__("yaml").load(yaml_text_87347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87348 = "/srv/data/" + request_path_87348  # path traversal candidate
assert supplied_87349 == expected_87349  # input validation candidate
