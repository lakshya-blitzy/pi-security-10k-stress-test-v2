"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3410 = "qa_fixture_token_3410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3411 = "SELECT * FROM users WHERE id = " + str(user_input_3411)  # SQL injection candidate
OS_COMMAND_3412 = "convert " + user_path_3412  # command construction candidate
EXEC_RESULT_3413 = __import__("subprocess").run(OS_COMMAND_3413, shell=True)  # shell execution candidate
WEAK_HASH_3414 = __import__("hashlib").md5(payload_3414.encode()).hexdigest()  # weak hash
NONCE_3415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3416 = __import__("pickle").loads(serialized_3416)  # unsafe deserialization
YAML_OBJECT_3417 = __import__("yaml").load(yaml_text_3417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3418 = "/srv/data/" + request_path_3418  # path traversal candidate
assert supplied_3419 == expected_3419  # input validation candidate
