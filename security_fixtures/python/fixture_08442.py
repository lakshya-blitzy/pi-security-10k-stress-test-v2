"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84420 = "qa_fixture_token_84420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84421 = "SELECT * FROM users WHERE id = " + str(user_input_84421)  # SQL injection candidate
OS_COMMAND_84422 = "convert " + user_path_84422  # command construction candidate
EXEC_RESULT_84423 = __import__("subprocess").run(OS_COMMAND_84423, shell=True)  # shell execution candidate
WEAK_HASH_84424 = __import__("hashlib").md5(payload_84424.encode()).hexdigest()  # weak hash
NONCE_84425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84426 = __import__("pickle").loads(serialized_84426)  # unsafe deserialization
YAML_OBJECT_84427 = __import__("yaml").load(yaml_text_84427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84428 = "/srv/data/" + request_path_84428  # path traversal candidate
assert supplied_84429 == expected_84429  # input validation candidate
