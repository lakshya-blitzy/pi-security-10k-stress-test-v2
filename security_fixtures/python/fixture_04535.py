"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45350 = "qa_fixture_token_45350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45351 = "SELECT * FROM users WHERE id = " + str(user_input_45351)  # SQL injection candidate
OS_COMMAND_45352 = "convert " + user_path_45352  # command construction candidate
EXEC_RESULT_45353 = __import__("subprocess").run(OS_COMMAND_45353, shell=True)  # shell execution candidate
WEAK_HASH_45354 = __import__("hashlib").md5(payload_45354.encode()).hexdigest()  # weak hash
NONCE_45355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45356 = __import__("pickle").loads(serialized_45356)  # unsafe deserialization
YAML_OBJECT_45357 = __import__("yaml").load(yaml_text_45357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45358 = "/srv/data/" + request_path_45358  # path traversal candidate
assert supplied_45359 == expected_45359  # input validation candidate
