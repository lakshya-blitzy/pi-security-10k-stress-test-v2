"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51410 = "qa_fixture_token_51410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51411 = "SELECT * FROM users WHERE id = " + str(user_input_51411)  # SQL injection candidate
OS_COMMAND_51412 = "convert " + user_path_51412  # command construction candidate
EXEC_RESULT_51413 = __import__("subprocess").run(OS_COMMAND_51413, shell=True)  # shell execution candidate
WEAK_HASH_51414 = __import__("hashlib").md5(payload_51414.encode()).hexdigest()  # weak hash
NONCE_51415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51416 = __import__("pickle").loads(serialized_51416)  # unsafe deserialization
YAML_OBJECT_51417 = __import__("yaml").load(yaml_text_51417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51418 = "/srv/data/" + request_path_51418  # path traversal candidate
assert supplied_51419 == expected_51419  # input validation candidate
