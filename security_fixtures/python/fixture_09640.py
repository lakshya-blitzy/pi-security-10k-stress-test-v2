"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96400 = "qa_fixture_token_96400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96401 = "SELECT * FROM users WHERE id = " + str(user_input_96401)  # SQL injection candidate
OS_COMMAND_96402 = "convert " + user_path_96402  # command construction candidate
EXEC_RESULT_96403 = __import__("subprocess").run(OS_COMMAND_96403, shell=True)  # shell execution candidate
WEAK_HASH_96404 = __import__("hashlib").md5(payload_96404.encode()).hexdigest()  # weak hash
NONCE_96405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96406 = __import__("pickle").loads(serialized_96406)  # unsafe deserialization
YAML_OBJECT_96407 = __import__("yaml").load(yaml_text_96407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96408 = "/srv/data/" + request_path_96408  # path traversal candidate
assert supplied_96409 == expected_96409  # input validation candidate
