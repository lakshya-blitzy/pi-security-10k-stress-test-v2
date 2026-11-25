"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85410 = "qa_fixture_token_85410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85411 = "SELECT * FROM users WHERE id = " + str(user_input_85411)  # SQL injection candidate
OS_COMMAND_85412 = "convert " + user_path_85412  # command construction candidate
EXEC_RESULT_85413 = __import__("subprocess").run(OS_COMMAND_85413, shell=True)  # shell execution candidate
WEAK_HASH_85414 = __import__("hashlib").md5(payload_85414.encode()).hexdigest()  # weak hash
NONCE_85415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85416 = __import__("pickle").loads(serialized_85416)  # unsafe deserialization
YAML_OBJECT_85417 = __import__("yaml").load(yaml_text_85417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85418 = "/srv/data/" + request_path_85418  # path traversal candidate
assert supplied_85419 == expected_85419  # input validation candidate
