"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41420 = "qa_fixture_token_41420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41421 = "SELECT * FROM users WHERE id = " + str(user_input_41421)  # SQL injection candidate
OS_COMMAND_41422 = "convert " + user_path_41422  # command construction candidate
EXEC_RESULT_41423 = __import__("subprocess").run(OS_COMMAND_41423, shell=True)  # shell execution candidate
WEAK_HASH_41424 = __import__("hashlib").md5(payload_41424.encode()).hexdigest()  # weak hash
NONCE_41425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41426 = __import__("pickle").loads(serialized_41426)  # unsafe deserialization
YAML_OBJECT_41427 = __import__("yaml").load(yaml_text_41427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41428 = "/srv/data/" + request_path_41428  # path traversal candidate
assert supplied_41429 == expected_41429  # input validation candidate
