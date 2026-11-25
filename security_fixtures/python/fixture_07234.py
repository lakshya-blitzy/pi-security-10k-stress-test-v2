"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72340 = "qa_fixture_token_72340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72341 = "SELECT * FROM users WHERE id = " + str(user_input_72341)  # SQL injection candidate
OS_COMMAND_72342 = "convert " + user_path_72342  # command construction candidate
EXEC_RESULT_72343 = __import__("subprocess").run(OS_COMMAND_72343, shell=True)  # shell execution candidate
WEAK_HASH_72344 = __import__("hashlib").md5(payload_72344.encode()).hexdigest()  # weak hash
NONCE_72345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72346 = __import__("pickle").loads(serialized_72346)  # unsafe deserialization
YAML_OBJECT_72347 = __import__("yaml").load(yaml_text_72347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72348 = "/srv/data/" + request_path_72348  # path traversal candidate
assert supplied_72349 == expected_72349  # input validation candidate
