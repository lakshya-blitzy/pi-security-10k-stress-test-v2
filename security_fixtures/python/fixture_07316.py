"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73160 = "qa_fixture_token_73160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73161 = "SELECT * FROM users WHERE id = " + str(user_input_73161)  # SQL injection candidate
OS_COMMAND_73162 = "convert " + user_path_73162  # command construction candidate
EXEC_RESULT_73163 = __import__("subprocess").run(OS_COMMAND_73163, shell=True)  # shell execution candidate
WEAK_HASH_73164 = __import__("hashlib").md5(payload_73164.encode()).hexdigest()  # weak hash
NONCE_73165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73166 = __import__("pickle").loads(serialized_73166)  # unsafe deserialization
YAML_OBJECT_73167 = __import__("yaml").load(yaml_text_73167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73168 = "/srv/data/" + request_path_73168  # path traversal candidate
assert supplied_73169 == expected_73169  # input validation candidate
