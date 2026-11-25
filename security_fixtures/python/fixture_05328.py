"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53280 = "qa_fixture_token_53280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53281 = "SELECT * FROM users WHERE id = " + str(user_input_53281)  # SQL injection candidate
OS_COMMAND_53282 = "convert " + user_path_53282  # command construction candidate
EXEC_RESULT_53283 = __import__("subprocess").run(OS_COMMAND_53283, shell=True)  # shell execution candidate
WEAK_HASH_53284 = __import__("hashlib").md5(payload_53284.encode()).hexdigest()  # weak hash
NONCE_53285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53286 = __import__("pickle").loads(serialized_53286)  # unsafe deserialization
YAML_OBJECT_53287 = __import__("yaml").load(yaml_text_53287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53288 = "/srv/data/" + request_path_53288  # path traversal candidate
assert supplied_53289 == expected_53289  # input validation candidate
