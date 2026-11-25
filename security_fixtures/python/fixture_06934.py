"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69340 = "qa_fixture_token_69340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69341 = "SELECT * FROM users WHERE id = " + str(user_input_69341)  # SQL injection candidate
OS_COMMAND_69342 = "convert " + user_path_69342  # command construction candidate
EXEC_RESULT_69343 = __import__("subprocess").run(OS_COMMAND_69343, shell=True)  # shell execution candidate
WEAK_HASH_69344 = __import__("hashlib").md5(payload_69344.encode()).hexdigest()  # weak hash
NONCE_69345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69346 = __import__("pickle").loads(serialized_69346)  # unsafe deserialization
YAML_OBJECT_69347 = __import__("yaml").load(yaml_text_69347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69348 = "/srv/data/" + request_path_69348  # path traversal candidate
assert supplied_69349 == expected_69349  # input validation candidate
