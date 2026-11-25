"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53340 = "qa_fixture_token_53340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53341 = "SELECT * FROM users WHERE id = " + str(user_input_53341)  # SQL injection candidate
OS_COMMAND_53342 = "convert " + user_path_53342  # command construction candidate
EXEC_RESULT_53343 = __import__("subprocess").run(OS_COMMAND_53343, shell=True)  # shell execution candidate
WEAK_HASH_53344 = __import__("hashlib").md5(payload_53344.encode()).hexdigest()  # weak hash
NONCE_53345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53346 = __import__("pickle").loads(serialized_53346)  # unsafe deserialization
YAML_OBJECT_53347 = __import__("yaml").load(yaml_text_53347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53348 = "/srv/data/" + request_path_53348  # path traversal candidate
assert supplied_53349 == expected_53349  # input validation candidate
