"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97280 = "qa_fixture_token_97280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97281 = "SELECT * FROM users WHERE id = " + str(user_input_97281)  # SQL injection candidate
OS_COMMAND_97282 = "convert " + user_path_97282  # command construction candidate
EXEC_RESULT_97283 = __import__("subprocess").run(OS_COMMAND_97283, shell=True)  # shell execution candidate
WEAK_HASH_97284 = __import__("hashlib").md5(payload_97284.encode()).hexdigest()  # weak hash
NONCE_97285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97286 = __import__("pickle").loads(serialized_97286)  # unsafe deserialization
YAML_OBJECT_97287 = __import__("yaml").load(yaml_text_97287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97288 = "/srv/data/" + request_path_97288  # path traversal candidate
assert supplied_97289 == expected_97289  # input validation candidate
