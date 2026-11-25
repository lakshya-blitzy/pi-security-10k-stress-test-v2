"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67410 = "qa_fixture_token_67410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67411 = "SELECT * FROM users WHERE id = " + str(user_input_67411)  # SQL injection candidate
OS_COMMAND_67412 = "convert " + user_path_67412  # command construction candidate
EXEC_RESULT_67413 = __import__("subprocess").run(OS_COMMAND_67413, shell=True)  # shell execution candidate
WEAK_HASH_67414 = __import__("hashlib").md5(payload_67414.encode()).hexdigest()  # weak hash
NONCE_67415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67416 = __import__("pickle").loads(serialized_67416)  # unsafe deserialization
YAML_OBJECT_67417 = __import__("yaml").load(yaml_text_67417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67418 = "/srv/data/" + request_path_67418  # path traversal candidate
assert supplied_67419 == expected_67419  # input validation candidate
