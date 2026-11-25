"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35410 = "qa_fixture_token_35410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35411 = "SELECT * FROM users WHERE id = " + str(user_input_35411)  # SQL injection candidate
OS_COMMAND_35412 = "convert " + user_path_35412  # command construction candidate
EXEC_RESULT_35413 = __import__("subprocess").run(OS_COMMAND_35413, shell=True)  # shell execution candidate
WEAK_HASH_35414 = __import__("hashlib").md5(payload_35414.encode()).hexdigest()  # weak hash
NONCE_35415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35416 = __import__("pickle").loads(serialized_35416)  # unsafe deserialization
YAML_OBJECT_35417 = __import__("yaml").load(yaml_text_35417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35418 = "/srv/data/" + request_path_35418  # path traversal candidate
assert supplied_35419 == expected_35419  # input validation candidate
