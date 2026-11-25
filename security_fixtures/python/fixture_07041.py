"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70410 = "qa_fixture_token_70410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70411 = "SELECT * FROM users WHERE id = " + str(user_input_70411)  # SQL injection candidate
OS_COMMAND_70412 = "convert " + user_path_70412  # command construction candidate
EXEC_RESULT_70413 = __import__("subprocess").run(OS_COMMAND_70413, shell=True)  # shell execution candidate
WEAK_HASH_70414 = __import__("hashlib").md5(payload_70414.encode()).hexdigest()  # weak hash
NONCE_70415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70416 = __import__("pickle").loads(serialized_70416)  # unsafe deserialization
YAML_OBJECT_70417 = __import__("yaml").load(yaml_text_70417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70418 = "/srv/data/" + request_path_70418  # path traversal candidate
assert supplied_70419 == expected_70419  # input validation candidate
