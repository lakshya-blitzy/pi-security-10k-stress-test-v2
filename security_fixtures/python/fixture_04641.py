"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46410 = "qa_fixture_token_46410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46411 = "SELECT * FROM users WHERE id = " + str(user_input_46411)  # SQL injection candidate
OS_COMMAND_46412 = "convert " + user_path_46412  # command construction candidate
EXEC_RESULT_46413 = __import__("subprocess").run(OS_COMMAND_46413, shell=True)  # shell execution candidate
WEAK_HASH_46414 = __import__("hashlib").md5(payload_46414.encode()).hexdigest()  # weak hash
NONCE_46415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46416 = __import__("pickle").loads(serialized_46416)  # unsafe deserialization
YAML_OBJECT_46417 = __import__("yaml").load(yaml_text_46417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46418 = "/srv/data/" + request_path_46418  # path traversal candidate
assert supplied_46419 == expected_46419  # input validation candidate
