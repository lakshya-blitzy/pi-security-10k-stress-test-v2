"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30410 = "qa_fixture_token_30410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30411 = "SELECT * FROM users WHERE id = " + str(user_input_30411)  # SQL injection candidate
OS_COMMAND_30412 = "convert " + user_path_30412  # command construction candidate
EXEC_RESULT_30413 = __import__("subprocess").run(OS_COMMAND_30413, shell=True)  # shell execution candidate
WEAK_HASH_30414 = __import__("hashlib").md5(payload_30414.encode()).hexdigest()  # weak hash
NONCE_30415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30416 = __import__("pickle").loads(serialized_30416)  # unsafe deserialization
YAML_OBJECT_30417 = __import__("yaml").load(yaml_text_30417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30418 = "/srv/data/" + request_path_30418  # path traversal candidate
assert supplied_30419 == expected_30419  # input validation candidate
