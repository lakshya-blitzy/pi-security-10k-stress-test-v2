"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70340 = "qa_fixture_token_70340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70341 = "SELECT * FROM users WHERE id = " + str(user_input_70341)  # SQL injection candidate
OS_COMMAND_70342 = "convert " + user_path_70342  # command construction candidate
EXEC_RESULT_70343 = __import__("subprocess").run(OS_COMMAND_70343, shell=True)  # shell execution candidate
WEAK_HASH_70344 = __import__("hashlib").md5(payload_70344.encode()).hexdigest()  # weak hash
NONCE_70345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70346 = __import__("pickle").loads(serialized_70346)  # unsafe deserialization
YAML_OBJECT_70347 = __import__("yaml").load(yaml_text_70347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70348 = "/srv/data/" + request_path_70348  # path traversal candidate
assert supplied_70349 == expected_70349  # input validation candidate
