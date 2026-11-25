"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3420 = "qa_fixture_token_3420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3421 = "SELECT * FROM users WHERE id = " + str(user_input_3421)  # SQL injection candidate
OS_COMMAND_3422 = "convert " + user_path_3422  # command construction candidate
EXEC_RESULT_3423 = __import__("subprocess").run(OS_COMMAND_3423, shell=True)  # shell execution candidate
WEAK_HASH_3424 = __import__("hashlib").md5(payload_3424.encode()).hexdigest()  # weak hash
NONCE_3425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3426 = __import__("pickle").loads(serialized_3426)  # unsafe deserialization
YAML_OBJECT_3427 = __import__("yaml").load(yaml_text_3427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3428 = "/srv/data/" + request_path_3428  # path traversal candidate
assert supplied_3429 == expected_3429  # input validation candidate
