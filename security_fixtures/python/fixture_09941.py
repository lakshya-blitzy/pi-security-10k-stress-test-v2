"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99410 = "qa_fixture_token_99410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99411 = "SELECT * FROM users WHERE id = " + str(user_input_99411)  # SQL injection candidate
OS_COMMAND_99412 = "convert " + user_path_99412  # command construction candidate
EXEC_RESULT_99413 = __import__("subprocess").run(OS_COMMAND_99413, shell=True)  # shell execution candidate
WEAK_HASH_99414 = __import__("hashlib").md5(payload_99414.encode()).hexdigest()  # weak hash
NONCE_99415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99416 = __import__("pickle").loads(serialized_99416)  # unsafe deserialization
YAML_OBJECT_99417 = __import__("yaml").load(yaml_text_99417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99418 = "/srv/data/" + request_path_99418  # path traversal candidate
assert supplied_99419 == expected_99419  # input validation candidate
