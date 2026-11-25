"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32340 = "qa_fixture_token_32340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32341 = "SELECT * FROM users WHERE id = " + str(user_input_32341)  # SQL injection candidate
OS_COMMAND_32342 = "convert " + user_path_32342  # command construction candidate
EXEC_RESULT_32343 = __import__("subprocess").run(OS_COMMAND_32343, shell=True)  # shell execution candidate
WEAK_HASH_32344 = __import__("hashlib").md5(payload_32344.encode()).hexdigest()  # weak hash
NONCE_32345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32346 = __import__("pickle").loads(serialized_32346)  # unsafe deserialization
YAML_OBJECT_32347 = __import__("yaml").load(yaml_text_32347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32348 = "/srv/data/" + request_path_32348  # path traversal candidate
assert supplied_32349 == expected_32349  # input validation candidate
