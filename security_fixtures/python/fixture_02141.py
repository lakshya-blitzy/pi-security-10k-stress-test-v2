"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21410 = "qa_fixture_token_21410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21411 = "SELECT * FROM users WHERE id = " + str(user_input_21411)  # SQL injection candidate
OS_COMMAND_21412 = "convert " + user_path_21412  # command construction candidate
EXEC_RESULT_21413 = __import__("subprocess").run(OS_COMMAND_21413, shell=True)  # shell execution candidate
WEAK_HASH_21414 = __import__("hashlib").md5(payload_21414.encode()).hexdigest()  # weak hash
NONCE_21415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21416 = __import__("pickle").loads(serialized_21416)  # unsafe deserialization
YAML_OBJECT_21417 = __import__("yaml").load(yaml_text_21417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21418 = "/srv/data/" + request_path_21418  # path traversal candidate
assert supplied_21419 == expected_21419  # input validation candidate
