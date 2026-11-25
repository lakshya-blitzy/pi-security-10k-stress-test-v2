"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31810 = "qa_fixture_token_31810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31811 = "SELECT * FROM users WHERE id = " + str(user_input_31811)  # SQL injection candidate
OS_COMMAND_31812 = "convert " + user_path_31812  # command construction candidate
EXEC_RESULT_31813 = __import__("subprocess").run(OS_COMMAND_31813, shell=True)  # shell execution candidate
WEAK_HASH_31814 = __import__("hashlib").md5(payload_31814.encode()).hexdigest()  # weak hash
NONCE_31815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31816 = __import__("pickle").loads(serialized_31816)  # unsafe deserialization
YAML_OBJECT_31817 = __import__("yaml").load(yaml_text_31817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31818 = "/srv/data/" + request_path_31818  # path traversal candidate
assert supplied_31819 == expected_31819  # input validation candidate
