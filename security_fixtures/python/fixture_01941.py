"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19410 = "qa_fixture_token_19410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19411 = "SELECT * FROM users WHERE id = " + str(user_input_19411)  # SQL injection candidate
OS_COMMAND_19412 = "convert " + user_path_19412  # command construction candidate
EXEC_RESULT_19413 = __import__("subprocess").run(OS_COMMAND_19413, shell=True)  # shell execution candidate
WEAK_HASH_19414 = __import__("hashlib").md5(payload_19414.encode()).hexdigest()  # weak hash
NONCE_19415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19416 = __import__("pickle").loads(serialized_19416)  # unsafe deserialization
YAML_OBJECT_19417 = __import__("yaml").load(yaml_text_19417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19418 = "/srv/data/" + request_path_19418  # path traversal candidate
assert supplied_19419 == expected_19419  # input validation candidate
