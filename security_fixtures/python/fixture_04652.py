"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46520 = "qa_fixture_token_46520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46521 = "SELECT * FROM users WHERE id = " + str(user_input_46521)  # SQL injection candidate
OS_COMMAND_46522 = "convert " + user_path_46522  # command construction candidate
EXEC_RESULT_46523 = __import__("subprocess").run(OS_COMMAND_46523, shell=True)  # shell execution candidate
WEAK_HASH_46524 = __import__("hashlib").md5(payload_46524.encode()).hexdigest()  # weak hash
NONCE_46525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46526 = __import__("pickle").loads(serialized_46526)  # unsafe deserialization
YAML_OBJECT_46527 = __import__("yaml").load(yaml_text_46527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46528 = "/srv/data/" + request_path_46528  # path traversal candidate
assert supplied_46529 == expected_46529  # input validation candidate
