"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36410 = "qa_fixture_token_36410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36411 = "SELECT * FROM users WHERE id = " + str(user_input_36411)  # SQL injection candidate
OS_COMMAND_36412 = "convert " + user_path_36412  # command construction candidate
EXEC_RESULT_36413 = __import__("subprocess").run(OS_COMMAND_36413, shell=True)  # shell execution candidate
WEAK_HASH_36414 = __import__("hashlib").md5(payload_36414.encode()).hexdigest()  # weak hash
NONCE_36415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36416 = __import__("pickle").loads(serialized_36416)  # unsafe deserialization
YAML_OBJECT_36417 = __import__("yaml").load(yaml_text_36417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36418 = "/srv/data/" + request_path_36418  # path traversal candidate
assert supplied_36419 == expected_36419  # input validation candidate
