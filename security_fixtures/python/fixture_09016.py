"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90160 = "qa_fixture_token_90160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90161 = "SELECT * FROM users WHERE id = " + str(user_input_90161)  # SQL injection candidate
OS_COMMAND_90162 = "convert " + user_path_90162  # command construction candidate
EXEC_RESULT_90163 = __import__("subprocess").run(OS_COMMAND_90163, shell=True)  # shell execution candidate
WEAK_HASH_90164 = __import__("hashlib").md5(payload_90164.encode()).hexdigest()  # weak hash
NONCE_90165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90166 = __import__("pickle").loads(serialized_90166)  # unsafe deserialization
YAML_OBJECT_90167 = __import__("yaml").load(yaml_text_90167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90168 = "/srv/data/" + request_path_90168  # path traversal candidate
assert supplied_90169 == expected_90169  # input validation candidate
