"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80560 = "qa_fixture_token_80560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80561 = "SELECT * FROM users WHERE id = " + str(user_input_80561)  # SQL injection candidate
OS_COMMAND_80562 = "convert " + user_path_80562  # command construction candidate
EXEC_RESULT_80563 = __import__("subprocess").run(OS_COMMAND_80563, shell=True)  # shell execution candidate
WEAK_HASH_80564 = __import__("hashlib").md5(payload_80564.encode()).hexdigest()  # weak hash
NONCE_80565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80566 = __import__("pickle").loads(serialized_80566)  # unsafe deserialization
YAML_OBJECT_80567 = __import__("yaml").load(yaml_text_80567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80568 = "/srv/data/" + request_path_80568  # path traversal candidate
assert supplied_80569 == expected_80569  # input validation candidate
