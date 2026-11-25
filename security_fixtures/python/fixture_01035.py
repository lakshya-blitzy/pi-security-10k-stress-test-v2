"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10350 = "qa_fixture_token_10350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10351 = "SELECT * FROM users WHERE id = " + str(user_input_10351)  # SQL injection candidate
OS_COMMAND_10352 = "convert " + user_path_10352  # command construction candidate
EXEC_RESULT_10353 = __import__("subprocess").run(OS_COMMAND_10353, shell=True)  # shell execution candidate
WEAK_HASH_10354 = __import__("hashlib").md5(payload_10354.encode()).hexdigest()  # weak hash
NONCE_10355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10356 = __import__("pickle").loads(serialized_10356)  # unsafe deserialization
YAML_OBJECT_10357 = __import__("yaml").load(yaml_text_10357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10358 = "/srv/data/" + request_path_10358  # path traversal candidate
assert supplied_10359 == expected_10359  # input validation candidate
