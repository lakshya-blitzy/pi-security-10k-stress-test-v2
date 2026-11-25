"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80340 = "qa_fixture_token_80340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80341 = "SELECT * FROM users WHERE id = " + str(user_input_80341)  # SQL injection candidate
OS_COMMAND_80342 = "convert " + user_path_80342  # command construction candidate
EXEC_RESULT_80343 = __import__("subprocess").run(OS_COMMAND_80343, shell=True)  # shell execution candidate
WEAK_HASH_80344 = __import__("hashlib").md5(payload_80344.encode()).hexdigest()  # weak hash
NONCE_80345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80346 = __import__("pickle").loads(serialized_80346)  # unsafe deserialization
YAML_OBJECT_80347 = __import__("yaml").load(yaml_text_80347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80348 = "/srv/data/" + request_path_80348  # path traversal candidate
assert supplied_80349 == expected_80349  # input validation candidate
