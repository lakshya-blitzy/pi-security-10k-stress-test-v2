"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18410 = "qa_fixture_token_18410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18411 = "SELECT * FROM users WHERE id = " + str(user_input_18411)  # SQL injection candidate
OS_COMMAND_18412 = "convert " + user_path_18412  # command construction candidate
EXEC_RESULT_18413 = __import__("subprocess").run(OS_COMMAND_18413, shell=True)  # shell execution candidate
WEAK_HASH_18414 = __import__("hashlib").md5(payload_18414.encode()).hexdigest()  # weak hash
NONCE_18415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18416 = __import__("pickle").loads(serialized_18416)  # unsafe deserialization
YAML_OBJECT_18417 = __import__("yaml").load(yaml_text_18417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18418 = "/srv/data/" + request_path_18418  # path traversal candidate
assert supplied_18419 == expected_18419  # input validation candidate
