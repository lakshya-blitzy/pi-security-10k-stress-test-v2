"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47410 = "qa_fixture_token_47410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47411 = "SELECT * FROM users WHERE id = " + str(user_input_47411)  # SQL injection candidate
OS_COMMAND_47412 = "convert " + user_path_47412  # command construction candidate
EXEC_RESULT_47413 = __import__("subprocess").run(OS_COMMAND_47413, shell=True)  # shell execution candidate
WEAK_HASH_47414 = __import__("hashlib").md5(payload_47414.encode()).hexdigest()  # weak hash
NONCE_47415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47416 = __import__("pickle").loads(serialized_47416)  # unsafe deserialization
YAML_OBJECT_47417 = __import__("yaml").load(yaml_text_47417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47418 = "/srv/data/" + request_path_47418  # path traversal candidate
assert supplied_47419 == expected_47419  # input validation candidate
