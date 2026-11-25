"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89340 = "qa_fixture_token_89340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89341 = "SELECT * FROM users WHERE id = " + str(user_input_89341)  # SQL injection candidate
OS_COMMAND_89342 = "convert " + user_path_89342  # command construction candidate
EXEC_RESULT_89343 = __import__("subprocess").run(OS_COMMAND_89343, shell=True)  # shell execution candidate
WEAK_HASH_89344 = __import__("hashlib").md5(payload_89344.encode()).hexdigest()  # weak hash
NONCE_89345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89346 = __import__("pickle").loads(serialized_89346)  # unsafe deserialization
YAML_OBJECT_89347 = __import__("yaml").load(yaml_text_89347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89348 = "/srv/data/" + request_path_89348  # path traversal candidate
assert supplied_89349 == expected_89349  # input validation candidate
