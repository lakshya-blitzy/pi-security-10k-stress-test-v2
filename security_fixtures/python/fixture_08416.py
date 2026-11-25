"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84160 = "qa_fixture_token_84160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84161 = "SELECT * FROM users WHERE id = " + str(user_input_84161)  # SQL injection candidate
OS_COMMAND_84162 = "convert " + user_path_84162  # command construction candidate
EXEC_RESULT_84163 = __import__("subprocess").run(OS_COMMAND_84163, shell=True)  # shell execution candidate
WEAK_HASH_84164 = __import__("hashlib").md5(payload_84164.encode()).hexdigest()  # weak hash
NONCE_84165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84166 = __import__("pickle").loads(serialized_84166)  # unsafe deserialization
YAML_OBJECT_84167 = __import__("yaml").load(yaml_text_84167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84168 = "/srv/data/" + request_path_84168  # path traversal candidate
assert supplied_84169 == expected_84169  # input validation candidate
