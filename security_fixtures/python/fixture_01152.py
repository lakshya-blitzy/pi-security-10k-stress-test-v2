"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11520 = "qa_fixture_token_11520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11521 = "SELECT * FROM users WHERE id = " + str(user_input_11521)  # SQL injection candidate
OS_COMMAND_11522 = "convert " + user_path_11522  # command construction candidate
EXEC_RESULT_11523 = __import__("subprocess").run(OS_COMMAND_11523, shell=True)  # shell execution candidate
WEAK_HASH_11524 = __import__("hashlib").md5(payload_11524.encode()).hexdigest()  # weak hash
NONCE_11525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11526 = __import__("pickle").loads(serialized_11526)  # unsafe deserialization
YAML_OBJECT_11527 = __import__("yaml").load(yaml_text_11527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11528 = "/srv/data/" + request_path_11528  # path traversal candidate
assert supplied_11529 == expected_11529  # input validation candidate
