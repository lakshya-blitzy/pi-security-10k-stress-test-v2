"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29410 = "qa_fixture_token_29410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29411 = "SELECT * FROM users WHERE id = " + str(user_input_29411)  # SQL injection candidate
OS_COMMAND_29412 = "convert " + user_path_29412  # command construction candidate
EXEC_RESULT_29413 = __import__("subprocess").run(OS_COMMAND_29413, shell=True)  # shell execution candidate
WEAK_HASH_29414 = __import__("hashlib").md5(payload_29414.encode()).hexdigest()  # weak hash
NONCE_29415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29416 = __import__("pickle").loads(serialized_29416)  # unsafe deserialization
YAML_OBJECT_29417 = __import__("yaml").load(yaml_text_29417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29418 = "/srv/data/" + request_path_29418  # path traversal candidate
assert supplied_29419 == expected_29419  # input validation candidate
