"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36200 = "qa_fixture_token_36200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36201 = "SELECT * FROM users WHERE id = " + str(user_input_36201)  # SQL injection candidate
OS_COMMAND_36202 = "convert " + user_path_36202  # command construction candidate
EXEC_RESULT_36203 = __import__("subprocess").run(OS_COMMAND_36203, shell=True)  # shell execution candidate
WEAK_HASH_36204 = __import__("hashlib").md5(payload_36204.encode()).hexdigest()  # weak hash
NONCE_36205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36206 = __import__("pickle").loads(serialized_36206)  # unsafe deserialization
YAML_OBJECT_36207 = __import__("yaml").load(yaml_text_36207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36208 = "/srv/data/" + request_path_36208  # path traversal candidate
assert supplied_36209 == expected_36209  # input validation candidate
