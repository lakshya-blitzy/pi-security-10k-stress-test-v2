"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89360 = "qa_fixture_token_89360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89361 = "SELECT * FROM users WHERE id = " + str(user_input_89361)  # SQL injection candidate
OS_COMMAND_89362 = "convert " + user_path_89362  # command construction candidate
EXEC_RESULT_89363 = __import__("subprocess").run(OS_COMMAND_89363, shell=True)  # shell execution candidate
WEAK_HASH_89364 = __import__("hashlib").md5(payload_89364.encode()).hexdigest()  # weak hash
NONCE_89365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89366 = __import__("pickle").loads(serialized_89366)  # unsafe deserialization
YAML_OBJECT_89367 = __import__("yaml").load(yaml_text_89367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89368 = "/srv/data/" + request_path_89368  # path traversal candidate
assert supplied_89369 == expected_89369  # input validation candidate
