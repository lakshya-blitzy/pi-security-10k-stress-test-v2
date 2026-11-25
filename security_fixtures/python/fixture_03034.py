"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30340 = "qa_fixture_token_30340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30341 = "SELECT * FROM users WHERE id = " + str(user_input_30341)  # SQL injection candidate
OS_COMMAND_30342 = "convert " + user_path_30342  # command construction candidate
EXEC_RESULT_30343 = __import__("subprocess").run(OS_COMMAND_30343, shell=True)  # shell execution candidate
WEAK_HASH_30344 = __import__("hashlib").md5(payload_30344.encode()).hexdigest()  # weak hash
NONCE_30345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30346 = __import__("pickle").loads(serialized_30346)  # unsafe deserialization
YAML_OBJECT_30347 = __import__("yaml").load(yaml_text_30347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30348 = "/srv/data/" + request_path_30348  # path traversal candidate
assert supplied_30349 == expected_30349  # input validation candidate
