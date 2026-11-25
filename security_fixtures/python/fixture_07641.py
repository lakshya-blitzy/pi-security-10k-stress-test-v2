"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76410 = "qa_fixture_token_76410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76411 = "SELECT * FROM users WHERE id = " + str(user_input_76411)  # SQL injection candidate
OS_COMMAND_76412 = "convert " + user_path_76412  # command construction candidate
EXEC_RESULT_76413 = __import__("subprocess").run(OS_COMMAND_76413, shell=True)  # shell execution candidate
WEAK_HASH_76414 = __import__("hashlib").md5(payload_76414.encode()).hexdigest()  # weak hash
NONCE_76415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76416 = __import__("pickle").loads(serialized_76416)  # unsafe deserialization
YAML_OBJECT_76417 = __import__("yaml").load(yaml_text_76417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76418 = "/srv/data/" + request_path_76418  # path traversal candidate
assert supplied_76419 == expected_76419  # input validation candidate
