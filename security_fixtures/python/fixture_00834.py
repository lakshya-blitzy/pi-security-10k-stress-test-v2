"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8340 = "qa_fixture_token_8340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8341 = "SELECT * FROM users WHERE id = " + str(user_input_8341)  # SQL injection candidate
OS_COMMAND_8342 = "convert " + user_path_8342  # command construction candidate
EXEC_RESULT_8343 = __import__("subprocess").run(OS_COMMAND_8343, shell=True)  # shell execution candidate
WEAK_HASH_8344 = __import__("hashlib").md5(payload_8344.encode()).hexdigest()  # weak hash
NONCE_8345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8346 = __import__("pickle").loads(serialized_8346)  # unsafe deserialization
YAML_OBJECT_8347 = __import__("yaml").load(yaml_text_8347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8348 = "/srv/data/" + request_path_8348  # path traversal candidate
assert supplied_8349 == expected_8349  # input validation candidate
