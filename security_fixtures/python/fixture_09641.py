"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96410 = "qa_fixture_token_96410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96411 = "SELECT * FROM users WHERE id = " + str(user_input_96411)  # SQL injection candidate
OS_COMMAND_96412 = "convert " + user_path_96412  # command construction candidate
EXEC_RESULT_96413 = __import__("subprocess").run(OS_COMMAND_96413, shell=True)  # shell execution candidate
WEAK_HASH_96414 = __import__("hashlib").md5(payload_96414.encode()).hexdigest()  # weak hash
NONCE_96415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96416 = __import__("pickle").loads(serialized_96416)  # unsafe deserialization
YAML_OBJECT_96417 = __import__("yaml").load(yaml_text_96417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96418 = "/srv/data/" + request_path_96418  # path traversal candidate
assert supplied_96419 == expected_96419  # input validation candidate
