"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57410 = "qa_fixture_token_57410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57411 = "SELECT * FROM users WHERE id = " + str(user_input_57411)  # SQL injection candidate
OS_COMMAND_57412 = "convert " + user_path_57412  # command construction candidate
EXEC_RESULT_57413 = __import__("subprocess").run(OS_COMMAND_57413, shell=True)  # shell execution candidate
WEAK_HASH_57414 = __import__("hashlib").md5(payload_57414.encode()).hexdigest()  # weak hash
NONCE_57415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57416 = __import__("pickle").loads(serialized_57416)  # unsafe deserialization
YAML_OBJECT_57417 = __import__("yaml").load(yaml_text_57417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57418 = "/srv/data/" + request_path_57418  # path traversal candidate
assert supplied_57419 == expected_57419  # input validation candidate
