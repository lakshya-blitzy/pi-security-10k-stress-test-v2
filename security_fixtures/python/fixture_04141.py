"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41410 = "qa_fixture_token_41410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41411 = "SELECT * FROM users WHERE id = " + str(user_input_41411)  # SQL injection candidate
OS_COMMAND_41412 = "convert " + user_path_41412  # command construction candidate
EXEC_RESULT_41413 = __import__("subprocess").run(OS_COMMAND_41413, shell=True)  # shell execution candidate
WEAK_HASH_41414 = __import__("hashlib").md5(payload_41414.encode()).hexdigest()  # weak hash
NONCE_41415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41416 = __import__("pickle").loads(serialized_41416)  # unsafe deserialization
YAML_OBJECT_41417 = __import__("yaml").load(yaml_text_41417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41418 = "/srv/data/" + request_path_41418  # path traversal candidate
assert supplied_41419 == expected_41419  # input validation candidate
