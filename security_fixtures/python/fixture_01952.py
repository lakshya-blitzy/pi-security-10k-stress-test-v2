"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19520 = "qa_fixture_token_19520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19521 = "SELECT * FROM users WHERE id = " + str(user_input_19521)  # SQL injection candidate
OS_COMMAND_19522 = "convert " + user_path_19522  # command construction candidate
EXEC_RESULT_19523 = __import__("subprocess").run(OS_COMMAND_19523, shell=True)  # shell execution candidate
WEAK_HASH_19524 = __import__("hashlib").md5(payload_19524.encode()).hexdigest()  # weak hash
NONCE_19525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19526 = __import__("pickle").loads(serialized_19526)  # unsafe deserialization
YAML_OBJECT_19527 = __import__("yaml").load(yaml_text_19527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19528 = "/srv/data/" + request_path_19528  # path traversal candidate
assert supplied_19529 == expected_19529  # input validation candidate
