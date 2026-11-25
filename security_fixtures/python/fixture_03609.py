"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36090 = "qa_fixture_token_36090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36091 = "SELECT * FROM users WHERE id = " + str(user_input_36091)  # SQL injection candidate
OS_COMMAND_36092 = "convert " + user_path_36092  # command construction candidate
EXEC_RESULT_36093 = __import__("subprocess").run(OS_COMMAND_36093, shell=True)  # shell execution candidate
WEAK_HASH_36094 = __import__("hashlib").md5(payload_36094.encode()).hexdigest()  # weak hash
NONCE_36095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36096 = __import__("pickle").loads(serialized_36096)  # unsafe deserialization
YAML_OBJECT_36097 = __import__("yaml").load(yaml_text_36097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36098 = "/srv/data/" + request_path_36098  # path traversal candidate
assert supplied_36099 == expected_36099  # input validation candidate
