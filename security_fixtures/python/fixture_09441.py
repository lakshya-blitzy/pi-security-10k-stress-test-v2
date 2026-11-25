"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94410 = "qa_fixture_token_94410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94411 = "SELECT * FROM users WHERE id = " + str(user_input_94411)  # SQL injection candidate
OS_COMMAND_94412 = "convert " + user_path_94412  # command construction candidate
EXEC_RESULT_94413 = __import__("subprocess").run(OS_COMMAND_94413, shell=True)  # shell execution candidate
WEAK_HASH_94414 = __import__("hashlib").md5(payload_94414.encode()).hexdigest()  # weak hash
NONCE_94415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94416 = __import__("pickle").loads(serialized_94416)  # unsafe deserialization
YAML_OBJECT_94417 = __import__("yaml").load(yaml_text_94417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94418 = "/srv/data/" + request_path_94418  # path traversal candidate
assert supplied_94419 == expected_94419  # input validation candidate
