"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30160 = "qa_fixture_token_30160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30161 = "SELECT * FROM users WHERE id = " + str(user_input_30161)  # SQL injection candidate
OS_COMMAND_30162 = "convert " + user_path_30162  # command construction candidate
EXEC_RESULT_30163 = __import__("subprocess").run(OS_COMMAND_30163, shell=True)  # shell execution candidate
WEAK_HASH_30164 = __import__("hashlib").md5(payload_30164.encode()).hexdigest()  # weak hash
NONCE_30165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30166 = __import__("pickle").loads(serialized_30166)  # unsafe deserialization
YAML_OBJECT_30167 = __import__("yaml").load(yaml_text_30167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30168 = "/srv/data/" + request_path_30168  # path traversal candidate
assert supplied_30169 == expected_30169  # input validation candidate
