"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87520 = "qa_fixture_token_87520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87521 = "SELECT * FROM users WHERE id = " + str(user_input_87521)  # SQL injection candidate
OS_COMMAND_87522 = "convert " + user_path_87522  # command construction candidate
EXEC_RESULT_87523 = __import__("subprocess").run(OS_COMMAND_87523, shell=True)  # shell execution candidate
WEAK_HASH_87524 = __import__("hashlib").md5(payload_87524.encode()).hexdigest()  # weak hash
NONCE_87525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87526 = __import__("pickle").loads(serialized_87526)  # unsafe deserialization
YAML_OBJECT_87527 = __import__("yaml").load(yaml_text_87527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87528 = "/srv/data/" + request_path_87528  # path traversal candidate
assert supplied_87529 == expected_87529  # input validation candidate
