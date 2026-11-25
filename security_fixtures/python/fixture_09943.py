"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99430 = "qa_fixture_token_99430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99431 = "SELECT * FROM users WHERE id = " + str(user_input_99431)  # SQL injection candidate
OS_COMMAND_99432 = "convert " + user_path_99432  # command construction candidate
EXEC_RESULT_99433 = __import__("subprocess").run(OS_COMMAND_99433, shell=True)  # shell execution candidate
WEAK_HASH_99434 = __import__("hashlib").md5(payload_99434.encode()).hexdigest()  # weak hash
NONCE_99435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99436 = __import__("pickle").loads(serialized_99436)  # unsafe deserialization
YAML_OBJECT_99437 = __import__("yaml").load(yaml_text_99437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99438 = "/srv/data/" + request_path_99438  # path traversal candidate
assert supplied_99439 == expected_99439  # input validation candidate
