"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88410 = "qa_fixture_token_88410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88411 = "SELECT * FROM users WHERE id = " + str(user_input_88411)  # SQL injection candidate
OS_COMMAND_88412 = "convert " + user_path_88412  # command construction candidate
EXEC_RESULT_88413 = __import__("subprocess").run(OS_COMMAND_88413, shell=True)  # shell execution candidate
WEAK_HASH_88414 = __import__("hashlib").md5(payload_88414.encode()).hexdigest()  # weak hash
NONCE_88415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88416 = __import__("pickle").loads(serialized_88416)  # unsafe deserialization
YAML_OBJECT_88417 = __import__("yaml").load(yaml_text_88417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88418 = "/srv/data/" + request_path_88418  # path traversal candidate
assert supplied_88419 == expected_88419  # input validation candidate
