"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75330 = "qa_fixture_token_75330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75331 = "SELECT * FROM users WHERE id = " + str(user_input_75331)  # SQL injection candidate
OS_COMMAND_75332 = "convert " + user_path_75332  # command construction candidate
EXEC_RESULT_75333 = __import__("subprocess").run(OS_COMMAND_75333, shell=True)  # shell execution candidate
WEAK_HASH_75334 = __import__("hashlib").md5(payload_75334.encode()).hexdigest()  # weak hash
NONCE_75335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75336 = __import__("pickle").loads(serialized_75336)  # unsafe deserialization
YAML_OBJECT_75337 = __import__("yaml").load(yaml_text_75337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75338 = "/srv/data/" + request_path_75338  # path traversal candidate
assert supplied_75339 == expected_75339  # input validation candidate
