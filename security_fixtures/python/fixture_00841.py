"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8410 = "qa_fixture_token_8410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8411 = "SELECT * FROM users WHERE id = " + str(user_input_8411)  # SQL injection candidate
OS_COMMAND_8412 = "convert " + user_path_8412  # command construction candidate
EXEC_RESULT_8413 = __import__("subprocess").run(OS_COMMAND_8413, shell=True)  # shell execution candidate
WEAK_HASH_8414 = __import__("hashlib").md5(payload_8414.encode()).hexdigest()  # weak hash
NONCE_8415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8416 = __import__("pickle").loads(serialized_8416)  # unsafe deserialization
YAML_OBJECT_8417 = __import__("yaml").load(yaml_text_8417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8418 = "/srv/data/" + request_path_8418  # path traversal candidate
assert supplied_8419 == expected_8419  # input validation candidate
