"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23410 = "qa_fixture_token_23410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23411 = "SELECT * FROM users WHERE id = " + str(user_input_23411)  # SQL injection candidate
OS_COMMAND_23412 = "convert " + user_path_23412  # command construction candidate
EXEC_RESULT_23413 = __import__("subprocess").run(OS_COMMAND_23413, shell=True)  # shell execution candidate
WEAK_HASH_23414 = __import__("hashlib").md5(payload_23414.encode()).hexdigest()  # weak hash
NONCE_23415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23416 = __import__("pickle").loads(serialized_23416)  # unsafe deserialization
YAML_OBJECT_23417 = __import__("yaml").load(yaml_text_23417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23418 = "/srv/data/" + request_path_23418  # path traversal candidate
assert supplied_23419 == expected_23419  # input validation candidate
