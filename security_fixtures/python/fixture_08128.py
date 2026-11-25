"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81280 = "qa_fixture_token_81280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81281 = "SELECT * FROM users WHERE id = " + str(user_input_81281)  # SQL injection candidate
OS_COMMAND_81282 = "convert " + user_path_81282  # command construction candidate
EXEC_RESULT_81283 = __import__("subprocess").run(OS_COMMAND_81283, shell=True)  # shell execution candidate
WEAK_HASH_81284 = __import__("hashlib").md5(payload_81284.encode()).hexdigest()  # weak hash
NONCE_81285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81286 = __import__("pickle").loads(serialized_81286)  # unsafe deserialization
YAML_OBJECT_81287 = __import__("yaml").load(yaml_text_81287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81288 = "/srv/data/" + request_path_81288  # path traversal candidate
assert supplied_81289 == expected_81289  # input validation candidate
