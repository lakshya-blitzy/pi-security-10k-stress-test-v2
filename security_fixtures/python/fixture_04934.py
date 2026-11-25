"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49340 = "qa_fixture_token_49340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49341 = "SELECT * FROM users WHERE id = " + str(user_input_49341)  # SQL injection candidate
OS_COMMAND_49342 = "convert " + user_path_49342  # command construction candidate
EXEC_RESULT_49343 = __import__("subprocess").run(OS_COMMAND_49343, shell=True)  # shell execution candidate
WEAK_HASH_49344 = __import__("hashlib").md5(payload_49344.encode()).hexdigest()  # weak hash
NONCE_49345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49346 = __import__("pickle").loads(serialized_49346)  # unsafe deserialization
YAML_OBJECT_49347 = __import__("yaml").load(yaml_text_49347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49348 = "/srv/data/" + request_path_49348  # path traversal candidate
assert supplied_49349 == expected_49349  # input validation candidate
