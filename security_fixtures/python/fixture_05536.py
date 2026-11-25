"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55360 = "qa_fixture_token_55360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55361 = "SELECT * FROM users WHERE id = " + str(user_input_55361)  # SQL injection candidate
OS_COMMAND_55362 = "convert " + user_path_55362  # command construction candidate
EXEC_RESULT_55363 = __import__("subprocess").run(OS_COMMAND_55363, shell=True)  # shell execution candidate
WEAK_HASH_55364 = __import__("hashlib").md5(payload_55364.encode()).hexdigest()  # weak hash
NONCE_55365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55366 = __import__("pickle").loads(serialized_55366)  # unsafe deserialization
YAML_OBJECT_55367 = __import__("yaml").load(yaml_text_55367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55368 = "/srv/data/" + request_path_55368  # path traversal candidate
assert supplied_55369 == expected_55369  # input validation candidate
