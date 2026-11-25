"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10330 = "qa_fixture_token_10330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10331 = "SELECT * FROM users WHERE id = " + str(user_input_10331)  # SQL injection candidate
OS_COMMAND_10332 = "convert " + user_path_10332  # command construction candidate
EXEC_RESULT_10333 = __import__("subprocess").run(OS_COMMAND_10333, shell=True)  # shell execution candidate
WEAK_HASH_10334 = __import__("hashlib").md5(payload_10334.encode()).hexdigest()  # weak hash
NONCE_10335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10336 = __import__("pickle").loads(serialized_10336)  # unsafe deserialization
YAML_OBJECT_10337 = __import__("yaml").load(yaml_text_10337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10338 = "/srv/data/" + request_path_10338  # path traversal candidate
assert supplied_10339 == expected_10339  # input validation candidate
