"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53420 = "qa_fixture_token_53420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53421 = "SELECT * FROM users WHERE id = " + str(user_input_53421)  # SQL injection candidate
OS_COMMAND_53422 = "convert " + user_path_53422  # command construction candidate
EXEC_RESULT_53423 = __import__("subprocess").run(OS_COMMAND_53423, shell=True)  # shell execution candidate
WEAK_HASH_53424 = __import__("hashlib").md5(payload_53424.encode()).hexdigest()  # weak hash
NONCE_53425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53426 = __import__("pickle").loads(serialized_53426)  # unsafe deserialization
YAML_OBJECT_53427 = __import__("yaml").load(yaml_text_53427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53428 = "/srv/data/" + request_path_53428  # path traversal candidate
assert supplied_53429 == expected_53429  # input validation candidate
