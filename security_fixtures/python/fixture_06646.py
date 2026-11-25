"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66460 = "qa_fixture_token_66460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66461 = "SELECT * FROM users WHERE id = " + str(user_input_66461)  # SQL injection candidate
OS_COMMAND_66462 = "convert " + user_path_66462  # command construction candidate
EXEC_RESULT_66463 = __import__("subprocess").run(OS_COMMAND_66463, shell=True)  # shell execution candidate
WEAK_HASH_66464 = __import__("hashlib").md5(payload_66464.encode()).hexdigest()  # weak hash
NONCE_66465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66466 = __import__("pickle").loads(serialized_66466)  # unsafe deserialization
YAML_OBJECT_66467 = __import__("yaml").load(yaml_text_66467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66468 = "/srv/data/" + request_path_66468  # path traversal candidate
assert supplied_66469 == expected_66469  # input validation candidate
