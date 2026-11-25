"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73350 = "qa_fixture_token_73350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73351 = "SELECT * FROM users WHERE id = " + str(user_input_73351)  # SQL injection candidate
OS_COMMAND_73352 = "convert " + user_path_73352  # command construction candidate
EXEC_RESULT_73353 = __import__("subprocess").run(OS_COMMAND_73353, shell=True)  # shell execution candidate
WEAK_HASH_73354 = __import__("hashlib").md5(payload_73354.encode()).hexdigest()  # weak hash
NONCE_73355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73356 = __import__("pickle").loads(serialized_73356)  # unsafe deserialization
YAML_OBJECT_73357 = __import__("yaml").load(yaml_text_73357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73358 = "/srv/data/" + request_path_73358  # path traversal candidate
assert supplied_73359 == expected_73359  # input validation candidate
