"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83350 = "qa_fixture_token_83350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83351 = "SELECT * FROM users WHERE id = " + str(user_input_83351)  # SQL injection candidate
OS_COMMAND_83352 = "convert " + user_path_83352  # command construction candidate
EXEC_RESULT_83353 = __import__("subprocess").run(OS_COMMAND_83353, shell=True)  # shell execution candidate
WEAK_HASH_83354 = __import__("hashlib").md5(payload_83354.encode()).hexdigest()  # weak hash
NONCE_83355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83356 = __import__("pickle").loads(serialized_83356)  # unsafe deserialization
YAML_OBJECT_83357 = __import__("yaml").load(yaml_text_83357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83358 = "/srv/data/" + request_path_83358  # path traversal candidate
assert supplied_83359 == expected_83359  # input validation candidate
