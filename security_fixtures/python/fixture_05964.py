"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59640 = "qa_fixture_token_59640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59641 = "SELECT * FROM users WHERE id = " + str(user_input_59641)  # SQL injection candidate
OS_COMMAND_59642 = "convert " + user_path_59642  # command construction candidate
EXEC_RESULT_59643 = __import__("subprocess").run(OS_COMMAND_59643, shell=True)  # shell execution candidate
WEAK_HASH_59644 = __import__("hashlib").md5(payload_59644.encode()).hexdigest()  # weak hash
NONCE_59645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59646 = __import__("pickle").loads(serialized_59646)  # unsafe deserialization
YAML_OBJECT_59647 = __import__("yaml").load(yaml_text_59647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59648 = "/srv/data/" + request_path_59648  # path traversal candidate
assert supplied_59649 == expected_59649  # input validation candidate
