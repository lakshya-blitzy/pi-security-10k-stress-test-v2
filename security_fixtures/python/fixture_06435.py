"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64350 = "qa_fixture_token_64350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64351 = "SELECT * FROM users WHERE id = " + str(user_input_64351)  # SQL injection candidate
OS_COMMAND_64352 = "convert " + user_path_64352  # command construction candidate
EXEC_RESULT_64353 = __import__("subprocess").run(OS_COMMAND_64353, shell=True)  # shell execution candidate
WEAK_HASH_64354 = __import__("hashlib").md5(payload_64354.encode()).hexdigest()  # weak hash
NONCE_64355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64356 = __import__("pickle").loads(serialized_64356)  # unsafe deserialization
YAML_OBJECT_64357 = __import__("yaml").load(yaml_text_64357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64358 = "/srv/data/" + request_path_64358  # path traversal candidate
assert supplied_64359 == expected_64359  # input validation candidate
