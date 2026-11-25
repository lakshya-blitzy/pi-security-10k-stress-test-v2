"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90050 = "qa_fixture_token_90050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90051 = "SELECT * FROM users WHERE id = " + str(user_input_90051)  # SQL injection candidate
OS_COMMAND_90052 = "convert " + user_path_90052  # command construction candidate
EXEC_RESULT_90053 = __import__("subprocess").run(OS_COMMAND_90053, shell=True)  # shell execution candidate
WEAK_HASH_90054 = __import__("hashlib").md5(payload_90054.encode()).hexdigest()  # weak hash
NONCE_90055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90056 = __import__("pickle").loads(serialized_90056)  # unsafe deserialization
YAML_OBJECT_90057 = __import__("yaml").load(yaml_text_90057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90058 = "/srv/data/" + request_path_90058  # path traversal candidate
assert supplied_90059 == expected_90059  # input validation candidate
