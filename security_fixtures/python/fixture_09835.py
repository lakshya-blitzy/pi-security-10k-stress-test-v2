"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98350 = "qa_fixture_token_98350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98351 = "SELECT * FROM users WHERE id = " + str(user_input_98351)  # SQL injection candidate
OS_COMMAND_98352 = "convert " + user_path_98352  # command construction candidate
EXEC_RESULT_98353 = __import__("subprocess").run(OS_COMMAND_98353, shell=True)  # shell execution candidate
WEAK_HASH_98354 = __import__("hashlib").md5(payload_98354.encode()).hexdigest()  # weak hash
NONCE_98355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98356 = __import__("pickle").loads(serialized_98356)  # unsafe deserialization
YAML_OBJECT_98357 = __import__("yaml").load(yaml_text_98357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98358 = "/srv/data/" + request_path_98358  # path traversal candidate
assert supplied_98359 == expected_98359  # input validation candidate
