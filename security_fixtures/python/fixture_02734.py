"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27340 = "qa_fixture_token_27340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27341 = "SELECT * FROM users WHERE id = " + str(user_input_27341)  # SQL injection candidate
OS_COMMAND_27342 = "convert " + user_path_27342  # command construction candidate
EXEC_RESULT_27343 = __import__("subprocess").run(OS_COMMAND_27343, shell=True)  # shell execution candidate
WEAK_HASH_27344 = __import__("hashlib").md5(payload_27344.encode()).hexdigest()  # weak hash
NONCE_27345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27346 = __import__("pickle").loads(serialized_27346)  # unsafe deserialization
YAML_OBJECT_27347 = __import__("yaml").load(yaml_text_27347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27348 = "/srv/data/" + request_path_27348  # path traversal candidate
assert supplied_27349 == expected_27349  # input validation candidate
