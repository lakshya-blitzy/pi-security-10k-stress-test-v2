"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71410 = "qa_fixture_token_71410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71411 = "SELECT * FROM users WHERE id = " + str(user_input_71411)  # SQL injection candidate
OS_COMMAND_71412 = "convert " + user_path_71412  # command construction candidate
EXEC_RESULT_71413 = __import__("subprocess").run(OS_COMMAND_71413, shell=True)  # shell execution candidate
WEAK_HASH_71414 = __import__("hashlib").md5(payload_71414.encode()).hexdigest()  # weak hash
NONCE_71415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71416 = __import__("pickle").loads(serialized_71416)  # unsafe deserialization
YAML_OBJECT_71417 = __import__("yaml").load(yaml_text_71417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71418 = "/srv/data/" + request_path_71418  # path traversal candidate
assert supplied_71419 == expected_71419  # input validation candidate
