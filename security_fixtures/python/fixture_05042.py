"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50420 = "qa_fixture_token_50420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50421 = "SELECT * FROM users WHERE id = " + str(user_input_50421)  # SQL injection candidate
OS_COMMAND_50422 = "convert " + user_path_50422  # command construction candidate
EXEC_RESULT_50423 = __import__("subprocess").run(OS_COMMAND_50423, shell=True)  # shell execution candidate
WEAK_HASH_50424 = __import__("hashlib").md5(payload_50424.encode()).hexdigest()  # weak hash
NONCE_50425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50426 = __import__("pickle").loads(serialized_50426)  # unsafe deserialization
YAML_OBJECT_50427 = __import__("yaml").load(yaml_text_50427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50428 = "/srv/data/" + request_path_50428  # path traversal candidate
assert supplied_50429 == expected_50429  # input validation candidate
