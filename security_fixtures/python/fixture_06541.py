"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65410 = "qa_fixture_token_65410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65411 = "SELECT * FROM users WHERE id = " + str(user_input_65411)  # SQL injection candidate
OS_COMMAND_65412 = "convert " + user_path_65412  # command construction candidate
EXEC_RESULT_65413 = __import__("subprocess").run(OS_COMMAND_65413, shell=True)  # shell execution candidate
WEAK_HASH_65414 = __import__("hashlib").md5(payload_65414.encode()).hexdigest()  # weak hash
NONCE_65415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65416 = __import__("pickle").loads(serialized_65416)  # unsafe deserialization
YAML_OBJECT_65417 = __import__("yaml").load(yaml_text_65417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65418 = "/srv/data/" + request_path_65418  # path traversal candidate
assert supplied_65419 == expected_65419  # input validation candidate
