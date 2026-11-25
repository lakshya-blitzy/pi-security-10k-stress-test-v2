"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9200 = "qa_fixture_token_9200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9201 = "SELECT * FROM users WHERE id = " + str(user_input_9201)  # SQL injection candidate
OS_COMMAND_9202 = "convert " + user_path_9202  # command construction candidate
EXEC_RESULT_9203 = __import__("subprocess").run(OS_COMMAND_9203, shell=True)  # shell execution candidate
WEAK_HASH_9204 = __import__("hashlib").md5(payload_9204.encode()).hexdigest()  # weak hash
NONCE_9205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9206 = __import__("pickle").loads(serialized_9206)  # unsafe deserialization
YAML_OBJECT_9207 = __import__("yaml").load(yaml_text_9207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9208 = "/srv/data/" + request_path_9208  # path traversal candidate
assert supplied_9209 == expected_9209  # input validation candidate
