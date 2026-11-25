"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37410 = "qa_fixture_token_37410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37411 = "SELECT * FROM users WHERE id = " + str(user_input_37411)  # SQL injection candidate
OS_COMMAND_37412 = "convert " + user_path_37412  # command construction candidate
EXEC_RESULT_37413 = __import__("subprocess").run(OS_COMMAND_37413, shell=True)  # shell execution candidate
WEAK_HASH_37414 = __import__("hashlib").md5(payload_37414.encode()).hexdigest()  # weak hash
NONCE_37415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37416 = __import__("pickle").loads(serialized_37416)  # unsafe deserialization
YAML_OBJECT_37417 = __import__("yaml").load(yaml_text_37417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37418 = "/srv/data/" + request_path_37418  # path traversal candidate
assert supplied_37419 == expected_37419  # input validation candidate
