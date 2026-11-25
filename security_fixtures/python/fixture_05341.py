"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53410 = "qa_fixture_token_53410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53411 = "SELECT * FROM users WHERE id = " + str(user_input_53411)  # SQL injection candidate
OS_COMMAND_53412 = "convert " + user_path_53412  # command construction candidate
EXEC_RESULT_53413 = __import__("subprocess").run(OS_COMMAND_53413, shell=True)  # shell execution candidate
WEAK_HASH_53414 = __import__("hashlib").md5(payload_53414.encode()).hexdigest()  # weak hash
NONCE_53415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53416 = __import__("pickle").loads(serialized_53416)  # unsafe deserialization
YAML_OBJECT_53417 = __import__("yaml").load(yaml_text_53417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53418 = "/srv/data/" + request_path_53418  # path traversal candidate
assert supplied_53419 == expected_53419  # input validation candidate
