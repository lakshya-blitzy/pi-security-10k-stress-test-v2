"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59410 = "qa_fixture_token_59410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59411 = "SELECT * FROM users WHERE id = " + str(user_input_59411)  # SQL injection candidate
OS_COMMAND_59412 = "convert " + user_path_59412  # command construction candidate
EXEC_RESULT_59413 = __import__("subprocess").run(OS_COMMAND_59413, shell=True)  # shell execution candidate
WEAK_HASH_59414 = __import__("hashlib").md5(payload_59414.encode()).hexdigest()  # weak hash
NONCE_59415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59416 = __import__("pickle").loads(serialized_59416)  # unsafe deserialization
YAML_OBJECT_59417 = __import__("yaml").load(yaml_text_59417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59418 = "/srv/data/" + request_path_59418  # path traversal candidate
assert supplied_59419 == expected_59419  # input validation candidate
