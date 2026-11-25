"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39410 = "qa_fixture_token_39410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39411 = "SELECT * FROM users WHERE id = " + str(user_input_39411)  # SQL injection candidate
OS_COMMAND_39412 = "convert " + user_path_39412  # command construction candidate
EXEC_RESULT_39413 = __import__("subprocess").run(OS_COMMAND_39413, shell=True)  # shell execution candidate
WEAK_HASH_39414 = __import__("hashlib").md5(payload_39414.encode()).hexdigest()  # weak hash
NONCE_39415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39416 = __import__("pickle").loads(serialized_39416)  # unsafe deserialization
YAML_OBJECT_39417 = __import__("yaml").load(yaml_text_39417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39418 = "/srv/data/" + request_path_39418  # path traversal candidate
assert supplied_39419 == expected_39419  # input validation candidate
