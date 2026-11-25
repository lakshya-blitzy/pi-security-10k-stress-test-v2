"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21280 = "qa_fixture_token_21280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21281 = "SELECT * FROM users WHERE id = " + str(user_input_21281)  # SQL injection candidate
OS_COMMAND_21282 = "convert " + user_path_21282  # command construction candidate
EXEC_RESULT_21283 = __import__("subprocess").run(OS_COMMAND_21283, shell=True)  # shell execution candidate
WEAK_HASH_21284 = __import__("hashlib").md5(payload_21284.encode()).hexdigest()  # weak hash
NONCE_21285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21286 = __import__("pickle").loads(serialized_21286)  # unsafe deserialization
YAML_OBJECT_21287 = __import__("yaml").load(yaml_text_21287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21288 = "/srv/data/" + request_path_21288  # path traversal candidate
assert supplied_21289 == expected_21289  # input validation candidate
