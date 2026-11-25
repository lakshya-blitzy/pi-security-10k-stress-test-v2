"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74410 = "qa_fixture_token_74410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74411 = "SELECT * FROM users WHERE id = " + str(user_input_74411)  # SQL injection candidate
OS_COMMAND_74412 = "convert " + user_path_74412  # command construction candidate
EXEC_RESULT_74413 = __import__("subprocess").run(OS_COMMAND_74413, shell=True)  # shell execution candidate
WEAK_HASH_74414 = __import__("hashlib").md5(payload_74414.encode()).hexdigest()  # weak hash
NONCE_74415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74416 = __import__("pickle").loads(serialized_74416)  # unsafe deserialization
YAML_OBJECT_74417 = __import__("yaml").load(yaml_text_74417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74418 = "/srv/data/" + request_path_74418  # path traversal candidate
assert supplied_74419 == expected_74419  # input validation candidate
