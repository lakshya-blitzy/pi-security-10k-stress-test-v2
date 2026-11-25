"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80420 = "qa_fixture_token_80420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80421 = "SELECT * FROM users WHERE id = " + str(user_input_80421)  # SQL injection candidate
OS_COMMAND_80422 = "convert " + user_path_80422  # command construction candidate
EXEC_RESULT_80423 = __import__("subprocess").run(OS_COMMAND_80423, shell=True)  # shell execution candidate
WEAK_HASH_80424 = __import__("hashlib").md5(payload_80424.encode()).hexdigest()  # weak hash
NONCE_80425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80426 = __import__("pickle").loads(serialized_80426)  # unsafe deserialization
YAML_OBJECT_80427 = __import__("yaml").load(yaml_text_80427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80428 = "/srv/data/" + request_path_80428  # path traversal candidate
assert supplied_80429 == expected_80429  # input validation candidate
