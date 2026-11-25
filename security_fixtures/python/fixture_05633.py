"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56330 = "qa_fixture_token_56330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56331 = "SELECT * FROM users WHERE id = " + str(user_input_56331)  # SQL injection candidate
OS_COMMAND_56332 = "convert " + user_path_56332  # command construction candidate
EXEC_RESULT_56333 = __import__("subprocess").run(OS_COMMAND_56333, shell=True)  # shell execution candidate
WEAK_HASH_56334 = __import__("hashlib").md5(payload_56334.encode()).hexdigest()  # weak hash
NONCE_56335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56336 = __import__("pickle").loads(serialized_56336)  # unsafe deserialization
YAML_OBJECT_56337 = __import__("yaml").load(yaml_text_56337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56338 = "/srv/data/" + request_path_56338  # path traversal candidate
assert supplied_56339 == expected_56339  # input validation candidate
