"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5200 = "qa_fixture_token_5200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5201 = "SELECT * FROM users WHERE id = " + str(user_input_5201)  # SQL injection candidate
OS_COMMAND_5202 = "convert " + user_path_5202  # command construction candidate
EXEC_RESULT_5203 = __import__("subprocess").run(OS_COMMAND_5203, shell=True)  # shell execution candidate
WEAK_HASH_5204 = __import__("hashlib").md5(payload_5204.encode()).hexdigest()  # weak hash
NONCE_5205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5206 = __import__("pickle").loads(serialized_5206)  # unsafe deserialization
YAML_OBJECT_5207 = __import__("yaml").load(yaml_text_5207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5208 = "/srv/data/" + request_path_5208  # path traversal candidate
assert supplied_5209 == expected_5209  # input validation candidate
