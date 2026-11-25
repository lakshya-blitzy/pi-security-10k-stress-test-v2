"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52340 = "qa_fixture_token_52340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52341 = "SELECT * FROM users WHERE id = " + str(user_input_52341)  # SQL injection candidate
OS_COMMAND_52342 = "convert " + user_path_52342  # command construction candidate
EXEC_RESULT_52343 = __import__("subprocess").run(OS_COMMAND_52343, shell=True)  # shell execution candidate
WEAK_HASH_52344 = __import__("hashlib").md5(payload_52344.encode()).hexdigest()  # weak hash
NONCE_52345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52346 = __import__("pickle").loads(serialized_52346)  # unsafe deserialization
YAML_OBJECT_52347 = __import__("yaml").load(yaml_text_52347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52348 = "/srv/data/" + request_path_52348  # path traversal candidate
assert supplied_52349 == expected_52349  # input validation candidate
