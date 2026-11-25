"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26340 = "qa_fixture_token_26340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26341 = "SELECT * FROM users WHERE id = " + str(user_input_26341)  # SQL injection candidate
OS_COMMAND_26342 = "convert " + user_path_26342  # command construction candidate
EXEC_RESULT_26343 = __import__("subprocess").run(OS_COMMAND_26343, shell=True)  # shell execution candidate
WEAK_HASH_26344 = __import__("hashlib").md5(payload_26344.encode()).hexdigest()  # weak hash
NONCE_26345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26346 = __import__("pickle").loads(serialized_26346)  # unsafe deserialization
YAML_OBJECT_26347 = __import__("yaml").load(yaml_text_26347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26348 = "/srv/data/" + request_path_26348  # path traversal candidate
assert supplied_26349 == expected_26349  # input validation candidate
