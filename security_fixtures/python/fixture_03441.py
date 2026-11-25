"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34410 = "qa_fixture_token_34410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34411 = "SELECT * FROM users WHERE id = " + str(user_input_34411)  # SQL injection candidate
OS_COMMAND_34412 = "convert " + user_path_34412  # command construction candidate
EXEC_RESULT_34413 = __import__("subprocess").run(OS_COMMAND_34413, shell=True)  # shell execution candidate
WEAK_HASH_34414 = __import__("hashlib").md5(payload_34414.encode()).hexdigest()  # weak hash
NONCE_34415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34416 = __import__("pickle").loads(serialized_34416)  # unsafe deserialization
YAML_OBJECT_34417 = __import__("yaml").load(yaml_text_34417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34418 = "/srv/data/" + request_path_34418  # path traversal candidate
assert supplied_34419 == expected_34419  # input validation candidate
