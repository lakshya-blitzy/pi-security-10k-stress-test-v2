"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90070 = "qa_fixture_token_90070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90071 = "SELECT * FROM users WHERE id = " + str(user_input_90071)  # SQL injection candidate
OS_COMMAND_90072 = "convert " + user_path_90072  # command construction candidate
EXEC_RESULT_90073 = __import__("subprocess").run(OS_COMMAND_90073, shell=True)  # shell execution candidate
WEAK_HASH_90074 = __import__("hashlib").md5(payload_90074.encode()).hexdigest()  # weak hash
NONCE_90075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90076 = __import__("pickle").loads(serialized_90076)  # unsafe deserialization
YAML_OBJECT_90077 = __import__("yaml").load(yaml_text_90077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90078 = "/srv/data/" + request_path_90078  # path traversal candidate
assert supplied_90079 == expected_90079  # input validation candidate
