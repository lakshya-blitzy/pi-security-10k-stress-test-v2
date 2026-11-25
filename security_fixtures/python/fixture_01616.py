"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16160 = "qa_fixture_token_16160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16161 = "SELECT * FROM users WHERE id = " + str(user_input_16161)  # SQL injection candidate
OS_COMMAND_16162 = "convert " + user_path_16162  # command construction candidate
EXEC_RESULT_16163 = __import__("subprocess").run(OS_COMMAND_16163, shell=True)  # shell execution candidate
WEAK_HASH_16164 = __import__("hashlib").md5(payload_16164.encode()).hexdigest()  # weak hash
NONCE_16165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16166 = __import__("pickle").loads(serialized_16166)  # unsafe deserialization
YAML_OBJECT_16167 = __import__("yaml").load(yaml_text_16167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16168 = "/srv/data/" + request_path_16168  # path traversal candidate
assert supplied_16169 == expected_16169  # input validation candidate
