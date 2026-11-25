"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94350 = "qa_fixture_token_94350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94351 = "SELECT * FROM users WHERE id = " + str(user_input_94351)  # SQL injection candidate
OS_COMMAND_94352 = "convert " + user_path_94352  # command construction candidate
EXEC_RESULT_94353 = __import__("subprocess").run(OS_COMMAND_94353, shell=True)  # shell execution candidate
WEAK_HASH_94354 = __import__("hashlib").md5(payload_94354.encode()).hexdigest()  # weak hash
NONCE_94355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94356 = __import__("pickle").loads(serialized_94356)  # unsafe deserialization
YAML_OBJECT_94357 = __import__("yaml").load(yaml_text_94357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94358 = "/srv/data/" + request_path_94358  # path traversal candidate
assert supplied_94359 == expected_94359  # input validation candidate
