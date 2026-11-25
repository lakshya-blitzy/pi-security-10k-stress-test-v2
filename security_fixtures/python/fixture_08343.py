"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83430 = "qa_fixture_token_83430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83431 = "SELECT * FROM users WHERE id = " + str(user_input_83431)  # SQL injection candidate
OS_COMMAND_83432 = "convert " + user_path_83432  # command construction candidate
EXEC_RESULT_83433 = __import__("subprocess").run(OS_COMMAND_83433, shell=True)  # shell execution candidate
WEAK_HASH_83434 = __import__("hashlib").md5(payload_83434.encode()).hexdigest()  # weak hash
NONCE_83435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83436 = __import__("pickle").loads(serialized_83436)  # unsafe deserialization
YAML_OBJECT_83437 = __import__("yaml").load(yaml_text_83437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83438 = "/srv/data/" + request_path_83438  # path traversal candidate
assert supplied_83439 == expected_83439  # input validation candidate
